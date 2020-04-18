import pymongo

import pprint


free_tier_client=pymongo.MongoClient("mongodb+srv://analytics:analytics-password@mflix-l9ggf.mongodb.net/test?retryWrites=true&w=majority")

​

# We're using the people-raw dataset from the Cleansing Data with Updates assessment

people = free_tier_client.cleansing["people-raw"]

# This is a helper function to reduce the output of explain to a few key metrics

def distilled_explain(explain_output):

    return {

        'executionTimeMillis': explain_output['executionStats']['executionTimeMillis'],

        'totalDocsExamined'  : explain_output['executionStats']['totalDocsExamined'],

        'nReturned'          : explain_output['executionStats']['nReturned']

    }

query_1_stats = people.find({

  "address.state": "Nebraska",

  "last_name": "Miller",

}).explain()

​

query_2_stats = people.find({

  "first_name": "Harry",

  "last_name": "Reed"

}).explain()

# This is to provide a baseline for how long it takes to execute these queries

print(distilled_explain(query_1_stats))

print(distilled_explain(query_2_stats))

#{'executionTimeMillis': 54, 'totalDocsExamined': 50474, 'nReturned': 6}
#{'executionTimeMillis': 21, 'totalDocsExamined': 50474, 'nReturned': 1}


people.create_index([('last_name',pymongo.DESCENDING)])

'last_name_-1'

query_1_stats = people.find({

  "address.state": "Nebraska",

  "last_name": "Miller",

}).explain()

​

query_2_stats = people.find({

  "first_name": "Harry",

  "last_name": "Reed"

}).explain()

# If everything went well, both queries should now have *much* lower execution times and documents examined

print(distilled_explain(query_1_stats))

print(distilled_explain(query_2_stats))

#{'executionTimeMillis': 1, 'totalDocsExamined': 533, 'nReturned': 6}
#{'executionTimeMillis': 0, 'totalDocsExamined': 114, 'nReturned': 1}
