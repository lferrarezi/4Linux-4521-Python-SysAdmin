from flask import Flask, jsonify, json

app = Flask(__name__) # main

@app.route('/') # o app estanciado como flask está ouvindo o acesso na raiz (/)
def index(): # esta é a função a ser executada quando do acesso na raiz (/)
    retorno = {'status':1 ,
               'mensagem':'Hello World!'}
    return jsonify(retorno)

@app.route('/a/') # o app estanciado como flask está ouvindo o acesso em a (/a)
@app.route('/a') # o app estanciado como flask está ouvindo o acesso em a (/a)
def a(): # esta é a função a ser executada quando do acesso em a (/a)
    return jsonify([{'Gasolina': 'O Preço da gasolina...'},
                    {'Etanol':'Acabou!'},
                    {'Mensagem':'Halla Warld!'}
                    ])

@app.route('/teste')
def teste():
    return jsonify([{'Mensagem':'Teste!'}
                    ])


# app.run(host='0.0.0.0', debug=True, port='80')
app.run(debug=True)
