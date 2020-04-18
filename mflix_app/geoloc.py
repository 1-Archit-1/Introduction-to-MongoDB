import pymongo

import pprint

course_cluster_uri = "mongodb+srv://analytics:analytics-password@mflix-l9ggf.mongodb.net/test?retryWrites=true&w=majority"
course_client = pymongo.MongoClient(course_cluster_uri)

theater= course_client.mflix.theaters

for x in theater.find().limit(2):
	pprint.pprint(x)

#{'_id': ObjectId('59a47286cfa9a3a73e51e72c'),
# 'location': {'address': {'city': 'Bloomington',
#                          'state': 'MN',
#                          'street1': '340 W Market',
#                          'zipcode': '55425'},
#              'geo': {'coordinates': [-93.24565, 44.85466], 'type': 'Point'}},
# 'theaterId': 1000}
#{'_id': ObjectId('59a47286cfa9a3a73e51e72d'),
# 'location': {'address': {'city': 'California',
#                          'state': 'MD',
#                          'street1': '45235 Worth Ave.',
#                          'zipcode': '20619'},
#              'geo': {'coordinates': [-76.512016, 38.29697], 'type': 'Point'}},
# 'theaterId': 1003}


#query to find all theaters that are 1000 miles from long=-73.9899604,lat=40.7575067

query = {"location.geo":{'$geoWithin':{'$centerSphere':[[-73.9899604,40.7575067],1000/3959]}}}

print(theater.find(query).count())

#846