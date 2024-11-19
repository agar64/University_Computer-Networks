# -*- coding: utf-8 -*-
"""
Alunos: Douglas Gaspar Feitosa Freitas (389129)
        Marcelo de Souza Ribeiro       (389133)

Lab 03
"""

'''Questão 1'''
'''Item A'''

import socket                            #Importa socket

host = 'myanimelist.net'               #Define o server

port = 80                                #Define a porta

server_ip = socket.gethostbyname(host) #Pega e imprime o IP do server
print(server_ip)                         #Não é essencial, mas ajuda a ficar bonitinho

request = "GET / HTTP/1.1\nHost: "+host+"\n\n"         #Guarda a requisição HTTP na variável request
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Cria um socket chamado s
s.connect((host, port))                                #Conecta ao host usando a porta definida

s.send(request.encode())                               #Codifica e envia a mensagem
result = s.recv(4096)                                  #Recebe e armazena em buffer a resposta do servidor

while (len(result) > 0):                               #Continua recebendo e imprimindo a resposta
    print(result)
    result = s.recv(4096)

#O cliente utiliza TCP, o que pode ser visto pela utilização do SOCK_STREAM. O site retorna o código 301, que
#significa Movido Permanentemente. No caso, o site foi movido pra HTTPS.
    
'''Item B'''

target = "hackthissite.org"                        #Define como alvo um site de testes
ports = [20,21,22,25,53,110,443,8080,3306]         #Portas definidas no pdf

def pscan(port):                                   #Define pscan para testar se é possível conectar
    try:
        s.connect((target,port))
        return True                                #Se for, retorna true
    except:
        return False


for x in ports:                                    #percorre as portas
    if pscan(x):                                   #se pscan for true,
        serv = socket.getservbyport(x)             #obtém a porta e imprime
        print("A porta " + x + " está aberta e com o serviço " + serv)