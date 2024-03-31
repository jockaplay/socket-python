import socket
import os
import json

with open('config.json', 'r') as file:
    dados = json.load(file)
    print(dados['ip'])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((dados['ip'], 5050))
server.listen(2)

print('Online!\nEsperando conexões...')

def run():

    connection, address = server.accept()
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'inventory'))
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    file_names_str = ','.join(files)
    connection.send(file_names_str.encode())

    print("Lista de arquivos enviada!")

    try:
        selected_file_name = connection.recv(1024).decode()
    except Exception as e:
        selected_file_name = ""
        print(e)
        
    if selected_file_name == "" or selected_file_name == '0':
        print('O cliente cancelou o download.')
    else:
        print("Arquivo selecionado: ", selected_file_name)
        with open(os.path.join(path, selected_file_name), 'r') as file:
            file_content = file.read()
            connection.send(file_content.encode())

        print("Arquivo enviado!")
        connection.close()
    run()
    
run()
server.close()