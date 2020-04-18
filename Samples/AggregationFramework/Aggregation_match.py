import pymongo
from pymongo import MongoClient
import pprint

cli=MongoClient("mongodb+srv://analytics:analytics-password@mflix-l9ggf.mongodb.net/test?retryWrites=true&w=majority")

movies_initial = cli.mflix.movies_initial

pipeline = [
    {
        '$match': {'language': 'Mandarin, English'}
    }  # stage1: 'match' stage
]
# Note that we can totally use movies_initial.find() method to filter, since
# this is a very simply case where we only have one stage in the pipeline

for result in movies_initial.aggregate(pipeline):
    pprint.pprint(result)