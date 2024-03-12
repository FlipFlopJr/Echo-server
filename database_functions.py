import sqlite3


def create_database(name='users'):
    connection = sqlite3.connect('my_database')

    cursor = connection.cursor()
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {name} (
    id INTEGER PRIMARY KEY,
    address TEXT NOT NULL,
    name TEXT NOT NULL,
    password TEXT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def insert_database(address:str,name:str, password:str):
    connection = sqlite3.connect('my_database')

    # password = hash(password) #Хэширую пароль

    cursor = connection.cursor()

    addresses = cursor.execute('''SELECT address FROM users''').fetchall()

    f = True #Проверка на то существует ли адрес в бд
    for t in addresses:
        if address in t:
            f = False

    
    if f:
        cursor.execute('''INSERT INTO users (address, name, password) VALUES (?, ?, ?)''',(address,name, password))
    connection.commit()
    connection.close()

def check_passwd(address:str, password:str):
    connection = sqlite3.connect('my_database')
    # password = hash(password) # Хэширую пароль
    print(f'Input {password}')
    cursor = connection.cursor()

    addresses = cursor.execute('''SELECT address, password FROM users''').fetchall()
    for t in addresses:
        if address == t[0]:
            print(f'Database {t[1]}')
            if password == t[1]:
                return True
            else:
                return False


def find_user(ip:str):
    connection = sqlite3.connect('my_database')

    cursor = connection.cursor()

    cursor.execute('SELECT name FROM users WHERE address = ?', (ip,))
    user =  cursor.fetchall()
    connection.close()
    return user


# create_database()
# insert_database('197.23.45.6','andrey','qwerty')
# print(find_user('197.23.45.6'))
# print(check_passwd('197.23.45.7','qwert'))

    

