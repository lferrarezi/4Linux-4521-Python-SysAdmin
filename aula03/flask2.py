from flask import Flask, jsonify, request
from datetime import datetime
from flask_pymongo import PyMongo
from bson import json_util
import json, re


from faker import Faker
fake = Faker('pt_BR')

app = Flask(__name__) # main
app.config['MONGO_DBNAME'] = 'orquestrador'
mongo = PyMongo(app)

fname = fake.name()
femail = fake.email()
fcpf = fake.cpf()
print(fname+' '+femail+' '+fcpf)
# print(fname)
# print(femail)
# print(dir(fake))

@app.route('/usuarios', methods=['GET', 'POST'])
@app.route('/usuarios/', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        data = request.get_json()
        u = Usuarios()
        u.nome = data['nome']
        u.email = data['email']
        u.save() # u.update() atualiza e u.delete() remove
        return jsonify(request.get_json({'status' : 1,
                                         'message' : 'Usuário cadastrado com sucesso!'}))
    else:
        nome = request.args.get('nome')
        nome = re.compile(nome, re.IGNORECASE)
        usuarios = [json.loads(json_util.dumps(u)) for u in mongo.db.usuarios.find({'nome' : nome})]
        print(usuarios)
        return jsonify(usuarios)

        # users = [u for u in Usuarios.objects]
        # users = sorted(users, key=lambda u : u['nome']) # organiza por ordem alfabética de nome
        #
        # map(lambda i : del i['_id'], users)
        # return jsonify(users)

        # for u in Usuarios.objects:
        #     return jsonify(u)

def remove_id(i):
    del i['_id']
    return i

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
    return jsonify([{'Mensagem':'Teste!'}])

@app.route('/noticias/', methods=['POST'])
@app.route('/noticias', methods=['POST'])
def noticia():
    return jsonify(request.get_json())

@app.route('/noticias/<int:i>')
def noticias(i=None):
    noticias = [{'Gasolina' : 'O preço da gasolina...'},
        {'Monsanto' : 'A fusão da Bayer com a Monsanto...'},
        {'Calamidade' : 'Exército diz que há um risco...'}]

    try:
        return jsonify(noticias if i is None else noticias[i])
    except:
        return jsonify({'Erro': 'Notícia não encontrada'})

    # if i is None:
    #     return jsonify(noticias)
    # else:
    #     if i < len(noticias):
    #         return jsonify(noticias[i])
    #     else:
    #         return jsonify({'Erro':'Notícia não encontrada'})

# app.run(host='0.0.0.0', debug=True, port='80')
app.run(debug=True)
