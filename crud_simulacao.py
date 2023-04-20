from flask import Flask, request
import dicionario
import json
import sqlite3

app = Flask(__name__)

produtos = {
    1: {
        "id": 1,
        "nome": "Lapiseira Pentel Técnica Vermelha",
        "descricao": "Lapiseira para desenho técnico com grafite de 0.3mm",
        "marca": "Pentel",
        "preco": 18.99
    },
    2: {
        "id": 2,
        "nome": "Post It 3M",
        "descricao": "Post It 3M Pink",
        "marca": "3M",
        "preco": 9.99
    },
    3: {
        "id": 3,
        "nome": "Patinho de borracha",
        "descricao": "Patinho de borracha amarelo",
        "marca": "Suzano",
        "preco": 5.99
    }
}

produto = {
        
        "nome": "Fita métrica",
        "descricao": "Fita métrica rosa com 1.5 metro de comprimento",
        "marca": "Sem marca",
        "preco": 1.99
}

# A tabela PRODUTOS criada no banco de dados deve conter as seguintes informações: ID_PRODUTO, NOME_PRODUTO, DESCRICAO_PRODUTO, MARCA_PRODUTO, PRECO_PRODUTO

# Com o banco de dados, o id passa a ser uma chave primária com autoincremento, ou seja, é criado assim que o produto é adicionado (não é preciso fazer uma função para criá-lo)

def novo_indice():
    indice = max(produtos.keys()) + 1
    return indice

#Algumas ações não devem ficar disponíveis para o USUÁRIO, mas sim apenas para o ADMINISTRADOR

# Cria um novo produto => apenas o administrador
@app.route("/produto", methods=['POST'])
def criar_produto():
    produtos[novo_indice()] = produto
    return produtos

# Deleta um produto => apenas o administrador
@app.route("/produtos/<int:id>", methods=['DELETE'])  
def deleta_produto(id:int):
    del produtos[id]

# Editar um produto => apenas o administrador
@app.route("/produto/<int:id>", methods=['UPDATE'])
def editar_produto(id:int):
    produtos[id] = {"dados_produtos"}

@app.route("/produtos", methods=['GET'])
def retornar_produtos():
    return produtos

@app.route("/produto/<int:id>", methods=['GET'])
def retorna_produto(id:int):
    return produtos[id]
# converte o dicionário produtos de python para JSON (observação que pode ser útil)
# produtos_json = json.dumps(produtos, indent=4) 


# converte a string JSON em dicionário python (observação que pode ser útil) 
# produtos_json = json.loads(produtos)

app.run(debug=True) 