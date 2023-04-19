from flask import Flask
import json

app = Flask(__name__)

produtos = {
    "nome": "",
    "descricao": "",
    "preco": ""
}

# Simula a criação do id pelo banco de dados
    # Com o banco de dados, o id passa a ser uma chave primária e autoincremento
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

@app.route("/produtos", methods=['GET', 'POST'])
def editar_produtos(id:int, dados_produtos:dict):
    produtos[id] = dados_produtos

# converte o dicionário produtos de python para JSON (observação que pode ser útil)
# produtos_json = json.dumps(produtos, indent=4) 


# converte a string JSON em dicionário python (observação que pode ser útil) 
# produtos_json = json.loads(produtos)

app.run(debug=True) 