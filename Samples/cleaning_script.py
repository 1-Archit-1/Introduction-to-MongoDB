
#This module achieves the same operations as Aggregation Framework pipeline using
#PyMongo scripting.
import pymongo
from pymongo import MongoClient
import pprint
from datetime import datetime

client=MongoClient("mongodb+srv://analytics:analytics-password@mflix-l9ggf.mongodb.net/test?retryWrites=true&w=majority")

batch_updates=[]
for movie in client.mflix.movies.find({}):
	fields_to_set={}
	fields_to_unset={}
	# Construct the fields to update (set and unset, respectively)

	for key,value in movie.copy().items():
		
		if value=='' or value=="" or value==[""]or value==['']:
			fields_to_unset[key]=''
			del movie[key]
		# Delete all the fields with empty values

	if 'fullplot' in movie:
		fields_to_set['fullPlot']=movie['fullplot']
		fields_to_unset['fullplot']=''
	#Renaming using camel case
	if 'director' in movie:
		fields_to_set['directors']=movie['director'].split(', ')
		fields_to_unset['director']=''
	# Split some fields from string literals to arrays	
	if 'cast' in movie:
		fields_to_set['actors']=movie['cast'].split(', ')
		fields_to_unset['cast']=''
	# Split some fields from string literals to arrays	
	if 'language' in movie:
		fields_to_set['languages']=movie['language'].split(', ')
		fields_to_unset['language']=''
	if 'country' in movie:
		fields_to_set['countries']=movie['country'].split(', ')

	IMDB={}
	if 'imdbID' in movie:
		IMDB['ID']=movie['imdbID']
		fields_to_unset['imdbID']=''
	#Grouping IMDB fields

	if 'imdbRating'in movie:
		IMDB['Rating']=movie['imdbRating']
		fields_to_unset['imdbRating']=''


	if 'imdbVotes' in movie:
		IMDB['Votes']=movie['imdbVotes']
		fields_to_unset['imdbVotes']=''

	fields_to_set['IMDB']=IMDB

	if 'released' in movie:
		fields_to_set['releaseDate']= datetime.strptime(movie['released'],'%Y-%m-%d')
		fields_to_unset['released']=''

	if 'lastupdated' in movie:
		fields_to_set['lastUpdated']=datetime.strptime(movie['lastupdated'].split('.')[0],'%Y-%m-%d %H:%M:%S')
		fields_to_unset['lastupdated']=''

	update={}
	if fields_to_set:
		update['$set']=fields_to_set
	if fields_to_unset:
		update['$unset']=fields_to_unset
	#setting $set and $unset fields in update document	



	batch_updates.append(pymongo.UpdateOne({'_id':movie['_id']},update=update))
	#Appending updates document to batch_updates 

	if len(batch_updates)==1000:
		client.mflix.movies.bulk_write(batch_updates)
		batch_updates=[]
	#If length reaches 1000 send all the updates

if batch_updates:
	client.mflix.movies.bulk_write(batch_updates)
#This is to write the remaining updates


print('Finished all the updates')




