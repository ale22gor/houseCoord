import sys, json
import requests
import np


if len(sys.argv) == 3:
  x = sys.argv[1]
  y = sys.argv[2]
  query = x +' '+ y 
else:
  houseNumber = sys.argv[-1]
  forbidenList = ['+','/','-','*',',','.'] 
  
  if any( c in houseNumber for c in forbidenList):
      translation = houseNumber.maketrans({i:"" for i in ['к','К','k','K']})
      houseNumber = houseNumber.translate(translation)
      translation = houseNumber.maketrans({i:" k" for i in ['/']})
      houseNumber = houseNumber.translate(translation)

  query = ' '.join(list(filter(lambda x: len(x) > 3, sys.argv[1:-2])))
  translation = query.maketrans({i:"" for i in forbidenList})
  query = query.translate(translation)
  query = query + ' '+houseNumber

print(query)
print('https://nominatim.openstreetmap.org/search.php?q='+query+'&polygon_geojson=1&format=jsonv2')
r = requests.get('https://nominatim.openstreetmap.org/search.php?q='+query+'&polygon_geojson=1&format=jsonv2')
#print(r.content)


coordinates = r.json()[0]['geojson']['coordinates']
for pair in coordinates[0]:
    pair[0], pair[1] = pair[1], pair[0]


coordinates = np.array(coordinates)
coordinates = coordinates.ravel()
rawCoord = ','.join(map(str, coordinates))
print(rawCoord)
