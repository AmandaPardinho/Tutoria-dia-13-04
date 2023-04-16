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

# Cria um novo produto 
@app.route("/produtos", methods=['GET', 'POST'])
def criar_produtos(nome, descricao, preco):
    produtos[gerar_id()] = {"nome": nome, "descricao": descricao, "preco": preco}

# Deleta um produto
@app.route("/produtos", methods=['GET', 'POST'])  
def deleta_produto(id:int):
    del produtos[id]

@app.route("/produtos", methods=['GET'])
def editar_produtos(id:int, dados_produtos:dict):
    produtos[id] = dados_produtos


    
app.run(debug=True) 
