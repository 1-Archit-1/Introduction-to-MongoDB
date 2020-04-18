# We're going to install this module to help us parse datetimes from the raw dataset
!pip install dateparser

from pymongo import MongoClient, InsertOne, UpdateOne
import pprint
import dateparser
from bson.json_util import loads

# Replace XXXX with your connection URI from the Atlas UI
client = MongoClient("mongodb+srv://analytics:analytics-password@mflix-l9ggf.mongodb.net/test?retryWrites=true&w=majority")

people_raw = client.cleansing['people-raw']

batch_size = 1000
inserts = []
count = 0

    # Instead of updating one document at a time, we will add the current update
    # to a batch of updates, and when the current batch size reaches the batch
    # size limit, send the batch updates to the server at once.
with open("./people-raw.json") as dataset: 
    for line in dataset: 
        inserts.append(InsertOne(loads(line)))
        
        count += 1
                       
        if count == batch_size:
            people_raw.bulk_write(inserts)
            inserts = []
            count = 0
if inserts:         
    people_raw.bulk_write(inserts)
    count = 0

# Confirm that 50,474 documents are in your collection before moving on
people_raw.count()


people_with_string_birthdays = people_raw.find({'birthday':{ '$type':'string'}})



people_with_string_birthdays.count()

updates = []
# Again, we're updating several thousand documents, so this will take a little while
for person in people_with_string_birthdays:
    # Pymongo converts datetime objects into BSON Dates. The dateparser.parse function returns a
    # datetime object, so we can simply do the following to update the field properly.

    updates.append(UpdateOne({ "_id": person["_id"] }, { '$set': { "birthday": dateparser.parse(person["birthday"]) } }))
    
    count += 1
                       
    if count == batch_size:
        people_raw.bulk_write(updates)
        updates = []
        count = 0
        
if updates:         
    people_raw.bulk_write(updates)
    count = 0


# If everything went well this should be zero
people_with_string_birthdays.count()