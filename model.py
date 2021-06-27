from api import RiotApi
import json
from PyQt5.QtWidgets import QLineEdit
import consts as Consts
import os
from os import path as Path

key = "RGAPI-85c9e7dc-460d-4967-840b-055384278af1"
na1_api = RiotApi(key, Consts.REGIONS['north_america'])
americas_api = RiotApi(key, Consts.REGIONS['americas'])

# Get json output from api call and call method to save file
def generateSummonerInfo(name) :
    jsonOut = na1_api.get_summoner_by_name(name)
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
    jsonOut = americas_api.getMatchList(puuid, 0, count)
    saveMatchInfo(jsonOut, name)

# Save json output from getMatchList api call in a json file.
def saveMatchInfo(jsonOut, name) : 
    for matchID in jsonOut :
        path = "matches/" + name + "-" + matchID + ".json" #Path for file
        # Remove file if it exists.
        if Path.exists(path) :
            os.remove(path)
        
        matchInfoFile = open(path, 'x')
        matchInfoFile.write(json.dumps(americas_api.getMatchData(matchID), indent = 2, sort_keys=True))
        matchInfoFile.close()

# Return the summoner level.
def getSummonerLevel(puuid) :
    summonerInfo = na1_api.getSummonerByPuuid(puuid)
    summonerLevel = summonerInfo['summonerLevel']
    return summonerLevel

# Return the summoner's rank
def getSummonerRank(puuid) :
    summonerInfo = na1_api.getSummonerByPuuid(puuid)
    summonerID = summonerInfo['id']
    summonerLeagueInfo = na1_api.getSummonerLeagueByID(summonerID)
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
    summonerInfo = na1_api.getSummonerByPuuid(puuid)
    summonerID = summonerInfo['id']
    summonerLeagueInfo = na1_api.getSummonerLeagueByID(summonerID)
    if summonerLeagueInfo == [] :
        return "EmptyBody"
    
    if summonerLeagueInfo[0]['hotStreak'] :
        return 1
    else :
        return 0

# Returns the champion mastery for a given player and champion.
def getChampionMastery(puuid, championid) :
    summonerInfo = na1_api.getSummonerByPuuid(puuid)
    summonerID = summonerInfo['id']
    
    championMasteryInfo = na1_api.getChampionMasteryBySummonerID(summonerID, championid)
    champMastery = championMasteryInfo['championLevel']
    return champMastery

def generateDataRow(matchid) :
    matchInfo = americas_api.getMatchData(matchid) # gives me the match info as a dictionary.

    row = []
    for participant in matchInfo['info']['participants'] :
        puuid = participant['puuid']
        row.append(puuid)

        summLevel = getSummonerLevel(puuid)
        row.append(summLevel)

        summRank = getSummonerRank(puuid)
        row.append(summRank)

        hotstreak = getIfHotstreak(puuid)
        row.append(hotstreak)

        champion = participant['championId']
        row.append(champion)

        champMastery = getChampionMastery(puuid, champion)
        row.append(champMastery)

        teamid = participant['teamId']
        row.append(teamid)

    winningTeam = 0
    if matchInfo['info']['teams'][0]['win'] :
        winningTeam = 0
    else :
        winningTeam = 1
    row.append(winningTeam)
    return row

def getMatchList(puuid, count) :
    matchList = americas_api.getMatchList(puuid, 0, count)
    return matchList