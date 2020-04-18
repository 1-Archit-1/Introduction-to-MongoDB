import pymongo
import matplotlib.pyplot as plt
import dateparser

course_cluster_uri = 'mongodb://analytics-student:analytics-password@cluster0-shard-00-00-jxeqq.mongodb.net:27017,cluster0-shard-00-01-jxeqq.mongodb.net:27017,cluster0-shard-00-02-jxeqq.mongodb.net:27017/?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

course_client = pymongo.MongoClient(course_cluster_uri)
trips = course_client.citibike.trips

cursor = trips.aggregate([
  {
    "$match": {
      # filter the results to January 2016
      "start time": {
        "$gte": dateparser.parse("1/1/2016"),
        "$lt": dateparser.parse("2/1/2016")
      },
      # filter to trips under an hour
      "tripduration": {
        "$lt": 3600
      }
    }
  },
  {
    # sort by a bikeid so our results aren't chronological (so our limit of 2,500 aren't all on the same day)
    "$sort": { "bikeid": 1 }
  },
  {
    # limit to the first 2,500
    "$limit": 2500
  },
  {
    # convert start time to an integer representing the day of the week
    "$addFields": { "dayOfWeek": { "$dayOfWeek": "$start time" } }
  },
  {
    # group by the day of the week, pushing each trip into an array
    "$group": { "_id": "$dayOfWeek", "trips": { "$push": "$$ROOT" } }
  },
  {
    # sort our results by day of week, so it goes Sun, Mon, Tues, Wed, Thur, Fri, Sat
    "$sort": { "_id": 1 }
  }
]);

# iterate through our cursor, pulling out the array of trips for each day of the week
trips_by_day = [doc['trips'] for doc in cursor]

# pull out the trip duration and convert it from seconds to minutes
trip_durations_by_day = [[trip['tripduration'] / 60 for trip in trips] for trips in trips_by_day]

plt.clf()

fig,ax=plt.subplots()
bp=ax.boxplot(trip_durations_by_day)
ax.set_xticklabels(['Sun','Mon','Tue','Wed','Thurs','Fri','Sat'])
ax.yaxis.grid(True)
plt.show()