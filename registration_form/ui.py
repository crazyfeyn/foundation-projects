from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QLabel,
    QFormLayout,
    QSpinBox,
    QComboBox,
    QRadioButton,
    QLineEdit,
    QCheckBox
)
from core import Core
from core_admin import Core_admin
from core_employee import Core_employee



class Registration_Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #2E3192")

        self.v_box = QVBoxLayout()

        self.username_edit = QLineEdit("")
        self.username_edit.setPlaceholderText("username")
        self.password_edit = QLineEdit("")
        self.password_edit.setPlaceholderText("Password")
        self.login_btn = QPushButton("Log in")
        self.create_btn = QPushButton("Create new account")
        self.admin_btn = QPushButton("Admin in")

        self.v_box.addWidget(self.username_edit)
        self.v_box.addWidget(self.password_edit)
        self.v_box.addStretch()
        self.v_box.addWidget(self.login_btn)
        self.v_box.addWidget(self.create_btn)
        self.v_box.addWidget(self.admin_btn)

        self.password_edit.setEchoMode(QLineEdit.Password)
        self.username_edit.setStyleSheet("font-size: 20px; padding: 14px 16px; border: 1px solid black; border-radius: 6px; background-color: #fff; margin-bottom: 5px")
        self.username_edit.setFixedHeight(70)
        self.password_edit.setStyleSheet("font-size: 20px; padding: 14px 16px; border: 1px solid black; border-radius: 6px; background-color: #fff")
        self.password_edit.setFixedHeight(70)
        self.login_btn.setFixedHeight(70)
        self.login_btn.setStyleSheet("background-color: #1877f2; border-radius: 6px; font-size: 20px; line-height: 48px; padding: 0px 16px; border-color: #365899; color: #fff; font-weight: bold")
        self.login_btn.setCursor(Qt.PointingHandCursor)
        self.create_btn.setFixedHeight(70)
        self.create_btn.setStyleSheet("background-color: #42b72a; border-radius: 6px; font-size: 20px; line-height: 48px; padding: 0px 16px; border-color: #365899; color: #fff; font-weight: bold")
        self.create_btn.setCursor(Qt.PointingHandCursor)
        self.admin_btn.setStyleSheet("background-color: #1877f2; border-radius: 6px; font-size: 17px; padding: 10px; border-color: #365899; color: #fff;")
        self.admin_btn.setCursor(Qt.PointingHandCursor)

        self.setLayout(self.v_box)
        
        self.login_btn.clicked.connect(self.login_user)
        self.create_btn.clicked.connect(self.create_user)
        self.admin_btn.clicked.connect(self.admin_user)

        self.show()

    def login_user(self):
        data = Core().get_all_users()
        for username, password, name, surname, phone_number, gender, age, education_field, location in data:
            if self.username_edit.text() == username and self.password_edit.text() == password:
                self.next_page = Login_Window(username)
                self.close()
        else:
            self.login_btn.setText("Invalid login or password")

    def create_user(self):
        self.close()
        self.next_page = Create_Window()
    
    def admin_user(self):
        data = Core_admin().get_all_users()
        for username, password in data:
            if self.username_edit.text() == username and self.password_edit.text() == password:
                self.close()
                self.next_page = Admin_Window()
        else:
            self.admin_btn.setText("Invalid admin")
    
    

class Create_Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Create account-page")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #2E3192; font-size: 17px; color: #fff;")


        self.name = QLineEdit("")
        self.surname = QLineEdit("")
        self.age = QSpinBox()
        self.age.setMinimum(5)
        self.age.setMaximum(60)  
        self.gender_man = QRadioButton("Man")
        self.gender_woman = QRadioButton("Woman")
        self.location_combo = QComboBox()
        self.location_combo.addItems(["Asia", "Europe", "America"])
        self.phone_number = QLineEdit("")
        self.education_field = QLineEdit("")
        self.username = QLineEdit("")
        self.password = QLineEdit("")
        
        self.save_btn = QPushButton("Save to file")

        self.v_box = QVBoxLayout()
        layout = QFormLayout()
        layout.addRow("Name: ", self.name)
        layout.addRow("Surname: ", self.surname)
        layout.addRow("Phone number: ", self.phone_number)
        layout.addRow("Gender: ", self.gender_man)
        layout.addRow("", self.gender_woman)
        layout.addRow("Age: ", self.age)
        layout.addRow("Education-field: ", self.education_field)
        layout.addRow("Location: ", self.location_combo)
        layout.addRow("Username (choose): ", self.username)
        layout.addRow("Password: ", self.password)
        
        self.save_btn = QPushButton("Save")
        self.back_btn = QPushButton("Back")
        self.v_box.addLayout(layout)
        self.v_box.addStretch()
        self.v_box.addWidget(self.save_btn)
        self.v_box.addWidget(self.back_btn)

        self.setLayout(self.v_box)
        self.show()
        
        self.name.setStyleSheet("font-size: 17px; padding: 4px; border: 1px solid black; margin-bottom: 10px; border-top: hidden; border-left: hidden; border-right: hidden; background-color: transparent")
        self.name.setFixedHeight(40)
        self.surname.setStyleSheet("font-size: 17px; padding: 4px; border: 1px solid black; margin-bottom: 10px; border-top: hidden; border-left: hidden; border-right: hidden; background-color: transparent")
        self.surname.setFixedHeight(40)
        self.phone_number.setStyleSheet("font-size: 17px; padding: 4px; border: 1px solid black; margin-bottom: 10px; border-top: hidden; border-left: hidden; border-right: hidden; background-color: transparent")
        self.phone_number.setFixedHeight(40)
        self.age.setStyleSheet("font-size: 17px; padding: 4px; border: 1px solid black; margin-bottom: 10px; border-top: hidden; border-left: hidden; border-right: hidden; background-color: transparent")
        self.age.setFixedHeight(40)
        self.education_field.setStyleSheet("font-size: 17px; padding: 4px; border: 1px solid black; margin-bottom: 10px; border-top: hidden; border-left: hidden; border-right: hidden; background-color: transparent")
        self.education_field.setFixedHeight(40)
        self.username.setStyleSheet("font-size: 17px; padding: 4px; border: 1px solid black; margin-bottom: 10px; border-radius: 6px; background-color: transparent")
        self.username.setFixedHeight(40)
        self.password.setStyleSheet("font-size: 17px; padding: 4px; border: 1px solid black; background-color: #fff; margin-bottom: 10px; border-radius: 6px; background-color: transparent")
        self.password.setFixedHeight(40)
        self.location_combo.setStyleSheet("font-size: 17px; background-color: #2E3192; border-radius: 6px; margin-bottom: 10px")
        self.location_combo.setFixedHeight(40)
        self.save_btn.setStyleSheet("background-color: #42b72a; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 15px; border-color: #365899; color: #fff; font-weight: bold")
        self.save_btn.setCursor(Qt.PointingHandCursor)
        self.back_btn.setStyleSheet("background-color: blue; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 10px; border-color: #365899; color: #fff; font-weight: bold")
        self.back_btn.setCursor(Qt.PointingHandCursor)

        
        self.save_btn.clicked.connect(self.save_btn_clicked)
        self.back_btn.clicked.connect(self.back_btn_clicked)
    
    def save_btn_clicked(self):
        if self.name.text() and self.surname.text() and self.phone_number.text() and self.age.value() and self.education_field.text() and self.username.text() and self.password.text() and self.location_combo.currentText():
            gender = 'man' if self.gender_man.isChecked() else 'female'
            Core().create_user(
                self.username.text().lower(),
                self.password.text().lower(),
                self.name.text().lower(),
                self.surname.text().lower(),
                self.phone_number.text(),
                gender,
                self.age.value(),
                self.education_field.text().lower(),
                self.location_combo.currentText().lower()
            )
            self.name.clear()
            self.surname.clear()
            self.phone_number.clear()
            self.education_field.clear()
            self.username.clear()
            self.password.clear()
            self.gender_man.setChecked(False)
            self.gender_woman.setChecked(False)
    
    def back_btn_clicked(self):
        self.close()
        self.next_page = Registration_Window()

class Login_Window(QWidget):
    def __init__(self, username) -> None:
        self.username = username
        super().__init__()
        self.setWindowTitle("Log-In-page")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #2E3192; font-size: 17px; color: #fff;")


        self.big_list = QListWidget()

        self.data = Core().get_specific_user(self.username)
        for username, password, name, surname, phone_number, gender, age, education_field, location in self.data:
            text = f"""
Username: {username}
Password: {password}
Name: {name}
Surname: {surname}
Phone number: {phone_number}
Gender: {gender}
Age: {age}
Education-field: {education_field}
Location: {location}
"""
        self.v_box123=QVBoxLayout()
        self.big_list.addItem(text)
        self.v_box123.addWidget(self.big_list)
        self.setLayout(self.v_box123)
    
        self.show()

class Admin_Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Admin-In-page")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #2E3192; font-size: 17px; color: #fff;")
        self.show()

        self.big_box = QVBoxLayout()
        layout = QFormLayout()
        self.v_box = QVBoxLayout()
        self.four_language_h1 = QHBoxLayout()
        self.four_language_h2 = QHBoxLayout()
        self.four_language_h3 = QHBoxLayout()
        self.four_language_v = QVBoxLayout()
        self.take_vboxes_4 = QHBoxLayout()

        self.name_inp = QLineEdit("")
        self.surname_inp = QLineEdit("")
        self.programming_field = QLineEdit("")
        self.age = QSpinBox(self)
        self.gender_man = QRadioButton('man', self)
        self.gender_female = QRadioButton('female', self)
        self.add_btn = QPushButton("Add")
        self.back_btn = QPushButton("Back")
        self.show_employee_btn = QPushButton("Show Employees")


        self.checkBoxA = QCheckBox('C')
        self.checkBoxB = QCheckBox('C#')
        self.checkBoxC = QCheckBox('Python')
        self.checkBoxD = QCheckBox('JS')
        self.checkBoxE = QCheckBox('DART')
        self.checkBoxF = QCheckBox('Java')
        self.checkBoxG = QCheckBox('Ruby')
        self.checkBoxH = QCheckBox('Swift')
        self.checkBoxI = QCheckBox('Go')
        self.checkBoxJ = QCheckBox('Kotlin')
        self.checkBoxK = QCheckBox('Rust')
        self.checkBoxL = QCheckBox('Node JS')


        self.checkBoxes = [self.checkBoxA, self.checkBoxB, self.checkBoxC, self.checkBoxD, self.checkBoxE, self.checkBoxF, self.checkBoxG, self.checkBoxH, self.checkBoxI, self.checkBoxJ, self.checkBoxK, self.checkBoxL]


        self.four_language_h1.addWidget(self.checkBoxA)
        self.four_language_h1.addWidget(self.checkBoxB)
        self.four_language_h1.addWidget(self.checkBoxC)
        self.four_language_h1.addWidget(self.checkBoxD)

        self.four_language_h2.addWidget(self.checkBoxE)
        self.four_language_h2.addWidget(self.checkBoxF)
        self.four_language_h2.addWidget(self.checkBoxG)
        self.four_language_h2.addWidget(self.checkBoxH)

        self.four_language_h3.addWidget(self.checkBoxI)
        self.four_language_h3.addWidget(self.checkBoxJ)
        self.four_language_h3.addWidget(self.checkBoxK)
        self.four_language_h3.addWidget(self.checkBoxL)

        self.just_txt = QLabel("Major progaramming language(s)")

        self.four_language_v.addWidget(self.just_txt)
        self.four_language_v.addLayout(self.four_language_h1)
        self.four_language_v.addLayout(self.four_language_h2)
        self.four_language_v.addLayout(self.four_language_h3)

        self.salary = QLineEdit("")
        layout.addRow('Name:', self.name_inp)
        layout.addRow('Surname:', self.surname_inp)
        layout.addRow('Programming-fieled:', self.programming_field)
        layout.addRow('Age:', self.age)
        layout.addRow('Gender:', self.gender_man)
        layout.addRow('', self.gender_female)

        self.v_box.addLayout(layout)
        self.v_box.addLayout(self.four_language_v)
        self.v_box.addStretch()
        self.v_box.addWidget(self.add_btn)
        self.v_box.addWidget(self.back_btn)
        self.v_box.addWidget(self.show_employee_btn)


        self.add_btn.setStyleSheet("background-color: #42b72a; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 15px; border-color: #365899; color: #fff; font-weight: bold")
        self.add_btn.setCursor(Qt.PointingHandCursor)
        self.back_btn.setStyleSheet("background-color: blue; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 10px; border-color: #365899; color: #fff; font-weight: bold")
        self.back_btn.setCursor(Qt.PointingHandCursor)
        self.show_employee_btn.setStyleSheet("background-color: red; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 10px; border-color: #365899; color: #fff; font-weight: bold")
        self.show_employee_btn.setCursor(Qt.PointingHandCursor)

        self.add_btn.clicked.connect(self.add_btn_clicked)
        self.back_btn.clicked.connect(self.back_btn_clicked)
        self.show_employee_btn.clicked.connect(self.show_employee_btn_clicked)


        self.setLayout(self.v_box)
        
    def add_btn_clicked(self):
        if self.name_inp and self.surname_inp and self.programming_field and self.age.value() and (self.gender_man.isChecked() or self.gender_female.isChecked()) and self.checkBoxes:
            gender = 'man' if self.gender_man.isChecked() else 'female'
            for i in self.checkBoxes:
                if i.isChecked():
                    i.setChecked(False)
                    Core_employee().create_user(self.name_inp.text().lower(), self.surname_inp.text().lower(), self.programming_field.text().lower(), self.age.value(), gender, i.text().lower())
            self.name_inp.clear()
            self.surname_inp.clear()
            self.programming_field.clear()
            self.age.clear()
            self.gender_man.setChecked(False)
            self.gender_female.setChecked(False)

    def back_btn_clicked(self):
        self.close()
        self.next_page = Registration_Window()
    
    def show_employee_btn_clicked(self):
        self.close()
        self.next_page = Employee_Window(self.four_language_v)

class  Employee_Window(QWidget):
    def __init__(self, four_language_v = None) -> None:
        super().__init__()
        self.four_language_v = four_language_v
        self.setWindowTitle("Show-Employee-page")
        self.setStyleSheet("background-color: #2E3192; font-size: 17px; color: #fff;")
        self.setFixedSize(400, 500)
        self.show()

        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.sorted_combo_field = QComboBox()
        self.sorted_combo_field.addItems(['Frontend', '.Net', 'Flutter', 'Backend', 'Go', 'Fullstack'])
        self.sorted_combo_per = QComboBox()
        self.sorted_combo_per.addItems(['All', 'Age', 'Male', 'Female'])
        self.apply = QPushButton("Apply")
        self.edit = QPushButton("Edit")
        self.back = QPushButton("Back")

        self.apply.setStyleSheet("background-color: blue; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 10px; border-color: #365899; color: #fff; font-weight: bold")
        self.apply.setCursor(Qt.PointingHandCursor)
        self.edit.setStyleSheet("background-color: blue; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 10px; border-color: #365899; color: #fff; font-weight: bold")
        self.edit.setCursor(Qt.PointingHandCursor)
        self.back.setStyleSheet("background-color: red; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 10px; border-color: #365899; color: #fff; font-weight: bold")
        self.back.setCursor(Qt.PointingHandCursor)
        self.sorted_combo_field.setStyleSheet("padding: 10px; border: 1px solid black")
        self.sorted_combo_field.setCursor(Qt.PointingHandCursor)
        self.sorted_combo_per.setStyleSheet("padding: 10px; border: 1px solid black")
        self.sorted_combo_per.setCursor(Qt.PointingHandCursor)

        self.big_list = QListWidget()
        self.full_data = Core_employee().full_data()

        self.big_list.setStyleSheet("padding: 10px")

        self.void_text = "There is no one you can find"


        for name, surname, programming_field, age, gender, languages in self.full_data:
            self.text = f"""
Name: {name}
Surname: {surname}
Age: {age}
Programming-field: {programming_field}
Gender: {gender}
Major programming languages: 
{languages}
"""
            self.big_list.addItem(self.text)
        self.v_box.addWidget(self.big_list)


        self.h_box.addWidget(self.sorted_combo_field)
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.sorted_combo_per)
        self.v_box.addLayout(self.four_language_v)
        self.v_box.addWidget(self.apply)
        self.v_box.addWidget(self.edit)
        self.v_box.addWidget(self.back)
        
        self.setLayout(self.v_box)

        self.big_list.itemClicked.connect(self.on_item_clicked)

        self.back.clicked.connect(self.back_clicked)
        self.apply.clicked.connect(self.apply_clicked)
        self.edit.clicked.connect(self.edit_clicked)
        self.text_for_class = ''
    def on_item_clicked(self, item):
        self.text_for_class = item.text()
    
    def apply_clicked(self):

        self.extracted_field = self.sorted_combo_field.currentText().lower()
        if self.sorted_combo_per.currentText() == "Age":
            self.age_sort_clicked()
        elif self.sorted_combo_per.currentText() == "Male":
            self.male_clicked()
        elif self.sorted_combo_per.currentText() == "Female":
            self.female_clicked()
        elif self.sorted_combo_per.currentText() == "All":
            self.all_clicked()
    
    def edit_clicked(self):
        if self.text_for_class:
            self.close()
            self.next_page = Edit_Employee_Window(self.text_for_class)
    
    def back_clicked(self):
        self.close()
        self.next_page = Admin_Window()

    def age_sort_clicked(self):
        self.big_list.clear()
        data = Core_employee().full_data()
        sorted_data = sorted(data, key= lambda x: x[3])
        for name, surname, programming_field, age, gender, languages in sorted_data:
            if self.extracted_field == programming_field:
                self.void_text = ''
                text = f"""
Name: {name}
Surname: {surname}
Age: {age}
Programming-field: {programming_field}
Gender: {gender}
Major programming languages: 
{languages}
"""
                self.big_list.addItem(text)
        else:
            self.big_list.addItem(self.void_text)
    
    def male_clicked(self):
        self.big_list.clear()
        data = Core_employee().full_data()
        for name, surname, programming_field, age, gender, languages in data:
            if gender == 'man' and self.extracted_field == programming_field:
                self.void_text = ''
                text = f"""
Name: {name}
Surname: {surname}
Age: {age}
Programming-field: {programming_field}
Gender: {gender}
Major programming languages: 
{languages}
"""
                self.big_list.addItem(text)
        else:
            self.big_list.addItem(self.void_text)


    def female_clicked(self):
        self.big_list.clear()
        data = Core_employee().full_data()
        for name, surname, programming_field, age, gender, languages in data:
            if gender == 'female' and self.extracted_field == programming_field:
                self.void_text = ''
                text = f"""
Name: {name}
Surname: {surname}
Age: {age}
Programming-field: {programming_field}
Gender: {gender}
Major programming languages: 
{languages}
"""
                self.big_list.addItem(text)
        else:
            self.big_list.addItem(self.void_text)


    def all_clicked(self):
        self.big_list.clear()
        data = Core_employee().full_data()
        for name, surname, programming_field, age, gender, languages in data:
            if self.extracted_field == programming_field:
                self.void_text = ''
                text = f"""
Name: {name}
Surname: {surname}
Age: {age}
Programming-field: {programming_field}
Gender: {gender}
Major programming languages: 
{languages}
"""
                self.big_list.addItem(text)
        else:
            self.big_list.addItem(self.void_text)


class Edit_Employee_Window(QWidget):
    def __init__(self, text) -> None:
        super().__init__()
        self.text = text

        self.setFixedSize(400, 500)
        self.setWindowTitle("Edit-Eployee Window")
        self.setStyleSheet("background-color: #2E3192; font-size: 17px; color: #fff;")
        self.show()

        self.v_box = QVBoxLayout()

        self.text_edit = QListWidget()
        self.delete = QPushButton("Delete")
        self.pre_version = QPushButton("Pre version")
        self.save = QPushButton("Save")
        self.back = QPushButton("Back")


        self.text_edit.addItem(self.text)

        self.v_box.addWidget(self.text_edit)
        self.v_box.addWidget(self.delete)
        self.v_box.addWidget(self.pre_version)
        self.v_box.addWidget(self.save)
        self.v_box.addWidget(self.back)

        self.setLayout(self.v_box)

        self.delete.setCursor(Qt.PointingHandCursor)
        self.delete.setStyleSheet("background-color: blue; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 10px; border-color: #365899; color: #fff; font-weight: bold")
        self.pre_version.setCursor(Qt.PointingHandCursor)
        self.pre_version.setStyleSheet("background-color: blue; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 10px; border-color: #365899; color: #fff; font-weight: bold")
        self.save.setCursor(Qt.PointingHandCursor)
        self.save.setStyleSheet("background-color: #42b72a; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 10px; border-color: #365899; color: #fff; font-weight: bold")
        self.back.setCursor(Qt.PointingHandCursor)
        self.back.setStyleSheet("background-color: red; border-radius: 6px; font-size: 20px; line-height: 38px; padding: 10px; border-color: #365899; color: #fff; font-weight: bold")

        self.after_text = ''
        for i in range(1, len(self.text)-1):
            self.after_text+=self.text[i]

        self.after_text = self.after_text.split('\n')
        for i in range(len(self.after_text)):
            self.after_text[i] = self.after_text[i].split(" ")
            self.name = self.after_text[0][1]
            self.surname = self.after_text[1][1]
            if self.after_text[i] == self.after_text[2]:
                break

        self.delete.clicked.connect(self.delete_clicked)
        self.pre_version.clicked.connect(self.pre_version_clicked)
        self.save.clicked.connect(self.save_clicked)
        self.back.clicked.connect(self.back_clicked)


    def delete_clicked(self):
        self.text_edit.clear()
    def pre_version_clicked(self):
        self.text_edit.addItem(self.text)
    def save_clicked(self):
        Core_employee().delete_employee(self.name, self.surname)
        self.close()
        self.next_page = Employee_Window()
    def back_clicked(self):
        self.close()
        self.next_page = Employee_Window()



app = QApplication([])
registration = Registration_Window()
app.exec_()