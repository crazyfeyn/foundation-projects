import mysql.connector

class Core_languages:
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
    CREATE TABLE IF NOT EXISTS languages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(32) NOT NULL,
    )
''')
        
    
    def add_language(self, languages: list):
        self.cursor.execute(f'''
    INSERT INTO languages (languages)
    VALUES
()
''')
        self.connection.commit()

    def get_all_users(self):
        self.cursor.execute('''name, surname, programming_field, age, gender from employee''')
        data = self.cursor.fetchall()
        return data
    


# self.cursor.execute('''DELETE u1 from users u1, users u2 where u1.username = u2.username and u1.id > u2.id''')