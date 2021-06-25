from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton
import sys
import model as Model
 
class Window(QMainWindow):
    def generateButtons(self) :
        self.generateSummonerIDInfoButton()

    #Button that generates the summoner id json files
    def generateSummonerIDInfoButton (self) :
        self.gsiib = QPushButton('Generate', self)
        self.gsiib.setToolTip('Generate the ID Info for\nthe selected summoner.')
        self.gsiib.move(100,70)
        self.summonerNameField = QLineEdit(self)
        self.summonerNameField.move(20, 20)
        self.summonerNameField.resize(280,40)
        self.gsiib.clicked.connect(self.gsiibOnClick)
        
    def gsiibOnClick (self) :
        textboxValue = self.summonerNameField.text()
        Model.generateSummonerInfo(textboxValue)
        self.summonerNameField.setText("")

    def __init__(self) :
        super().__init__()

        self.setGeometry(300, 300, 1280, 720)
        self.setWindowTitle("PyQt5 window")
        self.generateButtons()
        self.show()
    

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())