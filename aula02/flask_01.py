from flask import Flask, jsonify

app = Flask(__name__) # main

@app.route('/') # o app estanciado como flask está ouvindo o acesso na raiz (/)
def index(): # esta é a função a ser executada quando do acesso na raiz (/)
    return 'Hello World'

# app.run(host='0.0.0.0')
app.run()