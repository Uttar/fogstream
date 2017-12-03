'''
ТОП-5 чемпионатов. Вывести по каждому чемпионату первые пять команд с наибольшим колчиством голов
'''

import urllib.request
import json
import urllib.error

# Список самых клёвых чемпионатов
top_five_comp = ['PL', 'EC', 'EL', 'CL', 'WC']


def get_competitions(season='2017'):
    url = 'http://api.football-data.org/v1/competitions/?season=' + season
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req).read()
    js = json.loads(response.decode('utf-8'))
    return js


def get_league_table(href):
    url = href
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req).read()
    js = json.loads(response.decode('utf-8'))
    return js


competitions = get_competitions(season='2016')

c_five_comp = [c for c in competitions if c['league'] in top_five_comp]

for c in c_five_comp:
    print(c['caption'])
    try:
        league_table = get_league_table(c['_links']['leagueTable']['href'])
        all = []
        if league_table.get('standing') is not None:
            for group in range(len(league_table['standing'])):
                all.append(league_table['standing'][group])

        if league_table.get('_links') is not None:
            league_table.pop('_links')
        if league_table.get('standings') is not None:
            for group in league_table['standings']:
                for n in group:
                    for n in range(len(league_table['standings'][group])):
                        all.append(league_table['standings'][group][n])

        sorted_by_goals = sorted(all, key=lambda g: g['goals'])
        top_five_by_goals = sorted_by_goals[-5:]
        top_five_by_goals.reverse()
        if top_five_by_goals[0].get('teamName') is not None:
            for command in range(len(top_five_by_goals)):
                print('Команда: ' + top_five_by_goals[command]['teamName'] + ', колчество голов: ' + str(
                    top_five_by_goals[command]['goals']))
        else:
            for command in range(len(top_five_by_goals)):
                print('Команда: ' + top_five_by_goals[command]['team'] + ', колчество голов: ' + str(
                    top_five_by_goals[command]['goals']))
    except urllib.error.HTTPError:
        print('Сервер не отдаёт данные (' + c['_links']['leagueTable']['href'] + ')')


