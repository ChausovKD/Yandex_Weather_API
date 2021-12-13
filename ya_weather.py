import requests
import json


def get_weather_by_lat_lon(lat, lon):
    headers = {
        'X-Yandex-API-Key': "585de221-e8d5-4950-a9a2-5870a4d45d70",
    }

    params = (
        ('lat', lat),
        ('lon', lon),
        ('lang', 'ru_RU'),
    )

    response = requests.get('https://api.weather.yandex.ru/v2/forecast/', params=params, headers=headers)
    json_data = response.json()
    return json_data


with open('dataset.json', "w+") as file:
    json.dump(get_weather_by_lat_lon('55.333146', '37.224384'), file)

with open('dataset.json', 'r') as file:
    temp = json.load(file)
    print(temp)