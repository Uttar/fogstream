'''
ТОП-5 чемпионатах. Вывести по каждому чемпионату первые пять команд с наибольшим колчиством голов
'''

import urllib.request
import json

def get_competitions(season = '2015'):
    url = 'http://api.football-data.org/v1/competitions/?season=' + season
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req).read()
    js = json.loads(response.decode('utf-8'))
    print(js)
    return js

competitions = get_competitions()

for c in competitions:
    print(c['league'])