from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
)
from PyQt5.QtCore import Qt
# from random import randint
import random


class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("15 Puzzle")
        self.setFixedSize(500, 500)
        self.setStyleSheet("background-color: #57407c")

        self.moves_label = QVBoxLayout()
        self.top = QHBoxLayout()
        self.big = QVBoxLayout()
        

        self.new_button = QPushButton("New Game")
        self.new_button.setFixedSize(150, 40)
        self.new_button.setStyleSheet("font-size: 22px;border-radius: 8px;border: none; font-weight: bold; line-height: 60px; background-color: rgb(61, 41, 99);color: rgba(255, 255, 255, 0.5)")
        self.new_button.clicked.connect(self.__ui)

        self.moves_txt = QLabel("moves")
        self.moves_count = QLabel("0")
        self.moves_txt.setFixedSize(70, 30)
        self.moves_count.setFixedSize(70, 30)
        self.moves_txt.setStyleSheet("font-size: 12px; line-height: 12px; color: rgb(255, 255, 255); font-size: 19px")
        self.moves_count.setStyleSheet("font-size: 12px; line-height: 12px; color: rgb(255, 255, 255); font-size: 19px")
        self.moves_count.setAlignment(Qt.AlignCenter)
        self.moves_txt.setAlignment(Qt.AlignCenter)

        self.moves_label.addWidget(self.moves_txt)
        self.moves_label.addWidget(self.moves_count)
        self.top.addWidget(self.new_button)
        self.top.addLayout(self.moves_label)

        self.grid = QGridLayout()
        self.big.addLayout(self.top)
        self.big.addLayout(self.grid)
        self.__ui()
        self.setLayout(self.big)

    def __ui(self):
        self.allbuttons = []
        self.uniqe_numbers = set()
        self.space_number = [""]
        for i in range(1, 16):
            self.space_number.append(str(i))
        random.shuffle(self.space_number)
        number = 0
        
        for i in range(0,4):
            row = list()
            for j in range(0,4):
               self.button = QPushButton()
               self.button.setFixedSize(110, 100)
               self.button.setStyleSheet("background-color: rgb(73, 149, 145); color: #000; font-size: 30px; border-radius: 20px; border: 5px solid black")
               row.append(self.button)
               self.grid.addWidget(self.button, i, j)
               if number != 16:
                   self.button.setText(str(self.space_number[number]))
                   number+=1
               self.button.clicked.connect(self.__on_click)
            self.allbuttons.append(row)
        
        # if self.button.text() == "":
        #             self.button.setStyleSheet("background-color: rgb(61, 41, 99); color: #000; font-size: 30px; border-radius: 20px; border: 5px solid black")
        #        else:
        #            self.button.setStyleSheet("background-color: rgb(73, 149, 145); color: #000; font-size: 30px; border-radius: 20px; border: 5px solid black")
       
        self.count = 0
    def __on_click(self):
        button = self.sender()
        for i in range(len(self.allbuttons)):
            for j in range(len(self.allbuttons[i])):
                if button == self.allbuttons[i][j]:
                    a,b=i,j
        self.rebtn(a,b)
    def rebtn(self, a, b):
        self.sorted_numbers = []
        flag = False
        if 0 <= a < 4 and 0 <= b < 3 and self.allbuttons[a][b + 1].text() == "":
            self.allbuttons[a][b + 1].setText(str(self.allbuttons[a][b].text()))
            self.allbuttons[a][b].setText("")
            self.count+=1
            flag = True
        elif 0 <= a < 4 and 1 <= b < 4 and self.allbuttons[a][b - 1].text() == "":
            self.allbuttons[a][b - 1].setText(str(self.allbuttons[a][b].text()))
            self.allbuttons[a][b].setText("")
            self.count+=1
            flag = True
        elif 1 <= a < 4 and self.allbuttons[a - 1][b].text() == "":
            self.allbuttons[a - 1][b].setText(str(self.allbuttons[a][b].text()))
            self.allbuttons[a][b].setText("")
            self.count+=1
            flag = True
        elif 0 <= a < 3 and self.allbuttons[a + 1][b].text() == "":
            self.allbuttons[a + 1][b].setText(str(self.allbuttons[a][b].text()))
            self.allbuttons[a][b].setText("")
            self.count+=1
            flag = True
        self.moves_count.setText(str(self.count))
        
        if flag:
            for i in range(len(self.allbuttons)):
                for j in range(len(self.allbuttons[i])):
                    self.sorted_numbers.append(self.allbuttons[i][j].text())
            if self.sorted_numbers == sorted(self.sorted_numbers):
                self.new_button.setText("Winner")
            
            


app = QApplication([])
window = Main()
window.show()
app.exec_()