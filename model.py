from api import RiotApi
import json
from PyQt5.QtWidgets import QLineEdit
import consts as Consts
import os
from os import path as Path

key = "RGAPI-6a4a9c2d-af22-4bef-a64d-e0db2375fa2a"
api = RiotApi(key, Consts.REGIONS['americas'])

# Get json output from api call and call method to save file
def generateSummonerInfo(name) :
    jsonOut = api.get_summoner_by_name(name)
    saveSummonerInfo(jsonOut, name)

# Save json output from getSummonerInfo api call in a json file.
def saveSummonerInfo(jsonOut, name) :
    file = open("summoners/" + name + ".json", 'x')
    file.write(json.dumps(jsonOut, indent = 2, sort_keys=True))
    file.close()

# Get match info based on summoner name and amount of matches,
# then call method to save the file.
def generateMatchInfo(name, count) :
    f = open("summoners/" + name + ".json", 'r')
    summonerData = json.loads(f.read())
    puuid = summonerData['puuid']
    jsonOut = api.getMatchList(puuid, 0, count)
    saveMatchInfo(jsonOut, name)

# Save json output from getMatchList api call in a json file.
def saveMatchInfo(jsonOut, name) : 
    for matchID in jsonOut :
        path = "matches/" + name + "-" + matchID + ".json" #Path for file
        # Remove file if it exists.
        if Path.exists(path) :
            os.remove(path)
        
        matchInfoFile = open(path, 'x')
        matchInfoFile.write(json.dumps(api.getMatchData(matchID), indent = 2, sort_keys=True))
        matchInfoFile.close()