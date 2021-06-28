import model as Model
# from ui import Window
from api import RiotApi
import csv
import time

def main() :
    waitTime = 45

    # Window()
    name = input("Enter summoner name: ")
    puuid = Model.getSummonerPuuid(name)
    count = input("Enter number of matches: ")
    # fileNumber = input("Enter file number: ")
    matchStart = input("Enter match start point: ")

    # print(puuid)

    # Model.generateMatchInfo(name, 1)
    
    # print(Model.getSummonerLevel("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getSummonerRank("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getIfHotstreak("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getChampionMastery("JE2OA4NhplDQq3vd_BR_zkMj17LTP3R9K2yq2zphdSOxAHQxrxtkeX6TMDctzveiae3p48FOPhW_Rg", 223))
    
    # print(Model.getMatchList("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g", 10))
    
    print("Generating match list...")
    matchList = Model.getMatchList(puuid, matchStart, count)
    print("Match list of " + str(count) + " matches generated.\n")
    # fields = ["puuid1", "sumLevel1", "sumRank1", "championName1", "champMastery1", "role1", "teamid1", "puuid2", "sumLevel2", "sumRank2", "championName2", "champMastery2", "role2", "teamid2", "puuid3", "sumLevel3", "sumRank3", "championName3", "champMastery3", "role3", "teamid3", "puuid4", "sumLevel4", "sumRank4", "championName4", "champMastery4", "role4", "teamid4", "puuid5", "sumLevel5", "sumRank5", "championName5", "champMastery5", "role5", "teamid5", "puuid6", "sumLevel6", "sumRank6", "championName6", "champMastery6", "role6", "teamid6", "puuid7", "sumLevel7", "sumRank7", "championName7", "champMastery7", "role7", "teamid7", "puuid8", "sumLevel8", "sumRank8", "championName8", "champMastery8", "role8", "teamid8", "puuid9", "sumLevel9", "sumRank9", "championName9", "champMastery9", "role9", "teamid9", "puuid10", "sumLevel10", "sumRank10", "championName10", "champMastery10", "role10", "teamid10", "winningTeam"]
    # with open("data/data.csv", 'w') as data :
    #     write = csv.writer(data)
    #     write.writerow(fields)

    for match in matchList :
        print("Generating match data for id : " + str(match) + "...")
        row = []
        row.append(Model.generateDataRow(match))
        with open("data/data.csv", 'a') as data :
            write = csv.writer(data)
            write.writerows(row)
        print("Match " + str(len(row)) + " data generated, waiting for " + str(waitTime) + " seconds to avoid going over api call limit.")
        data.close()
        time.sleep(waitTime)

    print("\nMatch data generated, writing data to csv file...")
    # rows.append(Model.generateDataRow("NA1_3945315058"))
    fields = ["puuid1", "sumLevel1", "sumRank1", "championName1", "champMastery1", "role1", "teamid1", "puuid2", "sumLevel2", "sumRank2", "championName2", "champMastery2", "role2", "teamid2", "puuid3", "sumLevel3", "sumRank3", "championName3", "champMastery3", "role3", "teamid3", "puuid4", "sumLevel4", "sumRank4", "championName4", "champMastery4", "role4", "teamid4", "puuid5", "sumLevel5", "sumRank5", "championName5", "champMastery5", "role5", "teamid5", "puuid6", "sumLevel6", "sumRank6", "championName6", "champMastery6", "role6", "teamid6", "puuid7", "sumLevel7", "sumRank7", "championName7", "champMastery7", "role7", "teamid7", "puuid8", "sumLevel8", "sumRank8", "championName8", "champMastery8", "role8", "teamid8", "puuid9", "sumLevel9", "sumRank9", "championName9", "champMastery9", "role9", "teamid9", "puuid10", "sumLevel10", "sumRank10", "championName10", "champMastery10", "role10", "teamid10", "winningTeam"]
    

    print("\nGenerated data set of " + str(count) + " matches for " + str(name) + ".")


if __name__ == "__main__" :
    main()