import requests
import consts as Consts

key = "RGAPI-77d4bfe4-324a-4a77-a297-0fe3c6dbd587"
url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/JE2OA4NhplDQq3vd_BR_zkMj17LTP3R9K2yq2zphdSOxAHQxrxtkeX6TMDctzveiae3p48FOPhW_Rg/ids?start=0&count=20&api_key=RGAPI-e85582a7-c31e-4f4f-9078-872081eaef6c"

class RiotApi(object) :
    def __init__(self, api_key, region) :
        self.api_key = api_key
        self.region=region

    def request(self, api_url, params={}) :
        args = {'api_key' : self.api_key}
        for key, value in params.items() :
            if key not in args :
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                region=self.region,
                url=api_url
            ), 
            params = args
        )
        # print (response.url)
        return response.json()

    # Make api call to look up summoner profile info by summoner name.
    def get_summoner_by_name(self, name) :
        api_url = Consts.URL['summoner_by_name'].format(
            version = Consts.API_VERSIONS['summoner'],
            name=name
        )
        return self.request(api_url)
    
    # Make api call to get list of match IDs starting from the most recent match.
    def getMatchList(self, puuid, start, count) :
        api_url = Consts.URL['matches'].format(
            version=Consts.API_VERSIONS['match'],
            puuid=puuid,
            start=start,
            count=count
        )
        return self.request(api_url)
    
    # Make api call to get match information for a single match using the match ID.
    def getMatchData(self, matchID) :
        api_url = Consts.URL['match'].format(
            version = Consts.API_VERSIONS['match'],
            matchID = matchID
        )
        return self.request(api_url)

    def getSummonerByPuuid (self, puuid) :
        api_url = Consts.URL['summoner_by_puuid'].format(
            version = Consts.API_VERSIONS['summoner'],
            puuid=puuid
        )
        return self.request(api_url)

    def getSummonerLeagueByID (self, summonerID) :
        api_url = Consts.URL['league_by_summoner_id'].format(
            version = Consts.API_VERSIONS['league'],
            summonerID = summonerID
        )
        return self.request(api_url)

    def getChampionMasteryBySummonerID (self, summonerID, championID) :
        api_url = Consts.URL['champion_mastery_by_summoner_id'].format(
            version = Consts.API_VERSIONS['champion-mastery'],
            summonerID = summonerID,
            championID = championID
        )
        return self.request(api_url)

    def getLiveMatchData (self, summonerID) :
        api_url = Consts.URL['spectator_by_summoner_id'].format(
            version = Consts.API_VERSIONS['spectator'],
            summonerID = summonerID
        )
        return self.request(api_url)
    
    def getSummonerByID (self, summonerID) :
        api_url = Consts.URL['summoner_by_id'].format(
            version = Consts.API_VERSIONS['summoner'],
            summonerID = summonerID
        )