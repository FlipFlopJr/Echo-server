import socket

server = socket.socket()            # создаем объект сокета сервера
hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = 12345                        # устанавливаем порт сервера
server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
print("Server starts")

server.listen(5)




while True:
    print("Server started listening")

    con, addr = server.accept()
    print("Client connected")

    try:
        while True:
            data = con.recv(1024).decode()
            print('recieved data')

            if data == 'exit':
                con.close()
                break
            else:
                print('Send data back')
                con.send(data.encode())
    except:
        pass