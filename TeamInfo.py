import sys
import json
import TwitterApi as ta
import tests as t

# reads info from a json file
def get_data_from_file():
    with open('teams.json') as team_info:
        data = json.load(team_info)

    return data

# returns teams from region
def get_teams_from_region(region):
    teams_and_logos = {}
    data = get_data_from_file() 
    for teams in data['games'][region]['teams']:
        teams_and_logos[teams['name']] = teams['logo'] 

    return teams_and_logos

# returns name and logo of players from a team
def get_players_from_team(team_name, region):
    players = {}
    data = get_data_from_file()
    for team in data['games'][region]['teams']:
        if team['name'].lower() == team_name.lower():
            team_members = team['members']
            break
    for position in team_members:
        players[team_members[position]['nick']] = team_members[position]['avatar']

    return players

def calculate_odds(team_name1, region1, team_name2, region2):
    odds = {}
    results_team1 = get_info_from_team(team_name1, region1)
    results_team2 = get_info_from_team(team_name2, region2)
    emotion1 = get_tweets_from_team(team_name1, region1)
    emotion2 = get_tweets_from_team(team_name2, region2)
    rank_team1 = get_rank_team(team_name1, region1)
    rank_team2 = get_rank_team(team_name2, region2)
    counter_available_results = 0
    winrate_team1 = 0
    kda_team1 = 0
    winrate_team2 = 0
    kda_team2 = 0

    for player in results_team1:
        if results_team1[player]['WinRate'] != 'N/A' and results_team1[player]['KDA'] != 'N/A':
            winrate_team1 += float(results_team1[player]['WinRate'])
            kda_team1 += float(results_team1[player]['KDA'])
            counter_available_results += 1
    winrate_team1 = winrate_team1/counter_available_results
    kda_team1 = kda_team1/counter_available_results

    counter_available_results = 0

    for player in results_team2:
        if results_team2[player]['WinRate'] != 'N/A' and results_team2[player]['KDA'] != 'N/A':
            winrate_team2 += float(results_team2[player]['WinRate'])
            kda_team2 += float(results_team2[player]['KDA'])
            counter_available_results += 1
    winrate_team2 = winrate_team2/counter_available_results
    kda_team2 = kda_team2/counter_available_results

    total_team1 = (((0.3 * float(winrate_team1)) + (0.2 * float(kda_team1)) + (float(emotion1) * 0.5)) * float(rank_team1))
    total_team2 = (((0.3 * float(winrate_team2)) + (0.2 * float(kda_team2)) + (float(emotion2) * 0.5)) * float(rank_team2))
    total_rank_sum = total_team1 + total_team2 

    prob_team1 = total_team1/total_rank_sum
    prob_team2 = total_team2/total_rank_sum
    odds.update({team_name1:prob_team1})
    odds.update({team_name2:prob_team2})

    print odds



def get_rank_team(team_name, region):
    data = get_data_from_file()
    for team in data['games'][region]['teams']:
        if team['name'] == team_name:
            return team['ranking'] 

# returns logo, name, kda, winrate from players of a team
def get_info_from_team(team_name, region):
    nicks_team = get_team_nicks(team_name, region)
    data = {}
    players = get_players_from_team(team_name, region)
    for player in nicks_team:
        data[player] = t.game_tests(player, region)
        data[player].update({'logo': players[player]})
    return data
        
# returns emotions from players of a team
def get_tweets_from_team(team_name, region):
    team_members_twitter = get_teams_members_twitter(team_name, region)
    emotions_from_team = {}
    for player in team_members_twitter:
        emotions_from_team.update(ta.get_player_emotion(player, team_members_twitter[player]))
    emotion_counter = 0
    number_members = 0
    sum = 0
    total = 0
    for t in emotions_from_team:
        for t in emotions_from_team[t]:
            sum += (float(t['pos']) - float(t['neg'])) 
            emotion_counter += 1 
        if emotion_counter > 0:
            total += sum/emotion_counter
            number_members += 1
        sum = 0
        emotion_counter = 0
    return total/number_members
       


# returns name and twitter from players of a team
def get_teams_members_twitter(team_name, region):
    players_twitter = {}
    data = get_data_from_file()
    for team in data['games'][region]['teams']:
        if team['name'].lower() == team_name.lower():
            team_members = team['members']
            break
    for position in team_members:
        players_twitter[team_members[position]['nick']] = team_members[position]['twitter']

    return players_twitter

# returns members of a team
def get_team_nicks(team_name, region):
    players_nick = []
    data = get_data_from_file()
    for team in data['games'][region]['teams']:
        if team['name'].lower() == team_name.lower():
            team_members = team['members']
            break
    for position in team_members:
        players_nick.append(team_members[position]['nick'])

    return  players_nick 

if __name__ == '__main__':
    calculate_odds('Misfits', 'euw', 'Unicorns Of Love', 'euw') 
