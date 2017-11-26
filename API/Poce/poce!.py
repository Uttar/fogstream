'''
Получить номер покемона и выдать кракую информацию о нём
'''

import urllib.request
import urllib.error
import json
import re


def get_poke(poke_num=1):
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/' + str(poke_num)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req).read()
        js = json.loads(response.decode('utf-8'))
    except urllib.error.HTTPError:
        print('Нет такого покемона =(')
        exit()
    name = js['name']
    weight = js['weight']
    height = js['height']
    print('Имя - %(n)s, рост - %(h)s, вес - %(w)s' % {'n': name, 'h': height, 'w': weight})
    print('\nСкилы:')
    for slot in js['abilities']:
        url_ab = slot['ability']['url']
        req_ab = urllib.request.Request(url_ab, headers={'User-Agent': 'Mozilla/5.0'})
        response_ab = urllib.request.urlopen(req_ab).read()
        js_ab = json.loads(response_ab.decode('utf-8'))
        print(
            slot['ability']['name'] + ': \nshort effect - ' + js_ab['effect_entries'][0][
                'short_effect'] + '\neffect - ' +
            re.sub("^\s+|\n|\s+$", '', str(js_ab['effect_entries'][0]['effect'])))

    print("\nСтаты:")
    for stat in js['stats']:
        print(stat['stat']['name'] + ' = ' + str(stat['base_stat']))


get_poke(1)
