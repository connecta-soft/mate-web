import random
import requests
import string

from django.conf import settings
from django.utils.text import slugify


# get city coordinates by zip
def get_coordinates(city):
    coord_params = {
        "zip": city.zip,
        "key": "17o8dysaCDrgvlc"
    }

    coord_request = requests.get(
        'https://api.promaptools.com/service/us/zip-lat-lng/get/', params=coord_params).json()
    lat = coord_request.get("output", [{}])[0].get('latitude')
    lon = coord_request.get("output", [{}])[0].get("longitude")

    return f'{lat},{lon}'


# get distance
def get_distance(ship_to, ship_from):
    point_a = get_coordinates(ship_to)
    point_b = get_coordinates(ship_from)

    distance_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
    distance_params = {
        'origins': point_a,
        'destinations': point_b,
        'key': settings.GOOGLE_API_KEY
    }

    distance_request = requests.get(
        distance_url, params=distance_params)
    try:
        if 200 <= distance_request.status_code < 301: 
            distance_request = distance_request.json() 
            distance = distance_request.get('rows', [0])[0].get('elements', [0])[0].get('distance', {}).get("text") 
        else: 
            distance = 0
    except:
        distance = 0

    return distance


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, title, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, title, new_slug=new_slug)
    return slug
