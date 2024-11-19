# -*- coding: utf-8 -*-
"""
Alunos: Douglas Gaspar Feitosa Freitas (389129)
        Marcelo de Souza Ribeiro       (389133)

Lab 01
"""

'''Questão 1'''
'''Itens A e B'''
import socket                           #importa socket para que possamos usar as funções dele
name = socket.gethostname()             #obtém o hostname e o guarda na recém criada variável "name"
IP = socket.gethostbyname(name)         #obtém o IP local do computador a partir do hostname e o guarda na variável "IP"
print(name)                             #exibe no console o hostname guardado na variável name
print(IP)                               #exibe no console o IP guardado na variável IP

'''Item C'''
#Mostrar os servições das portas de 1 a 9999

for port in range(1,10000):                          #loop para percorrer as portas de 1 a 9999
    try:                                             #se não tratada, ao encontrar uma porta sem serviço, python interrompe com uma exceção
        serv = socket.getservbyport(port)            #procura na porta da vez qual serviço está mapeado para ela
        print(port, "-", serv)                       #imprime a porta e o nome do serviço
    except:                                          #no caso de uma exceção, continuar escaneando
        continue                                     #por isso, portas não inclusas na lista não tem serviços associados a elas

'''Questão 2'''
'''Item A'''
#Criar uma lista de 10 hostnames e seus IPs

hosts = ["crunchyroll.com", "myanimelist.net", "pcgamer.com", "store.steampowered.com", "youtube.com", "pudim.com.br", "stackoverflow.com", "telegram.org", "nicovideo.jp", "videolan.org"]
                                                    #cria uma lista de sites do quais obteremos o IP
for host in hosts:                                  #percorre a lista
    IP = socket.gethostbyname(host)                 #pega o IP e o guarda na variável IP
    print(host, "-", IP)                            #printa o site e o IP correspondente
    
'''Item B'''
#Obter dados dos IPs

import requests                                                           #importa requests, que será necessário para o próximo passo

for host in hosts:                                                        #percorre a lista criada no item A
    req = requests.get("http://freegeoip.net/json/%s" % host)             #pega o JSON fornecido pelo freegeoip com os dados do site
    print(host, "-", req.json()["country_name"])                          #decodifica o JSON e printa o country_name contido nele