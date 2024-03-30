import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('25.38.213.87', 5050))
server.listen(2)

print('Online!\n\nEsperando conexões...')

connection, address = server.accept()

namefile = connection.recv(1024).decode()

with open(namefile, 'rb') as file:
    for data in file.readlines():
        connection.send(data)
        
    print("Arquivo enviado!")