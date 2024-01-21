from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QKeySequence

from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QGridLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QShortcut
)

class Calculator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My Calculator")
        self.setStyleSheet("background-color: #000000;")
        self.setFixedSize(500,750)
        # self.showMaximized()

        self.v_box = QVBoxLayout()

        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("""
            color: #fff;
            font-size: 100px;
        """)
        self.v_box.addWidget(self.display)

        self.display_info = QLabel()
        self.display_info.setAlignment(Qt.AlignRight)
        self.display_info.setStyleSheet("""
            color: #fff;
            font-size: 25px;
        """)
        self.v_box.addWidget(self.display_info)

        self.shortcut = QShortcut(QKeySequence("Delete"), self)
        self.shortcut.activated.connect(self.clear_display)

        self.__initUI()
        self.setLayout(self.v_box)

    def __initUI(self):
        self.keyBoard = [
            ["AC", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["⌫", "0", ".", "="]
        ]
        self.equation = '0'
        self.buttonMap = dict()

        self.buttons = QGridLayout()
        for row, keys in enumerate(self.keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(100,100)
                if key in '/*-+=':
                    self.buttonMap[key].setStyleSheet('''
                        background-color: #ff9933;
                        color: #fff;
                        border-radius: 50px;
                        font-size: 50px;
                    ''')
                elif key in 'AC()':
                    self.buttonMap[key].setStyleSheet('''
                        background-color: #c0c0c0;
                        color: #101010;
                        border-radius: 50px;
                        font-size: 50px;
                    ''')
                else:
                    self.buttonMap[key].setStyleSheet('''
                        background-color: #303030;
                        color: #fff;
                        border-radius: 50px;
                        font-size: 50px;
                    ''')
                self.buttonMap[key].clicked.connect(self.__action)
                self.buttons.addWidget(self.buttonMap[key], row, col)

        self.v_box.addLayout(self.buttons)                

    def __action(self):
        sender = self.sender()
        text = sender.text()
        self.display_info.clear()
        self.addElement(text)


    def addElement(self, text):
        if text in '0123456789+-*/.()':
            if text == '.' and self.equation == '0':
                self.equation += text
            else:
                self.equation = text if self.equation == '0' else self.equation + text

        elif text == 'AC':
            self.equation = '0'  

        elif text == '⌫':

            self.equation = '0' if len(self.equation) == 1 else self.equation[:-1]
            
            # if len(self.equation) == 1:
            #     self.equation = '0'
            # else:
            #     self.equation = self.equation[:-1]
        elif text == '=':
            try:
                self.equation = str(eval(self.equation))
            except Exception as err:
                self.display_info.setText(str(err))
                self.equation = '0'

        self.display.setText(self.equation)

    def clear_display(self):
        self.equation = '0'
        self.display.setText(self.equation)

    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            text = event.text()
            self.addElement(text)
            


app = QApplication([])
calc = Calculator()
calc.show()
app.exec_()