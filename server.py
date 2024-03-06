import socket

server = socket.socket()            # создаем объект сокета сервера
hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = 12345                        # устанавливаем порт сервера
server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту

server.listen(5)




while True:
    


    con, addr = server.accept()
    file = open(f"logfile_{addr}","w")
    file.write("Server starts\n")
    file.write("Server started listening\n")

    file.write("Client connected\n")


    try:
        while True:
            data = con.recv(1024).decode()

            file.write(f"Recieved data: {data}\n")

            if data == 'exit':
                con.close()
                file.write(f"Connection with {addr} closed\n")
                file.close()
                break
            else:

                file.write("Send data back\n")
                con.send(data.encode())
    except:
        pass