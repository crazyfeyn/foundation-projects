from PyQt5.QtCore import Qt
from core import Core
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QLabel,
    QComboBox,
    QLineEdit,
    QMessageBox
)

class Main_window(QWidget):
    def __init__(self, data = None) -> None:
        super().__init__()

        data = Core().infos()
        self.just_flag = False
        if not data:
            self.just_flag = True
            
        self.data = data
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #fff685; padding: 4px")
        
        self.top_first = QHBoxLayout()
        self.top_second = QHBoxLayout()
        self.general_v = QVBoxLayout()
        self.left_side = QHBoxLayout()
        self.right_side = QHBoxLayout()
        self.left_right_holder = QHBoxLayout()
        self.cashes_holder = QHBoxLayout()
        self.three_list_holder = QHBoxLayout()
        self.tot_1_v = QVBoxLayout()
        self.tot_2_v = QVBoxLayout()
        self.tot_3_v = QVBoxLayout()
        self.tot_h = QHBoxLayout()
        self.accounts_combo = QComboBox()

        names = []
        if self.just_flag:
            self.accounts_combo.addItem("Cash Book    👇")
        else:
            self.accounts_combo.removeItem(0)
            for i in self.data:
                names.append(i[0])
            self.accounts_combo.addItems(names)
            names = []
            self.accounts_combo.setCurrentText(str(self.data[-1][0]))

        
        self.accounts_combo.addItem("Add Account")
        self.accounts_combo.activated[str].connect(self.add_btn_clicked)
    
        self.top_first.addWidget(self.accounts_combo)

        self.top_list_widget = QHBoxLayout()

        self.data_list = QListWidget()
        self.in_list = QListWidget()
        self.out_list = QListWidget()

        self.top_list_widget_left = QLabel("Data")
        self.top_list_widget_right_1 = QLabel("Cash In")
        self.top_list_widget_right_2 = QLabel("Cash Out")


        self.three_list_holder.addWidget(self.data_list)
        self.three_list_holder.addWidget(self.in_list)
        self.three_list_holder.addWidget(self.out_list)

        self.cash_in_btn = QPushButton("Cash In/Out")
        self.cash_in_btn.setCursor(Qt.PointingHandCursor)

        self.cashes_holder.addWidget(self.cash_in_btn)

        self.tot_1_txt = QLineEdit("Total Cash In")
        self.tot_1_txt.setReadOnly(True)
        self.tot_1_0 = QLineEdit("")
        self.tot_2_txt = QLineEdit("Total Cash Out")
        self.tot_2_txt.setReadOnly(True)
        self.tot_2_0 = QLineEdit("")
        self.tot_3_txt = QLineEdit("Total Balance")
        self.tot_3_txt.setReadOnly(True)
        self.tot_3_0 = QLineEdit("0")
        self.tot_3_0.setReadOnly(True)

        if Core().infos():
            self.tot_3_0.setText(str(self.data[-1][-1]))

        self.tot_1_v.addWidget(self.tot_1_txt)
        self.tot_1_v.addWidget(self.tot_1_0)
        self.tot_2_v.addWidget(self.tot_2_txt)
        self.tot_2_v.addWidget(self.tot_2_0)
        self.tot_3_v.addWidget(self.tot_3_txt)
        self.tot_3_v.addWidget(self.tot_3_0)
        self.tot_h.addLayout(self.tot_1_v)
        self.tot_h.addLayout(self.tot_2_v)
        self.tot_h.addLayout(self.tot_3_v)

        self.tot_1_txt.setStyleSheet("color: green; font-weight: bold; font-size: 15px")
        self.tot_1_0.setStyleSheet("color: green; font-weight: bold; font-size: 15px")
        self.tot_2_txt.setStyleSheet("color: red; font-weight: bold; font-size: 15px")
        self.tot_2_0.setStyleSheet("color: red; font-weight: bold; font-size: 15px")
        self.tot_3_txt.setStyleSheet("font-weight: bold; font-size: 15px")
        self.tot_3_0.setStyleSheet("font-weight: bold; font-size: 15px")

        self.cash_in_btn.clicked.connect(self.chash_in_btn_clicked)

        self.accounts_combo.setFixedWidth(370)
        self.accounts_combo.setStyleSheet("font-size: 19px; background-color: #fff685;")

        self.top_list_widget_left.setStyleSheet("font-size: 17px")
        self.top_list_widget_left.setFixedWidth(180)
        self.top_list_widget_right_1.setStyleSheet("font-size: 16px; color: green;")
        self.top_list_widget_right_2.setStyleSheet("font-size: 16px; color: red;")

        self.data_list.setFixedWidth(180)

        self.cash_in_btn.setFixedWidth(370)
        self.cash_in_btn.setStyleSheet("background-color: green; color: #fff; font-weight: bold; font-size: 16px; border-radius: 7px; padding: 8px")

        self.left_side.addWidget(self.top_list_widget_left)
        self.right_side.addWidget(self.top_list_widget_right_1)
        self.right_side.addWidget(self.top_list_widget_right_2)
        
        self.left_right_holder.addLayout(self.left_side)
        self.left_right_holder.addLayout(self.right_side)

        self.general_v.addLayout(self.top_first)
        self.general_v.addLayout(self.top_second)
        self.general_v.addLayout(self.left_right_holder)
        self.general_v.addLayout(self.three_list_holder)
        self.general_v.addLayout(self.cashes_holder)
        self.general_v.addLayout(self.tot_h)

        self.setLayout(self.general_v)
                



        self.show()
    
    def add_btn_clicked(self, text):
        if text == "Add Account":
            self.close()
            self.next_page = Add_Account()
        else:
            self.for_cash = Core().returnable_cashes(self.accounts_combo.currentText())
            self.data_list.clear()
            self.in_list.clear()
            self.out_list.clear()
            for i in self.for_cash:
                self.data_list.addItem(i[0].strftime("%Y-%m-%d %H:%M:%S"))
                self.in_list.addItem(str(i[1]))
                self.out_list.addItem(str(i[2]))

            for i in self.data:                
                if i[0] == self.accounts_combo.currentText():
                    data = Core().returnable(i[0])
                    self.tot_3_0.setText(str(data[0][4]))
        
    def chash_in_btn_clicked(self):

        if self.accounts_combo.currentText() == "Cash Book    👇":
            self.tot_1_0.clear()
            self.tot_2_0.clear()

        if (self.tot_1_0.text() or self.tot_2_0.text()) and self.accounts_combo.currentText() != "Cash Book    👇":

                if self.tot_1_0.text() and self.tot_2_0.text():
                    data = Core().modify(self.accounts_combo.currentText(), self.tot_1_0.text(), self.tot_2_0.text())
                    self.cashes = Core().create_cash_user(self.accounts_combo.currentText(), self.tot_1_0.text(), self.tot_2_0.text())
                    self.data_list.clear()
                    self.in_list.clear()
                    self.out_list.clear()

                elif self.tot_1_0.text():
                    data = Core().modify(self.accounts_combo.currentText(), self.tot_1_0.text(), 0)
                    self.cashes = Core().create_cash_user(self.accounts_combo.currentText(), self.tot_1_0.text(), 0)
                    self.data_list.clear()
                    self.in_list.clear()
                    self.out_list.clear()
                elif self.tot_2_0.text():
                    data = Core().modify(self.accounts_combo.currentText(), 0, self.tot_2_0.text())
                    self.cashes = Core().create_cash_user(self.accounts_combo.currentText(), 0, self.tot_2_0.text())
                    self.data_list.clear()
                    self.in_list.clear()
                    self.out_list.clear()

                self.tot_3_0.setText(str(data[0][0]))
                self.tot_1_0.clear()
                self.tot_2_0.clear()

                self.for_cash = Core().returnable_cashes(self.accounts_combo.currentText())
                for i in self.for_cash:
                    self.data_list.addItem(i[0].strftime("%Y-%m-%d %H:%M:%S"))
                    self.in_list.addItem(str(i[1]))
                    self.out_list.addItem(str(i[2]))
                
                if int(self.tot_3_0.text()) < 0:
                    self.tot_3_0.setStyleSheet("font-weight: bold; font-size: 15px; color: red")
                else:
                    self.tot_3_0.setStyleSheet("font-weight: bold; font-size: 15px;")


class Add_Account(QListWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #fff685; padding: 4px")

        self.hidable = QVBoxLayout()
        
        self.account_txt = QLineEdit("Name of account")
        self.account_txt.setReadOnly(True)
        self.account_txt1 = QLineEdit()
        self.account_txt1.setPlaceholderText("Account Name")
        self.account_sum = QLineEdit()
        self.account_sum.setPlaceholderText("Total money")
        
        self.account_add = QPushButton("Add account")
        self.back_btn = QPushButton("Back")
        self.account_add.setCursor(Qt.PointingHandCursor)
        self.back_btn.setCursor(Qt.PointingHandCursor)


        self.hidable.addWidget(self.account_txt)
        self.hidable.addWidget(self.account_txt1)
        self.hidable.addWidget(self.account_sum)
        self.hidable.addStretch()
        self.hidable.addWidget(self.account_add)
        self.hidable.addWidget(self.back_btn)

        self.account_txt1.setStyleSheet("font-size: 19px")
        self.account_txt1.setAlignment(Qt.AlignCenter)
        self.account_sum.setStyleSheet("font-size: 19px")
        self.account_sum.setAlignment(Qt.AlignCenter)
        self.account_txt.setStyleSheet("font-size: 19px; background-color: transparent; border: none")
        self.account_txt.setAlignment(Qt.AlignCenter)
        self.account_add.setFixedHeight(40)
        self.account_add.setStyleSheet("border: 10px; background-color: green; color: #fff; font-size: 17px")
        self.back_btn.setFixedHeight(40)
        self.back_btn.setStyleSheet("border: 10px; background-color: blue; color: #fff; font-size: 17px")

        self.setLayout(self.hidable)

        self.show()

        self.account_add.clicked.connect(self.account_add_clicked)
        self.back_btn.clicked.connect(self.back_btn_clicked)
    
    def back_btn_clicked(self):
        self.close()
        self.next_page = Main_window()
    def account_add_clicked(self):
        account_name = self.account_txt1.text()
        account_sum = self.account_sum.text()

        if account_name and account_sum:
            try:
                int(account_sum)
            except ValueError:
                QMessageBox.critical(self, "Error", "Total money must be a valid numeric value.")
                return
            
            data = Core().create_user(account_name, 0, 0, account_sum)
            self.next_page = Main_window(data)
            self.account_txt1.clear()
            self.account_sum.clear()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Please enter both account name and total money.")










app = QApplication([])
registration = Main_window()
app.exec_()