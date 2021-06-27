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
    fileNumber = input("Enter file number: ")

    # print(puuid)

    # Model.generateMatchInfo(name, 1)
    
    # print(Model.getSummonerLevel("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getSummonerRank("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getIfHotstreak("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getChampionMastery("JE2OA4NhplDQq3vd_BR_zkMj17LTP3R9K2yq2zphdSOxAHQxrxtkeX6TMDctzveiae3p48FOPhW_Rg", 223))
    
    # print(Model.getMatchList("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g", 10))
    
    print("Generating match list...")
    matchList = Model.getMatchList(puuid, 15, count)
    print("Match list of " + str(count) + " matches generated.\n")

    rows = []
    for match in matchList :
        print("Generating match data for id : " + str(match) + "...")
        rows.append(Model.generateDataRow(match))
        print("Match " + str(len(rows)) + " data generated, waiting for " + str(waitTime) + " seconds to avoid going over api call limit.")
        time.sleep(waitTime)

    print("\nMatch data generated, writing data to csv file...")
    # rows.append(Model.generateDataRow("NA1_3945315058"))
    fields = ["puuid1", "sumLevel1", "sumRank1", "championID1", "champMastery1", "teamid1", "puuid2", "sumLevel2", "sumRank2", "championID2", "champMastery2", "teamid2", "puuid3", "sumLevel3", "sumRank3", "championID3", "champMastery3", "teamid3", "puuid4", "sumLevel4", "sumRank4", "championID4", "champMastery4", "teamid4", "puuid5", "sumLevel5", "sumRank5", "championID5", "champMastery5", "teamid5", "puuid6", "sumLevel6", "sumRank6", "championID6", "champMastery6", "teamid6", "puuid7", "sumLevel7", "sumRank7", "championID7", "champMastery7", "teamid7", "puuid8", "sumLevel8", "sumRank8", "championID8", "champMastery8", "teamid8", "puuid9", "sumLevel9", "sumRank9", "championID9", "champMastery9", "teamid9", "puuid10", "sumLevel10", "sumRank10", "championID10", "champMastery10", "teamid10", "winningTeam"]
    with open("data/data" + str(fileNumber) + ".csv", 'x') as data :
        write = csv.writer(data)
        write.writerow(fields)
        write.writerows(rows)
    data.close()

    print("\nGenerated data set of " + str(count) + " matches for " + str(name) + ".")


if __name__ == "__main__" :
    main()