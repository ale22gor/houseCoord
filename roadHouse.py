import sys, json
import requests
import np

x=sys.argv[1]
y=sys.argv[2]
r = requests.get('https://nominatim.openstreetmap.org/search.php?q='+x+'%2C'+y+'&polygon_geojson=1&format=jsonv2')
coordinates = r.json()[0]['geojson']['coordinates']
for pair in coordinates[0]:
    pair[0], pair[1] = pair[1], pair[0]


coordinates = np.array(coordinates)
coordinates = coordinates.ravel()
rawCoord = ','.join(map(str, coordinates))
print(rawCoord)
