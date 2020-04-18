import pymongo
from pymongo import MongoClient
import pprint

client=MongoClient("mongodb+srv://analytics:analytics-password@mflix-l9ggf.mongodb.net/test?retryWrites=true&w=majority")


# Define top 100 language combinations as "usual"
top = 100
# Rest: Unusual language combinations

# Main pipeline
pipeline = [
    {
        '$sortByCount': '$language'
    },  # stage1: 'sortByCount' stage

    # $facet stage processes the same input documents through multiple pipelines in parallel

    {
        '$facet': { 
            # pipeline1: 'top language combinations'
            'top language combinations': [
                {'$limit': top}  # 'limit' stage
            ],
            # pipeline2: 'unsual combinations shared by'
            'unusual combinations shared by': [
                {'$skip': top},  # 'skip' stage
                {'$bucketAuto': {
                    'groupBy': '$count',  # Identifier expression to group by
                    'buckets': 5,  # Create <= 5 buckets
                    # This will automatically calculate the range for each
                    # bucket, and put documents within the same range to the
                    # same bucket.
                    'output': {'language combinations': {'$sum': 1}}
                    # For each bucket, it will output the value we specified for
                    # the "output" key.
                }}  
            ]
        }
    }  
]

for result in movies_initial.aggregate(pipeline):
    pprint.pprint(result)
