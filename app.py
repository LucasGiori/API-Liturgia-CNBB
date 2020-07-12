from flask import Flask, request, jsonify
from scraping import * #Aqui está importando todas as funções do arquivo scraping



app = Flask(__name__)
app.config["DEBUG"] = True
jsontypeerror = {"dados":[{"Message":"Invalid content-type. Must be application/json."}]}


# A route to return all of the available entries in our catalog.
@app.route('/api/liturgia', methods=['GET','POST'])
def getLiturgia(): 
    #se o metodo de requisição for post significa que o usuario quer especificar uma data para leitura
    if request.method == 'POST':
        #Verifica se o conteudo vindo na requisição é do tipo application/json, caso não for ele retorna um erro
        if request.content_type != 'application/json':
            return jsonify(jsontypeerror)   
        #aqui ele coleta o json da requisicao
        content = request.get_json()
        #e defini as variaveis, coletando cada atributo do json que o usuario enviou
        ano,mes,dia=int(content['ano']) , int(content['mes']) , int(content['dia'])
        #aqui ele está chamando a funçao de scraping
        return jsonify({"Liturgia":getReturnLiturgia(parametros={"ano":ano, "mes":mes, "dia":dia})})
    
    #caso ele não entrar no IF significa que a requisição é GET então o usuario chama a função 
    #de scraping mas não passa parametros assim vai trazer a leitura do dia
    return jsonify({"Liturgia":getReturnLiturgia()})
app.run()



