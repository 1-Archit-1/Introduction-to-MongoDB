import pymongo
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

course_cluster_uri = 'mongodb://analytics-student:analytics-password@cluster0-shard-00-00-jxeqq.mongodb.net:27017,cluster0-shard-00-01-jxeqq.mongodb.net:27017,cluster0-shard-00-02-jxeqq.mongodb.net:27017/?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

course_client = pymongo.MongoClient(course_cluster_uri)
weather_data = course_client['100YWeatherSmall'].data

# remove outliers that are clearly bad data
query = { 
    'pressure.value': { '$lt': 9999 }, 
    'airTemperature.value': { '$lt': 9999 },
    'wind.speed.rate': { '$lt': 500 },
}

# convert our cursor into a list
l = list(weather_data.find(query).limit(1000))

# pull out the 3 variables we care about into their own respective lists
pressures = [x['pressure']['value'] for x in l]
air_temps = [x['airTemperature']['value'] for x in l]
wind_speeds = [x['wind']['speed']['rate'] for x in l]

# here you'll write the code to plot pressures, air_temps, and wind_speeds in a 3D plot

plt.clf()
fig=plt.figure()
ax=plt.axes(projection="3d")
ax.scatter(pressures,air_temps,wind_speeds)
ax.set_xlabel("Pressure")
ax.set_ylabel("temperature")
ax.set_zlabel("wind speed")
plt.show()



