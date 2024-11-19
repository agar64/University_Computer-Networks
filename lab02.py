# -*- coding: utf-8 -*-
"""
Alunos: Douglas Gaspar Feitosa Freitas (389129)
        Marcelo de Souza Ribeiro       (389133)

Lab 02
"""

'''Questão 1'''
'''Item A'''

import urllib, urllib.request, urllib.error, urllib.parse
hosts = ["https://crunchyroll.com", "https://myanimelist.net", "https://pcgamer.com", "https://store.steampowered.com", "https://youtube.com", "http://pudim.com.br", "https://stackoverflow.com", "https://telegram.org", "http://nicovideo.jp", "https://videolan.org"]
                                                    #cria uma lista de sites do quais faremos requisições HTTP
for host in hosts:                                  #percorre a lista
    site = urllib.request.urlopen(host)             #faz requisição HTTP ao site
    print(host, "\n")                               #printa o site e quebra a linha
    print("HTTP Code:", site.getcode(), "\n")       #printa o código HTTP e quebra a linha
    print(site.info())                              #printa a metadata

'''Uma das meta informações que pode ser obtida em quase todos os sites requisitados é "Server", que indica qual é o
tipo de servidor que hosteia aquele site. Os tipos encontrados, em ordem, foram:
    Crunchyroll: Cloudflare
    My Anime List: Apache
    PC Gamer: Não apareceu
    Steam: Apache
    YouTube: YouTube Frontend Proxy
    pudim.com.br: Apache
    StackOverflow: Não apareceu
    Telegram: nginx
    Nico Nico Douga: Apache
    Videolan: nginx'''
    
'''Item B'''
'''O código de resposta foi capturado e exibido no item A. Os códigos foram todos iguais, 200. O código 200 do HTTP
significa "OK", ou seja, a requisição foi realizada com sucesso e autorizada e logo mais virá o arquivo da página
requisitada'''

'''Questão 2'''
'''Item A'''

import json

addresses = ["60455900","60020181","60060390","60455970","60160140","60411205"]     #define uma lista de CEPs

for address in addresses:                     #percorre a lista
    url = urllib.request.urlopen('http://viacep.com.br/ws/' + address + '/json') #obtém o JSON do ViaCep
    data = json.load(url)                                #converte o JSON pro formato de dicionário do Python
    if next(iter(data)) == "erro":                       #por algum motivo, se tem algum erro no CEP, o site retorna um JSON com apenas uma marcação de "erro: true", então essa gambiarra foi feita pra dar a volta nisso.
        print("CEP: " + address + "\n" + "Erro Encontrado \n") #ele checa se o primeiro item se chama "erro", se sim, ele manda esse aviso
    else:
        print("CEP: " + data["cep"] + "\n" + "Logradouro: " + data["logradouro"] + "\n" + "Complemento: " +
            data["complemento"] + "\n" + "Bairro: " + data["bairro"] + "\n" + "Localidade: " +
            data["localidade"] + "\n" + "UF: " + data["uf"] + "\n" + "Unidade: " + data["unidade"] + "\n" +
            "IBGE: " + data["ibge"] + "\n" + "GIA: " + data["gia"] + "\n")
            #printa as informações de forma bonitinha

'''Item B'''


try:
    site = urllib.request.urlopen('https://www.google.com.br/search?q=anime')  #faz a requisição HTTP
    print("HTTP Code:", site.getcode(), "\n")                                  #tenta obter o código HTTP                   
    print(data.info())                                                         #tenta obter a metadata
except urllib.error.HTTPError as e:                                            #tenta lidar com as exceções
    print('Error code: ', e.code)
except urllib.error.URLError as e:
    print('Reason: ', e.reason)
    
'''Ao tentar, vemos que ocorre uma exceção que é pega pelo HTTPError, o Google retorna o código de erro 403, 
que significa "proibido", ou seja, que o servidor não nos garantiu permissão para realizar a requisição. Uma rápida
pesquisa, ironicamente, no Google, me informou que isso se deve ao Google bloquear requisições diretas, que não
foram feitas por browsers, exigindo que você use a API deles, e ainda assim, os termos de uso proibem pesquisas
automatizadas, dizendo: "Automated requests are prohibited; all requests must be made as a result of
an end-user action."'''