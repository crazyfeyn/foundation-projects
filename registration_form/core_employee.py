import mysql.connector

class Core_employee:
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
    CREATE TABLE IF NOT EXISTS employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(32) NOT NULL,
        surname VARCHAR(32) NOT NULL,
        programming_field VARCHAR(32) NOT NULL,
        age INTEGER NOT NULL,
        gender VARCHAR(32) NOT NULL,
        languages VARCHAR(32) NOT NULL
    )
''')
        
    
    def create_user(self, name, surname, programming_field, age, gender, new_lang):
        self.cursor.execute(f'''
    INSERT INTO employee (name, surname, programming_field, age, gender, languages)
    VALUES ('{name}', '{surname}', '{programming_field}', '{age}', '{gender}', '{new_lang}')
''')
        self.connection.commit()
        # self.cursor.execute('''DELETE u1 from users u1, users u2 where u1.username = u2.username and u1.id > u2.id''')
    
    def general(self):
        self.cursor.execute('''select name, surname, programming_field, age, gender, l1.id as 'languages' from employee e1 left join languages l1
        on e1.languages = l1.languages
''')
        data = self.cursor.fetchall()
        return data
    
    def full_data(self):
        self.cursor.execute('''
SELECT                       
  e1.name,
  e1.surname,
  MAX(e1.programming_field) AS programming_field,
  MAX(e1.age) AS age,
  MAX(e1.gender) AS gender,
  (
    SELECT GROUP_CONCAT(e2.languages)
    FROM employee e2
    WHERE e1.name = e2.name AND e1.surname = e2.surname
    GROUP BY e2.name, e2.surname
  ) AS languages
FROM
  employee e1
GROUP BY
  e1.name, e1.surname;
''')
        self.full_data = self.cursor.fetchall()
        return self.full_data
    
    def full_data_clone(self):
        self.cursor.execute('''
SELECT      
  e1.id,                 
  e1.name,
  e1.surname,
  MAX(e1.programming_field) AS programming_field,
  MAX(e1.age) AS age,
  MAX(e1.gender) AS gender,
  (
    SELECT GROUP_CONCAT(e2.languages)
    FROM employee e2
    WHERE e1.name = e2.name AND e1.surname = e2.surname
    GROUP BY e2.name, e2.surname
  ) AS languages
FROM
  employee e1
GROUP BY
  e1.name, e1.surname;
''')
        self.full_data = self.cursor.fetchall()
        return self.full_data
    
    def delete_employee(self, name, surname):
        self.cursor.execute(f'''delete from employee where name = '{name}' and surname = '{surname}'
''')
        self.connection.commit()


# c1 = Core_admin()
# data = c1.get_all_users()
# for i in data:
#     print(i)