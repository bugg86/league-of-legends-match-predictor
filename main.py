import model as Model
from api import RiotApi
import csv
import time
import controller as Controller

def main() :
    
    # This section of code is for generating data for the dataset.
    # name = input("Enter summoner name: ")
    # puuid = Model.getSummonerPuuid(name)
    # count = input("Enter number of matches: ")
    # # fileNumber = input("Enter file number: ")
    # matchStart = input("Enter match start point: ")
    # Controller.generateNewData(name, puuid, matchStart, count)

    #This section of code is for getting live match data.
    name = input("Enter summoner name: ")
    Controller.generateLiveMatchData(name)

    # Model.generateSummonerInfo(name)

    # print(puuid)

    # Model.generateMatchInfo(name, 1)
    
    # print(Model.getSummonerLevel("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getSummonerRank("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getIfHotstreak("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getChampionMastery("JE2OA4NhplDQq3vd_BR_zkMj17LTP3R9K2yq2zphdSOxAHQxrxtkeX6TMDctzveiae3p48FOPhW_Rg", 223))
    
    # print(Model.getMatchList("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g", 10))


if __name__ == "__main__" :
    main()