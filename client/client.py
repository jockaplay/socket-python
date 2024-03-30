import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("25.38.213.87", 5050))

namefile = str(input("Arquivo >> "))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while True:
        data = client.recv(1000000)
        if data:
            file.write(data)
        else:
            break