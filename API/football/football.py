'''
ТОП-5 чемпионатов. Вывести по каждому чемпионату первые пять команд с наибольшим колчиством голов
'''

import urllib.request
import json
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


competitions = get_competitions(season='2017')

c_five_comp = [c for c in competitions if c['league'] in top_five_comp]
# c_five_comp = filter(lambda c: c['league'] in top_five_comp, competitions)
# c_by_numberOfGames = sorted(competitions, key = lambda c: c['numberOfGames'])
for c in c_five_comp:
    print(c['_links']['leagueTable']['href'])
    league_table = get_league_table(c['_links']['leagueTable']['href'])
    if league_table.get('_links') is not None:
        league_table.pop('_links')
    all = []
    # print(league_table['standings'])
    for group in league_table['standings']:
        for n in group:
            for n in range(len(league_table['standings'][group])):
                all.append(league_table['standings'][group][n])
                # for team in league_table['standings'][group]:
                #     print(team['goals'])
    sorted_by_goals = sorted(all, key=lambda g: g['goals'])
    top_five_by_goals = sorted_by_goals[-5:]
    top_five_by_goals.reverse()
