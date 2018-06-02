from blueprints.usuarios import users
from flask import Flask, jsonify, request
from bson import json_util
from datetime import datetime
import json
import re

app = Flask(__name__) #__main__
app.register_blueprint(users)

@app.route('/') # o app estanciado como flask está ouvindo o acesso na raiz (/)
def index(): # esta é a função a ser executada quando do acesso na raiz (/)
    retorno = {'status':1 ,
               'mensagem':'Hello World!'}
    return jsonify(retorno)

app.run(debug=True)