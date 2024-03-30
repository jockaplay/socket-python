import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 5050))
server.listen(2)

print('Online!\nEsperando conexões...')

def run():

    connection, address = server.accept()
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'inventory'))
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    # Enviar a lista de arquivos como uma string
    file_names_str = ','.join(files)
    connection.send(file_names_str.encode())

    print("Lista de arquivos enviada!")

    # Receber o nome do arquivo selecionado
    selected_file_name = connection.recv(1024).decode()
    if selected_file_name == '0':
        return
    print("Arquivo selecionado:", selected_file_name)

    # Ler e enviar o conteúdo do arquivo selecionado como uma string
    with open(os.path.join(path, selected_file_name), 'r') as file:
        file_content = file.read()
        connection.send(file_content.encode())

    print("Arquivo enviado!")
    connection.close()
    run()
    
run()
server.close()
input()