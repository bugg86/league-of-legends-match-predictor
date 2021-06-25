from api import RiotApi
import json
from PyQt5.QtWidgets import QLineEdit
import consts as Consts
import os
from os import path as Path

key = "RGAPI-6a4a9c2d-af22-4bef-a64d-e0db2375fa2a"
api = RiotApi(key, Consts.REGIONS['north_america'])

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

# Return the summoner level.
def getSummonerLevel(puuid) :
    summonerInfo = api.getSummonerByPuuid(puuid)
    summonerLevel = summonerInfo['summonerLevel']
    return summonerLevel

# Return the summoner's rank
def getSummonerRank(puuid) :
    summonerInfo = api.getSummonerByPuuid(puuid)
    summonerID = summonerInfo['id']
    summonerLeagueInfo = api.getSummonerLeagueByID(summonerID)
    if summonerLeagueInfo == [] :
        return "EmptyBody"
    tier = summonerLeagueInfo[0]['tier']
    rank = summonerLeagueInfo[0]['rank']
    summonerTier = 0
    summonerRank = 0.0

    # Gives numerical value to each tier.
    if tier == "IRON" :
        summonerTier = 1
    elif tier == "BRONZE" :
        summonerTier = 2
    elif tier == "SILVER" :
        summonerTier = 3
    elif tier == "GOLD" :
        summonerTier = 4
    elif tier == "PLATINUM" :
        summonerTier = 5
    elif tier == "DIAMOND" :
        summonerTier = 6
    elif tier == "MASTER" :
        summonerTier = 7
    elif tier == "GRANDMASTER" :
        summonerTier = 8
    elif tier == "CHALLENGER" :
        return 9
    else :
        return 0.0

    # Gives numerical value to each rank.
    if rank == "I" :
        summonerRank = 0.1
    elif rank == "II" :
        summonerRank = 0.2
    elif rank == "III" :
        summonerRank = 0.3
    elif rank == "IV" :
        summonerRank = 0.4

    return (summonerTier + summonerRank)

# Returns if there was a hotstreak or not. 0 is no 1 is yes.
def getIfHotstreak(puuid) :
    summonerInfo = api.getSummonerByPuuid(puuid)
    summonerID = summonerInfo['id']
    summonerLeagueInfo = api.getSummonerLeagueByID(summonerID)
    if summonerLeagueInfo == [] :
        return "EmptyBody"
    
    if summonerLeagueInfo[0]['hotStreak'] :
        return 1
    else :
        return 0

def getChampionMastery(puuid, matchid) :
    summonerInfo = api.getSummonerByPuuid(puuid)
    summonerID = summonerInfo['id']
    
    matchData = api.getMatchData(matchid)