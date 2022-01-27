import sys
import requests

from PIL import Image
from io import BytesIO

# Var 1
# map_request = "https://static-maps.yandex.ru/1.x/?ll=133.795%2C-25.695&spn=20.464,20.780&l=sat"
# response = requests.get(map_request)
#
# Image.open(BytesIO(response.content)).show()

# Var 2
api_server = "https://static-maps.yandex.ru/1.x/"

lon = "133.795"
lat = "-25.695"
delta = "20.464,20.780"
params = {"ll": ",".join([lon, lat]),
          "spn": delta,
          "l": "sat"}

response = requests.get(api_server, params=params)

Image.open(BytesIO(response.content)).show()
