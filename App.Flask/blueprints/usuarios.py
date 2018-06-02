import json, re
from datetime import datetime
from mdb import db
from bson import json_util
from flask import jsonify, request, Blueprint, render_template
from faker import Faker

fake = Faker('pt-BR')
users = Blueprint('users', __name__) # __main__

@users.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        data = request.get_json()
        u = {}
        u['nome'] = data['nome']
        u['email'] = data['email']
        u['dcadastro'] = str(datetime.now().date())
        db.usuarios.insert(u)
        return jsonify({'status' : 1, 'message' : 'Usuário cadastrado com sucesso!'})
    else:
        # criar um dicionário dinamicamente
        seletor = {}
        campos = ['nome','email', 'dcadastro']
        for c in campos:
            value = request.args.get(c)
            if value:
                seletor[c] = re.compile(value)

        usuarios = [json.loads(json_util.dumps(u)) for u in db.usuarios.find(seletor)]
        for u in usuarios:
            u['_id'] = u['_id']['$oid']

        return render_template('layout.html', usuarios=usuarios)

@users.route('/usuarios_dumb', methods=['GET', 'POST'])
@users.route('/usuarios_dumb/', methods=['GET', 'POST'])
def usuarios_dumb():
    if request.method == 'GET':
        u_d = {}
        u_d['nome'] = fake.name()
        u_d['email'] = fake.email()
        u_d['dcadastro'] = str(datetime.now().date())
        db.usuarios.insert(u_d)
        return jsonify({'status': 1,'message': 'Usuário cadastrado com sucesso!'})