from flask import Flask
import json

app = Flask(__name__)

produtos = {
    "nome": "",
    "descricao": "",
    "preco": ""
}

def gerar_id():
    id = len(produtos) + 1
    return id

@app.route("/produtos", methods=['POST'])
def criar_produtos(nome, descricao, preco):
    produtos[gerar_id()] = {"nome": nome, "descricao": descricao, "preco": preco}

app.run(debug=True) 
