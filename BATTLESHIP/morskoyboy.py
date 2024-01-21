from random import randint

from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QListWidget,
    QTextEdit,
)
from PyQt5.QtCore import Qt



class Main(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Morskoy Boy")
        self.setFixedSize(500, 500)
        self.setStyleSheet("background-color: #3498db")

        self.big_box = QVBoxLayout()
        self.top = QHBoxLayout()
        self.bottom = QHBoxLayout()
        self.top_bottom = QVBoxLayout()

        self.winner = QLabel("Winner")
        self.left_side = QLabel("Attempts: ")
        self.left_score = QLabel('25')

        self.right_side = QLabel("found: ")
        self.right_score = QLabel('0/10')
        self.left_side.setStyleSheet("font-size: 19px")
        self.left_score.setStyleSheet("border: 1px solid black; background-color: #fff; font-size: 19px")
        self.left_side.setFixedSize(80, 22)
        self.left_score.setFixedSize(60, 22)
        self.left_score.setAlignment(Qt.AlignCenter)

        self.right_side.setStyleSheet("font-size: 19px")
        self.right_score.setStyleSheet("border: 1px solid black; background-color: #fff; font-size: 19px")
        self.right_score.setAlignment(Qt.AlignCenter)
        self.right_side.setFixedSize(80, 22)
        self.right_score.setFixedSize(60, 22)

        self.top.addWidget(self.left_side)
        self.top.addWidget(self.left_score)
        self.bottom.addWidget(self.right_side)
        self.bottom.addWidget(self.right_score)
        self.top_bottom.addLayout(self.top)
        self.top_bottom.addLayout(self.bottom)
        self.winner.setAlignment(Qt.AlignCenter)
        self.winner.setStyleSheet("font-size: 20px")
        self.winner.setFixedHeight(40)
        

        self.grid = QGridLayout()
        self.position = set()
        self.__iu()
        self.big_box.addWidget(self.winner)
        self.big_box.addLayout(self.top_bottom)
        self.big_box.addLayout(self.grid)
        self.setLayout(self.big_box)

        

    def __iu(self):
        self.winner.hide()
        self.Allbuttons = []
        for i in range(0,7):
            for j in range(0,7):
               self.button = QPushButton("")
               self.button.setStyleSheet("background-color: #fff; border: 0.5px solid black")
               self.button.setFixedSize(70, 62)
               self.grid.addWidget(self.button, i, j)
               self.Allbuttons.append(self.button)
               self.button.clicked.connect(self.__on_click)
        while len(self.position) < 10:
            random_index = randint(0, 48)
            self.position.add(random_index)
        self.extracted_buttons = []
        for i in self.position:
            self.extracted_buttons.append(self.Allbuttons[i])
            self.Allbuttons[i].setStyleSheet("background-color: yellow")

        
        
    count_on_click = 0
    found = 0
    not_found = 0
    senders = []
    attempts_counter = 25

    def __on_click(self):
        self.winner.hide()
        self.setStyleSheet("background-color: #3498db")
        self.left_score.setText
        button = self.sender()

        if button not in self.senders:
            self.senders.append(button)   
            if button in self.extracted_buttons:
                button.setStyleSheet("background-color: green")
                self.found+=1
                self.right_score.setText(f"{self.found}/10")
            else:
                button.setStyleSheet("background-color: black")
                self.not_found+=1

            self.count_on_click+=1
            self.attempts_counter-=1
            if self.attempts_counter < 0:
                self.attempts_counter = 10
            self.left_score.setText(str(self.attempts_counter))

        if self.count_on_click == 25 and self.found != 10:
            for i in self.Allbuttons:
                i.setStyleSheet("background-color: #fff")
            self.left_score.setText("0")
            self.right_score.setText("0")
            self.found = 0
            self.not_found = 0
            self.attempts_counter = 25
            self.count_on_click = 0
            self.senders = []
            self.close()
            self.x = Over()
            self.x.show()
        
        if self.count_on_click <= 25 and self.found == 10:
            self.winner.show()
            self.left_score.setText("0")
            self.right_score.setText("0")
            self.found = 0
            self.not_found = 0
            self.attempts_counter = 25
            self.count_on_click = 0
            self.senders = []
            self.Allbuttons = []
            self.position.clear()
            self.close()
            self.x = winner()
            self.x.show()

class Over(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("looser")
        self.setFixedSize(500, 500)
        self.setStyleSheet("background-color: red")
        self.v_box = QVBoxLayout()
        self.over_txt = QLabel("Game is over, looser")
        self.over_txt.setAlignment(Qt.AlignCenter)
        self.over_txt.setStyleSheet("font-size: 30px; color: #fff")
        self.v_box.addWidget(self.over_txt)
        self.cont = QPushButton("New game")
        self.exit = QPushButton("Exit")
        self.v_box.addWidget(self.over_txt)
        self.v_box.addWidget(self.cont)
        self.v_box.addWidget(self.exit)
        self.cont.setStyleSheet("background-color: #fff; font-size: 20px;")
        self.exit.setStyleSheet("background-color: #fff; font-size: 20px;")
        self.cont.clicked.connect(self.new_game)
        self.exit.clicked.connect(self.exit_game)
        self.setLayout(self.v_box)
    def new_game(self):
        self.close()
        self.x = Main()
        self.x.show()
    def exit_game(self):
        self.close()
    
class winner(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("winner")
        self.setFixedSize(500, 500)
        self.setStyleSheet("background-color: green")
        self.v_box = QVBoxLayout()
        self.over_txt = QLabel("Game is over, winner")
        self.over_txt.setAlignment(Qt.AlignCenter)
        self.over_txt.setStyleSheet("font-size: 30px; color: #fff")
        self.cont = QPushButton("New game")
        self.exit = QPushButton("Exit")
        self.v_box.addWidget(self.over_txt)
        self.v_box.addWidget(self.cont)
        self.v_box.addWidget(self.exit)
        self.setLayout(self.v_box)
        self.cont.setStyleSheet("background-color: #fff; font-size: 20px;")
        self.exit.setStyleSheet("background-color: #fff; font-size: 20px;")
        self.cont.clicked.connect(self.new_game)
        self.exit.clicked.connect(self.exit_game)
    def new_game(self):
        self.close()
        self.x = Main()
        self.x.show()
    def exit_game(self):
        self.close()

app = QApplication([])
window = Main()
window.show()
app.exec_()