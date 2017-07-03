import time
import json
import sys
from riotwatcher import RiotWatcher, NORTH_AMERICA, EUROPE_WEST
from riotwatcher import LoLException, error_404, error_429

key = 'RGAPI-8a4e9fd9-ef04-4088-ad57-f9eb445bbb7b'

w = RiotWatcher(key)

def wait():
    while not w.can_make_request():
        time.sleep(1)

def game_tests(name, region):
    wait()
    summoner = w.get_summoner(name = name, region = region)
    try:
        x = w.get_recent_games(summoner['id'], region = region)
    except:
        return {'WinRate': 'N/A' ,'KDA':'N/A'}
    kills = 0
    deaths = 0
    assists = 0
    wins = 0

    try:
        for t in x['games']:
            deaths += t['stats']['numDeaths'] if 'numDeaths' in t['stats'] else 0
            assists += t['stats']['assists'] if 'assists' in t['stats'] else 0
            kills += t['stats']['championsKilled'] if 'championsKilled' in t['stats'] else 0
            if(t['stats']['win']):
                wins += 1
    except:
        return {'WinRate': 'N/A' ,'KDA':'N/A'}
    if deaths > 0:
        kda = (kills + assists) / (deaths * 1.00)
    else:
        kda = kills + assists
    wrate = wins/10.0
    return {'WinRate': wrate ,'KDA':"%.3f" % round(kda,3)}
