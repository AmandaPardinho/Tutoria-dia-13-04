from flask import Flask
import json
import sqlite3

app = Flask(__name__)

# A tabela PRODUTOS criada no banco de dados deve conter as seguintes informações: ID_PRODUTO, NOME_PRODUTO, DESCRICAO_PRODUTO, MARCA_PRODUTO, PRECO_PRODUTO

# Com o banco de dados, o id passa a ser uma chave primária com autoincremento, ou seja, é criado assim que o produto é adicionado (não é preciso fazer uma função para criá-lo)

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