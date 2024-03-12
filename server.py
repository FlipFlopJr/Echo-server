import socket
import sqlite3
from database_functions import *


def find_available_port(startPort, attempts = 100):
    #Функция по поиску свободного порта
    for port in range(startPort, startPort+attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((socket.gethostname(), port))
            return port
        except:
            continue


server = socket.socket()            # создаем объект сокета сервера
hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = find_available_port(12345)   # устанавливаем порт сервера
print(port)

#Создаем базу данных пользователей
create_database()

server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту

server.listen(5)

while True:
    
    con, addr = server.accept()
    address = addr[0]

    
    while True: 
        #Идентификация пользователя по ip: Если пользователь есть в бд, то приветствуем его, если нет - отправляем ему запрос на ввод имени пользователя
        user = find_user(address) #Проверяем есть ли пользователь в бд
        if not user: #Если его нет, отсылаем команду log с просьбой написать свое имя
            con.send('log'.encode())

            username, password = con.recv(1024).decode().split()
            insert_database(address,username,password)
        else:
            while True:
                con.send('check_passwd'.encode())
                password = con.recv(1024).decode()
                if check_passwd(address,password):
                    con.send(f'Hello, {user[0][0]}'.encode()) #Если же пользователь все-таки есть в бд, то отправляем ему привет
                    break
                else:
                    pass
            break
        

    file = open(f"logfile_{address}","w")
    file.write("Server starts\n")
    file.write("Server started listening\n")

    file.write("Client connected\n")


    try:
        while True:
            data = con.recv(1024).decode()

            if data == 'exit':
                con.close()
                file.write(f"Connection with {address} closed\n")
                file.close()
                break
            if 'name_' in data:
                insert_database(address,data.split('_')[1])
            else:
                file.write(f"Recieved data: {data}\n")
                file.write("Send data back\n")
                con.send(data.encode())
    except:
        pass