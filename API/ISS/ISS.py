import urllib.request
import urllib.error
import json
import re

def get_iss():
    try:
        url = 'http://api.open-notify.org/iss-now.json'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req).read()
        js = json.loads(response.decode('utf-8'))
    except urllib.error.HTTPError:
        print('Нет такого покемона =(')
        exit()
    lat = js['iss_position']['longitude']
    lon = js['iss_position']['latitude']
    try:

        url = "http://maps.googleapis.com/maps/api/geocode/json?"
        url += "latlng=%s,%s&sensor=false" % (lat, lon)
        v = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        r = urllib.request.urlopen(v).read()
        j = json.loads(r.decode('utf-8'))
    except urllib.error.HTTPError:
        print('Координаты МКС: %s:%s' % (lat, lon))
        exit()

    components = j['results'][0]['address_components']
    country = town = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
        if "postal_town" in c['types']:
            town = c['long_name']
    print(town, country)
    return town, country


get_iss()