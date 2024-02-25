import mysql.connector
from datetime import datetime

class Core:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'expanse'
        )
        self.cursor = self.connection.cursor()
        self.create_table()
        self.create_cash_table()
    
    def create_table(self):
        self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        account_name VARCHAR(32) NOT NULL,
        date DATE NOT NULL,
        income INT NOT NULL,
        outcome INT NOT NULL,
        total INT NOT NULL
    )
''')
        self.connection.commit()
    
    def create_user(self, account_name, income, outcome, total):
        self.cursor.execute(f'''
    INSERT INTO accounts (account_name, date, income, outcome, total)
    VALUES ('{account_name}', '{datetime.now()}', '{income}', '{outcome}', '{total}')
''')
        self.connection.commit()
        self.cursor.execute('''select account_name, date, income, outcome, total from accounts
''')
        data = self.cursor.fetchall()
        return data
    
    def infos(self):
        self.cursor.execute('''select account_name, date, income, outcome, total from accounts
''')
        data = self.cursor.fetchall()
        return data
    
    def modify(self, name, in_sum, out_sum):
        self.cursor.execute(f'''
            UPDATE accounts 
            SET income = {int(in_sum)}, outcome = {int(out_sum)}, total = total + income - outcome
            WHERE account_name = '{name}'
''')
        self.connection.commit()
        
        self.cursor.execute(f'''
            SELECT total from accounts
            WHERE account_name = '{name}'
''')
        data = self.cursor.fetchall()
        return data
    

    def returnable(self, name):
        self.cursor.execute(f'''select account_name, date, income, outcome, total from accounts where account_name = '{name}'
''')
        data = self.cursor.fetchall()
        return data
    
    def for_total(self, name):
        self.cursor.execute(f'''select total from accounts where account_name = '{name}'
''')
        data = self.cursor.fetchall()
        return data
    


    def create_cash_table(self):
        self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS cash_accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        account_name VARCHAR(32) NOT NULL,
        date DATE NOT NULL,
        income INT NOT NULL,
        outcome INT NOT NULL
    )
''')
        self.connection.commit()
    
    def create_cash_user(self, account_name, income, outcome):
        self.cursor.execute(f'''
    INSERT INTO cash_accounts (account_name, date, income, outcome)
    VALUES ('{account_name}', '{datetime.now()}', '{income}', '{outcome}')
''')
        self.connection.commit()
        self.cursor.execute('''select account_name, date, income, outcome from cash_accounts
''')
        data = self.cursor.fetchall()
        return data
    
    def returnable_cashes(self, name):
        self.cursor.execute(f'''select date, income, outcome from cash_accounts where account_name = '{name}'
''')
        data = self.cursor.fetchall()
        return data