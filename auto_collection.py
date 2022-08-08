import os
import json
from codecs import ignore_errors

cities_path = 'cities/'
cities = os.listdir(cities_path)


def get_file_data(path: str):
    with open(path, 'r') as f:
        data = json.load(f)
        return data


def create_collection(city: str, service: str, places_data):
    with open(f'database/{city}/{service}.json', 'w') as f:
        json.dump({
            'city': city,
            'service': service,
            'places': places_data
        }, f)


for city in cities:
    city_path = cities_path + city + '/'
    services = os.listdir(city_path)
    for service in services:
        places_data = []

        service_path = city_path + service + '/'
        places = os.listdir(service_path)
        for place in places:
            place_path = service_path + place
            places_data.append(get_file_data(place_path))

        if not os.path.exists(f'database/{city}'):
            os.mkdir(f'database/{city}')

        create_collection(city, service, places_data)
