import model as Model
# from ui import Window
from api import RiotApi
import csv

def main() :
    # Window()
    # name = input("Enter summoner name: ")
    # Model.generateMatchInfo(name, 1)
    
    # print(Model.getSummonerLevel("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getSummonerRank("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getIfHotstreak("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g"))
    
    # print(Model.getChampionMastery("JE2OA4NhplDQq3vd_BR_zkMj17LTP3R9K2yq2zphdSOxAHQxrxtkeX6TMDctzveiae3p48FOPhW_Rg", 223))
    
    # print(Model.getMatchList("jYHjDC1WFC_1YqNldzBESxEzERwh0wZq9gE58ccUHcAFKYmdS5BYSvHS_uLp8uIzMnLN6PxjrWIV8g", 10))
    
    row = Model.generateDataRow("NA1_3945315058")
    dataFile = open("data.csv", 'w')
    for entry in row :
        dataFile.write(entry + ", ")
    dataFile.write("\r\n")
    dataFile.close()


if __name__ == "__main__" :
    main()