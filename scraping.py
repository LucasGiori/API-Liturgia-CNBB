import requests,re
from bs4 import BeautifulSoup
from urllib import parse as urlDict

def _parser_data(response):
    #aqui é uma classe do python que realiza o parser do html
    soup = BeautifulSoup(response.text,"lxml")
    #aqui está fazendo uma busca pela <div class="blog-post" onde fica as leituras no site, depois tu pode olhar no html do site para ver
    post=soup.find_all("div", class_="blog-post")
    leitura=''
    for i in post:
        #aqui ele está pegando somente o texto do html e salvando na variael leitura
        leitura += str(i.get_text())
    #quando finalizar de coletas as leituras ele vai olhar esses \n->significa nova linha \t-> siginifica tabulação
    #quando tiver \n\n\n\n\t\t\t\t\t\t\t\t siginifica que é um novo texto, com a funcao split ele transforma cada texto em um elemento da lista
    return [texto.replace('\n','').replace('\t','') for texto in leitura.split('\n\n\n\n\t\t\t\t\t\t\t\t')]

def getReturnLiturgia(**kwargs): 
    #Neste if ele verifica se esta vindo parametros, caso não tiver ele vai puxar a leitura do dia   
    if kwargs.get('parametros') is None:
        response = requests.get(url='https://liturgiadiaria.cnbb.org.br/app/user/user/UserView.php')
        return _parser_data(response)
    #Caso tiver parametros ele vai fazer a requisição com o ano mes e dia informado na requisição da  api
    response =  requests.get(url='https://liturgiadiaria.cnbb.org.br/app/user/user/UserView.php?'+urlDict.urlencode(kwargs.get('parametros')))
    return _parser_data(response)
    
    
    