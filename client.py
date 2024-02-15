import socket
import threading
import tkinter as tk

# Dados(alvo) para conexão com Servidor
SERVER = ("127.0.0.1", 65432)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receber():
    while True:
        mensagem = s.recv(1024).decode('utf-8')
        area_texto.insert("end", mensagem)


def conectar(cliente):
    try:
        s.connect(SERVER)
        s.send(cliente.encode())

        print('Conectado ao servidor')

        thread_receber = threading.Thread(target=receber)
        thread_receber.start()
    except Exception as e:
        print(e)


def enviar_mensagem():
    mensagem = entrada_mensagem.get()
    area_texto.insert("end", f"Você: {mensagem}\n")
    entrada_mensagem.delete(0, "end")
    s.send(mensagem.encode('utf-8'))


def pedir_nome():
    janela = tk.Tk()
    janela.title("Nome")

    rotulo_nome = tk.Label(text="Digite seu nome:", font=("Arial", 12))
    rotulo_nome.pack()

    caixa_nome = tk.Entry(width=30)
    caixa_nome.pack()

    def obter_nome():
        nome = caixa_nome.get()
        janela.destroy()
        conectar(nome)

    botao_ok = tk.Button(text="OK", command=obter_nome)
    botao_ok.pack()

    janela.mainloop()


pedir_nome()

janela = tk.Tk()
janela.geometry("400x380")
janela.title("Chat")

area_texto = tk.Text(janela, height=20, width=50)
area_texto.pack()

entrada_mensagem = tk.Entry(janela, width=50)
entrada_mensagem.pack()

botao_enviar = tk.Button(janela, text="Enviar", command=lambda: enviar_mensagem())
botao_enviar.pack()
janela.mainloop()
