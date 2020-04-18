import pymongo
import matplotlib.pyplot as plt

course_cluster_uri = 'mongodb://analytics-student:analytics-password@cluster0-shard-00-00-jxeqq.mongodb.net:27017,cluster0-shard-00-01-jxeqq.mongodb.net:27017,cluster0-shard-00-02-jxeqq.mongodb.net:27017/?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

course_client = pymongo.MongoClient(course_cluster_uri)
weather_data = course_client['100YWeatherSmall'].data

for x in weather_data.find().limit(1):
    print(x)
"""{'_id': ObjectId('5553a98ce4b02cf7150dee3c'),
 'airTemperature': {'quality': '1', 'value': 27.5},
 'callLetters': 'PHQK',
 'dataSource': '4',
 'dewPoint': {'quality': '9', 'value': 999.9},
 'elevation': 9999,
 'pastWeatherObservationManual': [{'atmosphericCondition': {'quality': '1',
                                                            'value': '1'},
                                   'period': {'quality': '1', 'value': 6}}],
 'position': {'coordinates': [86.0, -0.7], 'type': 'Point'},
 'precipitationEstimatedObservation': {'discrepancy': '0',
                                       'estimatedWaterDepth': 999},
 'presentWeatherObservationManual': [{'condition': '15', 'quality': '1'}],
 'pressure': {'quality': '1', 'value': 1012.2},
 'qualityControlProcess': 'V020',
 'sections': ['AG1', 'AY1', 'GF1', 'MW1'],
 'skyCondition': {'cavok': 'N',
                  'ceilingHeight': {'determination': 'C',
                                    'quality': '1',
                                    'value': 22000}},
 'skyConditionObservation': {'highCloudGenus': {'quality': '1', 'value': '00'},
                             'lowCloudGenus': {'quality': '1', 'value': '00'},
                             'lowestCloudBaseHeight': {'quality': '9',
                                                       'value': 99999},
                             'lowestCloudCoverage': {'quality': '1',
                                                     'value': '00'},
                             'midCloudGenus': {'quality': '1', 'value': '00'},
                             'totalCoverage': {'opaque': '99',
                                               'quality': '1',
                                               'value': '00'}},
 'st': 'x-00700+086000',
 'ts': datetime.datetime(1984, 1, 1, 0, 0),
 'type': 'FM-13',
 'visibility': {'distance': {'quality': '1', 'value': 20000},
                'variability': {'quality': '9', 'value': 'N'}},
 'wind': {'direction': {'angle': 290, 'quality': '1'},
          'speed': {'quality': '1', 'rate': 2.6},
          'type': 'N'}}"""

# remove outliers that are clearly bad data
query = { 'pressure.value': { '$lt': 9999 }, 'airTemperature.value': { '$lt': 9999 } }

# convert our cursor into a list
l = list(weather_data.find(query).limit(1000))

# pull out the two variables we care about into their own respective lists
pressures = [x['pressure']['value'] for x in l]
air_temps = [x['airTemperature']['value'] for x in l]


plt.clf()
plt.figure(figsize=(14,11))
plt.scatter(pressures,air_temps)
plt.show()