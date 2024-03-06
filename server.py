import socket
import threading

HOST = '0.0.0.0'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print(f'Servidor em Execução em {s.getsockname()}')

clientes = []


def cliente(conn, nome):
    while True:
        mensagem = conn.recv(1024).decode('utf-8')
        if mensagem:
            print('Mensagem recebida: ', mensagem)

            for cliente in clientes:
                if cliente is not conn:
                    texto = nome + ": " + mensagem + "\n"
                    cliente.send(texto.encode('utf-8'))
        else:
            clientes.remove(conn)
            conn.close()


while True:
    conn, addr = s.accept()
    print(f'Conectado por {addr}')
    nome = conn.recv(1024).decode()
    print(f'Nome: {nome}')

    clientes.append(conn)

    thread = threading.Thread(target=cliente, args=(conn, nome))
    thread.start()
