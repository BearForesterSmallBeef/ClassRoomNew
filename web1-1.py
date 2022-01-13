import requests


name = input()

geocoder = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={name}&format=json"

response = requests.get(geocoder)
# print(response)
# print(response.content)

if response:
    #print(response.content)
    json_response = response.json()
    # print(json_response)
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_adress = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_cords = toponym["Point"]["pos"]
    print(toponym_adress)
    print(toponym_cords)
else:
    print("Произошла ошибка!")
    print(geocoder)
    print("Http статус:", response.status_code)
    print(response.status_code)