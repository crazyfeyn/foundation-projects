from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QHBoxLayout
)
from PyQt5 import QtCore

class Tasbeh(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.zirklar = ['SubhanAlloh', 'Alhamdulillah', 'Allohu Akbar']
        self.index = 0

        self.setWindowTitle("tasbeh")
        self.setFixedSize(250, 300)
        self.setStyleSheet("background-color: yellow; font-size: 20px")
        
        self.h_box = QHBoxLayout()

        self.v_box = QVBoxLayout()

        self.count_33_1 = QLineEdit('0')
        self.count_33_1.setAlignment(QtCore.Qt.AlignCenter)
        self.count_33_1.setStyleSheet("padding: 10px; border-radius: 15px; background-color: chocolate; border: 2px solid yellow")

        self.count_33_2 = QPushButton("light")
        self.count_33_2.setStyleSheet("padding: 10px; border-radius: 15px; background-color: chocolate; border: 2px solid yellow; font-size: 19px; color: red")

        self.count_33_3 = QPushButton('reset')
        self.count_33_3.setStyleSheet("padding: 10px; border-radius: 15px; background-color: chocolate; border: 2px solid yellow; font-size: 17px")


        self.label_zikr = QLabel(self.zirklar[0])
        self.label_zikr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_zikr.setStyleSheet("background-color: green; border-radius: 20px; color: #fff; font-size: bold; border: 2px solid red")

        self.edit_count = QLineEdit('0')
        self.edit_count.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_count.setFixedSize(230, 50)
        self.edit_count.setStyleSheet("padding: 10px; border-radius: 15px; background-color: chocolate; border: 2px solid yellow")
        
        self.btn = QPushButton('📿')
        self.btn.setFixedSize(230, 50)
        self.btn.setStyleSheet("background-color: #fff; border-radius: 20px; border: 2px solid red")


        self.h_box.addWidget(self.count_33_1)
        self.h_box.addWidget(self.count_33_2)
        self.h_box.addWidget(self.count_33_3)

        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.label_zikr)
        self.v_box.addWidget(self.edit_count)
        self.v_box.addWidget(self.btn)

        self.setLayout(self.v_box)

        self.btn.clicked.connect(self.on_click)
        self.count_33_2.clicked.connect(self.change_back)
        self.back_colors = ["red", "#fff", "yellow"]
        self.count_33_3.clicked.connect(self.change_power)


        

    def on_click(self):
        count = int(self.edit_count.text())
        count_for_33 = int(self.count_33_1.text())
        if count == 33:
            count_for_33+=1
            self.count_33_1.setText(str(count_for_33))
            count = 0
            self.index+=1
            if self.index == 3:
                self.index = 0
            self.label_zikr.setText(self.zirklar[self.index])
            
        self.edit_count.setText(str(count+1))

    index2 = 0
    def change_back(self):
        self.setStyleSheet(f"background-color: {self.back_colors[self.index2]}; font-size: 20px")
        self.index2+=1
        self.btn.setFixedSize(230, 50)
        if self.index2 == 3:
            self.index2 = 0
        self.count_33_2.setStyleSheet(f"padding: 10px; border-radius: 15px; background-color: chocolate; border: 2px solid yellow; font-size: 19px; color: {self.back_colors[self.index2]}")

    def change_power(self):
        self.count_33_1.setText("0")
        self.edit_count.setText("0")


    





app = QApplication([])
window = Tasbeh()
window.show()
app.exec_()