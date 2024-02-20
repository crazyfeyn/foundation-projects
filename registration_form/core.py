import mysql.connector

class Core:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'login'
        )
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(32) NOT NULL,
        password VARCHAR(32) NOT NULL,
        name VARCHAR(32) NOT NULL,
        surname VARCHAR(32) NOT NULL,
        phone_number VARCHAR(32) NOT NULL,
        gender VARCHAR(32) NOT NULL,
        age INTEGER NOT NULL,
        education_field VARCHAR(32) NOT NULL,
        location VARCHAR(32) NOT NULL      
    )
''')
    
    def create_user(self, username, password, name, surname, phone_number, gender, age, education, location):
        self.cursor.execute(f'''
    INSERT INTO users (username, password, name, surname, phone_number, gender, age, education_field, location)
    VALUES ('{username}', '{password}', '{name}', '{surname}', '{phone_number}', '{gender}', '{age}', '{education}', '{location}')
''')
        self.cursor.execute('''DELETE u1 from users u1, users u2 where u1.username = u2.username and u1.id > u2.id''')
        self.connection.commit()
    

    def get_all_users(self):
        self.cursor.execute('''SELECT username, password, name, surname, phone_number, gender, age, education_field, location from users''')
        data = self.cursor.fetchall()
        return data
    
    def get_specific_user(self, username):
        self.cursor.execute(f'''SELECT username, password, name, surname, phone_number, gender, age, education_field, location from users where username = '{username}' ''')
        data = self.cursor.fetchall()
        return data

    def delete_password(self, username, password):
        self.cursor.execute(f'''
UPDATE users
SET password = "{username}"
WHERE username = "{password}" 
''')
        self.connection.commit()
    

# c1 = Core()