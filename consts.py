API_VERSIONS = {
    'summoner' : '4',
    'match' : '5'
}

REGIONS = {
    'north_america' : 'na1',
    'americas' : 'americas'
}

GAMES = {
    'league' : 'lol'
}

URL = {
    'base' : 'https://{region}.api.riotgames.com/lol/{url}',
    'summoner_by_name' : 'summoner/v{version}/summoners/by-name/{name}',
    'matches' : 'match/v{version}/matches/by-puuid/{puuid}/ids?start={start}&count={count}',
    'match' : 'match/v{version}/matches/{matchID}'
}