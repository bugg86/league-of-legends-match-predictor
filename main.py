import model as Model
# from ui import Window
from api import RiotApi
import consts as Consts

def main() :
    # Window()
    name = input("Enter summoner name: ")
    Model.generateMatchInfo(name, 5)

if __name__ == "__main__" :
    main()