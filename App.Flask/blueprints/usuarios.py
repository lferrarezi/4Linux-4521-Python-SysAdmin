import json, re
from mdb import db
from bson import json_util
from flask import jsonify, request, Blueprint

users = Blueprint('users', __name__) # __main__

@users.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        data = request.get_json()
        u = {}
        u.nome = data['nome']
        u.email = data['email']
        u.save() # u.update() atualiza e u.delete() remove
        return jsonify(request.get_json({'status' : 1,
                                         'message' : 'Usuário cadastrado com sucesso!'}))
    else:
        # criar um dicionário dinamicamente
        seletor = {}
        campos = ['nome','email']
        for c in campos:
            value = request.args.get(c)
            if value:
                seletor[c] = re.compile(value)

        usuarios = [json.loads(json_util.dumps(u)) for u in db.usuarios.find(seletor)]
        print(usuarios)
        return jsonify(usuarios)