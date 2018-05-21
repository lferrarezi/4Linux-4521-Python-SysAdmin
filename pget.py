#!/usr/local/bin/python3
import requests, json
URL = "http://127.0.0.1:5000/usuarios/"

def pget_cadastra(vUser):
    data = vUser
    headers = {"Content-Type":"application/json"}
    request = requests.post(URL, data=json.dumps(data), headers=headers) # IMPORTANTE: ustilizar o json.dumps() para converter o conteúdo
    print(request.text)

with open("users.csv", "r") as file:
    # for linha in [linha.strip() for linha in file.readlines()]:
    for linha in file.readlines():
        usuario = {"nome":linha.strip().title(), "email":linha.strip()+"@"+linha.strip()+".com.br"}
        # usuario = {"nome":linha.strip().title(), "email":"{}@uol.com.br".format(l)}
        print(usuario)
        pget_cadastra(usuario)

