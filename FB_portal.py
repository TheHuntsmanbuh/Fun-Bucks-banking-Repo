import os
import sys
#pyqt6 imports fr

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt6.QtCore import (
    Qt,
    QSize,
)
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)

from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("fun-bucks portal")
        self.setWindowIcon(QIcon('fbicon.png'))
        self.acceptDrops()
        
        def getfbcount():
            global line
            file = open("fb_money.txt", "r") #gets initial value from wallet
            for line in file.readlines():
                line = (line)
        getfbcount()
        fbicon = QPixmap("fbicon.png")
        fbcount = QLabel(f"{line} <-- your funbucks balance")

        #labels
        welcome = QLabel()
        welcome.setText("welcome to the fun-bucks portal")
        #sublayouts
        funguess = QVBoxLayout()
        funmaths = QVBoxLayout()
        fungame = QVBoxLayout()
        funinfo = QVBoxLayout()
        #funguesscontent
        fginfo = QLabel("fun-guesser is a small minigame. you guess a number between 0 and 10000, guess right and earn funbucks!")
        funguess.addWidget(fginfo)
        fginfo.setWordWrap(True)
        funguesserbutton = QPushButton("play fun-guesser!")
        funguess.addWidget(funguesserbutton)
        #funmathscontent
        fminfo = QLabel("fun-maths is an educational game made to renforce maths skills by rewarding correct answers with small amounts of fun-bucks")
        funmaths.addWidget(fminfo)
        fminfo.setWordWrap(True)
        funmathsbutton = QPushButton("play fun-maths!")
        funmaths.addWidget(funmathsbutton)
        #fungamecontent
        fginfo = QLabel("fun-investor is the official investment app for the funbucks bank! invest in stocks and withdraw with no fees")
        fginfo.setWordWrap(True)
        fungame.addWidget(fginfo)
        fungamebutton = QPushButton("fun-investor")
        fungame.addWidget(fungamebutton)
        #funinfocontent
        funinfo.addWidget(fbcount)
        fiinfo = QLabel("fun-bucks is a currency in these suite of apps that can be earned by completing tasks and games. your money will persist through opening and closing the apps so dont be worried about losing progress")
        fiinfo.setWordWrap(True)
        funinfo.addWidget(fiinfo)
        findoutmorebutton = QPushButton("find out more!")
        funinfo.addWidget(findoutmorebutton)
        
        #mainlayout
        toprow = QHBoxLayout()
        toprow.addLayout(funguess)
        toprow.addLayout(funmaths)
        toprow.addLayout(fungame)
        toprow.addLayout(funinfo)
        #mainlayoutformatting
        funguess.setContentsMargins(0,0,0,0)
        funguess.setSpacing(20)


        #buttonlogic
        funguesserbutton.clicked.connect(self.initfunguess)
        funmathsbutton.clicked.connect(self.initfunmaths)
        findoutmorebutton.clicked.connect(self.initfuninfo)
        fungamebutton.clicked.connect(self.initfungames)


        
        widget = QWidget()
        widget.setLayout(toprow)
        self.setCentralWidget(widget)
    def initfungames(self):
        os.system(f"python FB_investor.py")
        print("opened fun-investor")
    def initfunguess(self):
        print("opened fun-guesser")
    def initfunmaths(self):
        os.system(f"python FB_maths.py")
        print("opened fun-maths")
    def initfuninfo(self):
        print("opened info")
   


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
