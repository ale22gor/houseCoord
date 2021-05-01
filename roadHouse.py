import sys, json
import requests
import np

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if is_number(sys.argv[1]) and is_number(sys.argv[2]):
  x=sys.argv[1]
  y=sys.argv[2] 
  r = requests.get('https://nominatim.openstreetmap.org/search.php?q='+x+'%2C'+y+'&polygon_geojson=1&format=jsonv2')
else:
  print('https://geocode-maps.yandex.ru/1.x/?geocode='+'+'.join(sys.argv[1:]))
  r = requests.get('https://geocode-maps.yandex.ru/1.x/?geocode='+'+'.join(sys.argv[1:]))
  print('wrong')

coordinates = r.json()[0]['geojson']['coordinates']
for pair in coordinates[0]:
    pair[0], pair[1] = pair[1], pair[0]


coordinates = np.array(coordinates)
coordinates = coordinates.ravel()
rawCoord = ','.join(map(str, coordinates))
print(rawCoord)
