#!/usr/local/bin/python3
import requests, json
URL = "http://127.0.0.1:5000/usuarios/"
ID = "16"
requests.delete(URL+ID+"/")