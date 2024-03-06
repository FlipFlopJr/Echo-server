# Создать простой TCP-сервер, который принимает от клиента строку (порциями по 1 КБ) и возвращает ее. (Эхо-сервер).
import socket

client = socket.socket()
hostname = socket.gethostname()
port = 12345

client.connect((hostname, port))

print("Connected to server")

command = input('You send: ')

while command!='exit':
    print("Send data to server")
    client.send(command.encode())

    data = client.recv(1024)
    print(f"You've recieved: {data.decode()}")

    command = input("You send: ")

client.send(command.encode())
print("Disconnecting from server")
client.close()
