#!/usr/local/bin/python3
import requests
URL = "http://127.0.0.1:5000/usuarios/"

request = requests.get(URL)
data = request.json()
# print(data["usuarios"][0]["nome"])
# print(data["usuarios"][0])

for user in data["usuarios"]:
    print(user["nome"])