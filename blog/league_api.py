#get api form a specific website
from distutils.log import info
import pip._vendor.requests as requests
import json
import time
data = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/COOKIEMONSTER123?api_key=RGAPI-8f052fa2-f185-4c70-87ea-cff6dbb47c49').json()
#print the json data
print(data)
#print the name of the summoner
puuid = data['puuid']
matches = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=100&api_key=RGAPI-8f052fa2-f185-4c70-87ea-cff6dbb47c49"
matches_1 = requests.get(matches).json()
print(matches_1)
dictionary = {}
for x in matches_1:
    print(x)
    match_data = f"https://americas.api.riotgames.com/lol/match/v5/matches/{x}?api_key=RGAPI-8f052fa2-f185-4c70-87ea-cff6dbb47c49"
    match_data_1 = requests.get(match_data).json()
    time.sleep(1.5)
    print(match_data_1['info']['gameDuration'])
    dictionary[x] = match_data_1
json_object = json.dumps(dictionary, indent=4)
with open("league_matches.json", "w") as outfile:
    outfile.write(json_object)