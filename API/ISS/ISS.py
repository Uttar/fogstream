import urllib.request
import urllib.error
import json
import time


def get_iss():
    try:
        url = 'http://api.open-notify.org/iss-now.json'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req).read()
        js = json.loads(response.decode('utf-8'))
    except urllib.error.HTTPError or urllib.error.URLError:
        print('Что-то поломалось =(')
        return 'Что-то поломалось =('
    lat = js['iss_position']['latitude']
    lon = js['iss_position']['longitude']
    try:

        url = "http://maps.googleapis.com/maps/api/geocode/json?"
        url += "latlng=%s,%s&sensor=false" % (lat, lon)
        v = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        r = urllib.request.urlopen(v).read()
        j = json.loads(r.decode('utf-8'))
    except urllib.error.HTTPError or urllib.error.URLError:
        print('Координаты МКС: %s:%s' % (lat, lon))
        return lat, lon

    place = None
    if j['status'] == 'OK':
        try:
            place = j['results'][1]['formatted_address']
        except IndexError:
            return lat, lon

    print('Координаты МКС: %s:%s' % (lat, lon))
    if place:
        print(place)
        return lat, lon, place
    else:
        return lat, lon


# get_iss()

while True:
    with open('result.txt', 'a', encoding='utf-8', errors=None) as f:
        t = time.strftime("%d_%b_%Y_%H-%M ")
        text = t + str(get_iss()) + '\n'
        f.write(text)
        f.close()
        time.sleep(60)
