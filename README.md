# Introduction-to-MongoDB

To import a file to your mongodb cluster go to your databaseand check CLI for mongoimport
You can connect your application using your database connect option and copying the uri
For creation and insertion using CLI check createdb.py 


#Aggregation framework:

$group,
$limit,
$sort,
$skip,
$sortbycount,		
$count,
$project,			
$filter,		
$out				(Aggregation_cleaning)
$addFields
$arrayElemAt        (check cleaning using aggregation)
 

#Queries:

.find(filter,projection)
.limit()			
.sort()
.skip()
.count()
.insert_one()		(check basics)
.insert_many()
.bulk_write			(for insertion you can check Cleaning2.py)
.update_one()       (for updates refer to cleaningscript.py  or cleaning.py)
$set,$unset			(Used for updating)
.format()           (print in a specific format)
.delete_one()
.delete_many()
Dot notation for subdocument queries

#Array update operators
$addToSet
$push
$pop
$pull

#Field update ooperators
$set
$unset
$inc
$min
$max


Filter:: $in:{ [xx,xxx,xxxx]}
		 $nin:
		 $ne    
		 $gt
		 $lt
		 $elemMatch   (for array filters)
		 $eq


explain:    (to explain how the query is being executed)


#Creating Indexes:

db.col.create_index([{"key",pymongo.ASCENDING}])

indexes for text search support can be used , which do not need to match exact values
if the index has been set up
filter={ "$text":{"$search":"Titanic"}}



#Geospatial Queries

$geoWithin
$centerSphere
$nearSphere
