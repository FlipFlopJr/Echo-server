import socket


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