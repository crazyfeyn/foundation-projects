import mysql.connector

class Core_admin:
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
    CREATE TABLE IF NOT EXISTS admins (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(32) NOT NULL,
        password VARCHAR(32) NOT NULL  
    )
''')
    
    def create_user(self, username, password):
        self.cursor.execute(f'''
    INSERT INTO admins (username, password)
    VALUES ('{username}', '{password}')
''')
        self.cursor.execute('''DELETE u1 from users u1, users u2 where u1.username = u2.username and u1.id > u2.id''')
        self.connection.commit()

    def get_all_users(self):
        self.cursor.execute('''SELECT username, password from admins''')
        data = self.cursor.fetchall()
        return data
    


c1 = Core_admin()
# data = c1.get_all_users()
# for i in data:
#     print(i)