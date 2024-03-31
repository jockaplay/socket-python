import socket
import os
import json

with open('config.json', 'r') as file:
    dados = json.load(file)
    print(dados['ip'])

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.connect((dados['ip'], 5050))

        # Receber a lista de arquivos como uma string
        file_names_str = client.recv(1024).decode()
        file_names = file_names_str.split(',')
        print("Lista de arquivos recebida:", file_names)

        # Selecionar um arquivo
        selected_file_name = input("Digite o nome do arquivo que deseja enviar: ")
        if selected_file_name == '0':
            client.send(selected_file_name.encode())
            return
        try:
            client.send(selected_file_name.encode())
        except Exception as e:
            print(e)

        # Receber e salvar o conteúdo do arquivo selecionado
        file_content_str = client.recv(1024).decode()
        local = f'C:/Users/{os.getlogin()}/Downloads/{file_names_str}'
        with open(local, 'w') as file:
            file.write(file_content_str)

        print("Arquivo recebido e salvo em: " + local)

        client.close()
    except Exception as e:
        print(e)
        
main()
    
input("Pressione Enter para fechar.")