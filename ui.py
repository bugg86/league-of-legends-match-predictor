from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton
import sys
import model as Model
 
class Window(QMainWindow):
    def generateButtons(self) :
        self.generateSummonerProfileButton()

    #Button that generates the summoner id json files
    def generateSummonerProfileButton (self) :
        self.gsp = QPushButton('Generate', self)
        self.gsp.setToolTip('Generate the ID Info for\nthe selected summoner.')
        self.gsp.move(100,70)
        self.gsp.clicked.connect(self.gspOnClick)
        
    def gspOnClick (self) :
        textboxValue = self.summonerNameField.text()
        Model.generateSummonerInfo(textboxValue)
        self.summonerNameField.setText("")

    def generateSummonerNameField(self) :
        self.summonerNameField = QLineEdit(self)
        self.summonerNameField.move(20, 20)
        self.summonerNameField.resize(280,40)

    def __init__(self) :
        super().__init__()

        self.setGeometry(300, 300, 1280, 720)
        self.setWindowTitle("PyQt5 window")
        self.generateSummonerNameField()
        self.generateButtons()
        self.show()
    

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())