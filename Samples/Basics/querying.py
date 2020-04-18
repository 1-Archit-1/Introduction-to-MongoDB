import pymongo
from pymongo import MongoClient
import pprint

client=MongoClient("mongodb+srv://analytics:analytics-password@mflix-l9ggf.mongodb.net/test?retryWrites=true&w=majority")


mydb=client.mflix
mycol=mydb.movies_inital
#x=client.mflix.movies_initial.find({}).limit(10)
#x=client.mflix.movies_initial.find({"year":{'$gt':2016},"title":{'$regex':'^T'}},{"title":1,"year":1}).sort("year",-1)

client.mflix.movies_initial.update_one({"title":"The Justice League Part One"},{"$set":{"title":"The Justice League Part 1"}})

x=client.mflix.movies_initial.find({"title":"The Justice League Part 1"})


for i in x:
	print(i)
