import pymongo 
from pymongo import MongoClient
import pprint

client=MongoClient("mongodb+srv://analytics:analytics-password@mflix-l9ggf.mongodb.net/test?retryWrites=true&w=majority")


pipeline=[
			{
				'$limit': 100
			},
			# $addFields stage adds new fields.
		    # Since "lastupdated" field contains too many trailing 0s in the string
		    # representation of the timestamp, we need to trim them off, to be able to
		    # parse out a date from it.
#		    {
#		        '$addFields': {
#		            'lastupdated': {
#		                '$arrayElemAt': [  # Take the element at the given index in the given array
#		                    {'$split': ['$lastupdated', '.']},
#		                    0
#		                ]
#		            }  # Note that since "lastupdated" field already exists, its value will be replaced
#		        }
#		    },  
			{
				'$project': {
					'title': '$title',
					'year':'$year',
					'rating':'$rating',
					'runtime': {'$split':["$runtime"," "]},
					'genres' : {'$split': ["$genre",", "]},
					'released': {'$cond': {
									'if':{'$ne':["$released",""]},
									'then':{
										'$dateFromString':{
											'dateString':"$released"
										}
									},
									'else':""}},

					'direcetors':{'$split': ["$director",", "]},
					'writers':{'$split': ["$writers",", "]},
					'cast':{'$split': ["$cast",", "]},
					'metacritic':'$metacritic',
					'IMDB':{
						'ID':'$imdbID',
						'rating':'$imdbRating',
						'votes':'$imdbVotes'
					},
					'poster':1,
					'plot':1,
					'fullplot':1,
					'languages':{'$split': ["$language",", "]},
					'countries':{'$split': ["$country",", "]},
					'awards':1,
					'lastupdated': { '$cond':{
										'if':{'$ne':['$lastupdated','']},
										'then':{'$dateFromString':{
														'dateString': {'$substr':['$lastupdated',0,22]}
										}
										},
										'else':""}},		
					'type':1
				}
			},
			{
				'$out':'movies_scratch'
			}

]

pprint.pprint(list(client.mflix.movies_initial.aggregate(pipeline)))
