import sys, json
import requests
import np


if len(sys.argv) == 3:
  x = sys.argv[1]
  y = sys.argv[2]
  query = x +' '+ y 
else:
  houseNumber = sys.argv[-1]
  forbidenList = ['+','/','-','*'] 
  
  if any(not c.isalnum() for c in mystring):
    print('a1')
    if houseNumber[-1].isalpha():
      print('a')
      translation = houseNumber.maketrans({i:"" for i in forbidenList})
      houseNumber = houseNumber.translate(translation)
    else:
      print('b')
      translation = houseNumber.maketrans({i:"k" for i in forbidenList})
      houseNumber = houseNumber.translate(translation)

  query = ' '.join(list(filter(lambda x: len(x) > 5, sys.argv[1:])))
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
