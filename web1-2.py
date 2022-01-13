import requests
import os
import sys
import pygame


name = input()

geocoder = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={name}&format=json"

response = requests.get(geocoder)

json_response = response.json()

toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_adress = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
toponym_cords = toponym["Point"]["pos"]
print(toponym_cords)

map_requests = f"http://static-maps.yandex.ru/1.x/?ll={','.join(toponym_cords.split())}8&spn=0.04,0.04&l=map"
response = requests.get(map_requests)


if not response:
    print("Произошла ошибка!")
    print(map_requests)
    print("Http статус:", response.status_code)
    print(response.status_code)
    sys.exit(1)

map_file = "map.png"

with open(map_file, "wb") as file:
    file.write(response.content)


pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
