from flask import Flask,render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Models/banco.db"

db = SQLAlchemy(app)

class Usuarios(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String())
    email = db.Column(db.String(),unique=True)

    def __init__(self,nome="",email=""):
        self.nome = nome
        self.email = email

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/chamado/<numero>/")
def chamado(numero):
    return render_template("chamado.html")

@app.route("/provisionamento/")
def provisionamento():
    return render_template("provisionamento.html")

@app.route("/provisionamento/novo/",methods=["POST"])
def provisionamento_novo():
    try:
        j = json.loads(request.get_json())
        j["gitlab"]["desenvolvedores"] = j["gitlab"]["desenvolvedores"].split(",")
        j["jenkins"]["branches"] = j["jenkins"]["branches"].split(",")
        j["docker"] = j["docker"].split(",")
        client = MongoClient("127.0.0.1")
        db = client["dexterops"]
        db.provisionamento.insert(j)
        return jsonify({"message":"Inserido no banco com sucesso"})
    except Exception as e:
        print("erro %s"%e)
        return jsonify({"message":"%s"%e})

@app.route("/provisionamento/lista/")
def provisionamento_lista():
    try: 
        client = MongoClient("127.0.0.1")
        db = client["dexterops"]
        lista = db.provisionamento.find({"_id":1})[0]
        return jsonify(lista)
    except Exception as e:
        print("erro %s"%e)
        return jsonify({"message":"%s"%e})

@app.route("/usuarios/")
def usuarios_listar():
    try:        
        users = Usuarios.query.all()
        dic = {"usuarios":[]}
        for u in users:
            dic['usuarios'].append({"id":u.id,"nome":u.nome,"email":u.email})
        return jsonify(dic)
    except Exception as e:
        return jsonify({"status":1,"message":"Ocorreu um erro: %s"%e})

@app.route("/usuarios/",methods=["POST"])
def usuarios_cadastrar():
    try:
        print(request.headers)
        res = request.get_json()
        print(res)
        user = Usuarios(res['nome'],res['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message":"Usuario cadastrado com sucesso"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"status":1,"message":"Ocorreu um erro: %s"%e})

@app.route("/usuarios/<int:id>/",methods=["PUT"])
def usuarios_atualizar(id):
    try:
        user = Usuarios.query.filter(Usuarios.id==id).first()
        dados = request.get_json()
        for k in dados.keys():
            setattr(user,k,dados[k])
        db.session.commit()
        user = Usuarios.query.filter(Usuarios.id==id).first()
        user.__dict__.pop("_sa_instance_state",None)
        return jsonify(user.__dict__)
    except Exception as e:
        db.session.rollback()
        return jsonify({"status":1,"message":"Ocorreu um erro: %s"%e})

@app.route("/usuarios/<int:id>/",methods=["DELETE"])
def usuarios_deletar(id):
    try:
        user = Usuarios.query.filter(Usuarios.id==id).first()
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message":"Usuario deletado com sucesso!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"status":1,"message":"Ocorreu um erro: %s"%e})

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True,host="0.0.0.0")
