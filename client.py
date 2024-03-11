# Создать простой TCP-сервер, который принимает от клиента строку (порциями по 1 КБ) и возвращает ее. (Эхо-сервер).
import socket
import getpass
import sys

client = socket.socket()
f = True
while f:
    hostname = getpass.getpass(prompt="Input host name: ")
    port = getpass.getpass(prompt="Input host port: ")

    if hostname == 'exit' or port == 'exit':
        f = False
    else:
        try:
            client.connect((hostname, int(port)))
            break
        except:
            print("Wrong arguments")

if not f:
    sys.exit()

while True: #Ждем информацию от сервера, когда он нас идентифицирует в системе
    data = client.recv(1024).decode()
    if data == 'log': #Если сервер отправил нам информацию, что пользователя нет в бд, то просит ввести имя пользователя
        username = input("Write your username: ")
        client.send(f'{username}'.encode())
    else:
        print(data)
        break

print("Connected to server")

command = input('You send: ')

while command!='exit':
    print("Send data to server")
    client.send(command.encode())

    data = client.recv(1024)

    print(f"You've recieved: {data.decode()}\n")

    command = input("You send: ")

client.send(command.encode())
print("Disconnecting from server")
client.close()
