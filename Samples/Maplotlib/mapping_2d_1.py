# matplotlib makes it easy to plot data; basemap makes it easy to plot on a map with matplotlib
!pip install matplotlib
# Python 3 doesn't currently support basemap this exercise can be performed on Python 2
#!conda install -y basemap

import pymongo
import pprint

import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap

course_cluster_uri = 'mongodb://analytics-student:analytics-password@cluster0-shard-00-00-jxeqq.mongodb.net:27017,cluster0-shard-00-01-jxeqq.mongodb.net:27017,cluster0-shard-00-02-jxeqq.mongodb.net:27017/?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

course_client = pymongo.MongoClient(course_cluster_uri)
shipwrecks = course_client.ships.shipwrecks

# Let's get all of the shipwrecks and convert our cursor into a list
l = list(shipwrecks.find({}))
for x in shipwrecks.find().limit(2):
    print(x)

#{'_id': ObjectId('578f6fa3df35c7fbdbaeea05'), 'recrd': '', 'vesslterms': '', 'feature_type': 'Wrecks - Visible', 'chart': 'US,US,graph,Chart 11553', 'latdec': 35.5390359, 'londec': -76.6260807, 'gp_quality': '', 'depth': '', 'sounding_type': '', 'yearsunk': '', 'history': '', 'quasou': '', 'watlev': 'always dry', 'coordinates': [-76.6260807, 35.5390359]}
#{'_id': ObjectId('578f6fa3df35c7fbdbaee9c4'), 'recrd': '', 'vesslterms': '', 'feature_type': 'Wrecks - Submerged, dangerous', 'chart': 'US,US,graph,Chart 11552', 'latdec': 35.015018, 'londec': -76.690048, 'gp_quality': '', 'depth': '', 'sounding_type': '', 'yearsunk': '', 'history': '', 'quasou': 'depth unknown', 'watlev': 'always under water/submerged', 'coordinates': [-76.690048, 35.015018]}


# Here you need to use our list of shipwrecks, l, and pull out the longitudes (XXXX) and latitudes (YYYY)
lngs = [shipw['londec'] for shipw in l]
lats = [shipw['latdec'] for shipw in l]

# Clear the figure (this is nice if you execute the cell multiple times)
plt.clf()

# Set the size of our figure
plt.figure(figsize=(14, 8))

# Set the center of our map with our first pair of coordinates and set the projection

#######m = Basemap(lat_0=lats[0], lon_0=lngs[0], projection='cyl')

# Draw the coastlines and the states
#######m.drawcoastlines()
#######m.drawstates()

# Convert our coordinates to the system that the projection uses
#######x, y = m(lngs, lats)

# Plot our converted coordinates
plt.scatter(lngs, lats)

# Display our beautiful map
plt.show()