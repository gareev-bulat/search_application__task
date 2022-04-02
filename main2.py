import sys
from io import BytesIO
import requests
from solution import select_params
from PIL import Image


toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass
json_response = response.json()
map_api_server = "http://static-maps.yandex.ru/1.x/"
map_params = select_params(json_response)
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(response.content)).show()









