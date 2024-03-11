import sqlite3


def create_database(name='users'):
    connection = sqlite3.connect('my_database')

    cursor = connection.cursor()
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {name} (
    id INTEGER PRIMARY KEY,
    address TEXT NOT NULL,
    name TEXT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def insert_database(address:str,name:str):
    connection = sqlite3.connect('my_database')

    cursor = connection.cursor()

    addresses = cursor.execute('''SELECT address FROM users''').fetchall()

    f = True
    for t in addresses:
        if address in t:
            f = False

    if f:
        cursor.execute('''INSERT INTO users (address, name) VALUES (?, ?)''',(address,name))
    connection.commit()
    connection.close()


def find_user(ip:str):
    connection = sqlite3.connect('my_database')

    cursor = connection.cursor()

    cursor.execute('SELECT name FROM users WHERE address = ?', (ip,))
    user =  cursor.fetchall()
    connection.close()
    return user

    

