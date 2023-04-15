from flask import Flask
import json

app = Flask(__name__)

produtos = {
    "nome": "",
    "descricao": "",
    "preco": ""
}

# Simula a criação do id pelo banco de dados
def gerar_id():
    id = len(produtos) + 1
    return id

# Cria um novo produto no dicionário
@app.route("/produtos", methods=['POST'])
def criar_produtos(nome, descricao, preco):
    produtos[gerar_id()] = {"nome": nome, "descricao": descricao, "preco": preco}

@app.route("/produtos", methods=['POST'])  
def deleta_produto(id:int):
    del produtos[id]

app.run(debug=True) 
