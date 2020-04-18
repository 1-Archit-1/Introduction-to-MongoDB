import pymongo 
from pymongo import MongoClient
import pprint

client = pymongo.MongoClient("mongodb+srv://analytics:analytics-password@mflix-l9ggf.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
print(client.mflix)
pipeline= [
    {            
        '$group': 
            { 
                '_id': '$director',
                'count':{ '$sum':1 }
            
            }
            #This groups using the director key and stores the number of items per group in the var count
    } ,
    {
    	'$limit':20  #Limiting to 20 documents
    } ,
    {
    	'$sort': {'count':-1}    #Sort in descending order (use +1 for ascending)
    }    

]

#Each stage of the pipeline is executed sequentially


#pipeline = [
#    {
#        '$sortByCount': '$director'
#    }  # stage1: 'sortByCount' stage
#]

#This does the same thing using 'sortByCount' parameter

pprint.pprint(list(client.mflix.movies_initial.aggregate(pipeline)))