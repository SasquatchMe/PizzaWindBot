# from geopy.distance import geodesic
# import requests
# import json
#
#
# coords = requests.get('http://127.0.0.1:8000/geopos').json()
#
#
# l_l = []
# for coord in coords['geoposes']:
#     longitude = coord['longitude']
#     latitude = coord['latitude']
#     l_l.append((latitude, longitude))
#
#
# print(geodesic(l_l[2], l_l[3]))