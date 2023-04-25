from flask import Flask, request, jsonify
import dictionary

app = Flask(__name__)

# Route to return a single product by id
@app.route("/products/<int:id>", methods = ['GET'])
def show_product(id:int):
    return dictionary.return_product(id)

# Route to return all products
@app.route("/products", methods = ['GET'])
def show_all():
    return dictionary.return_products()

#


app.run(debug=True)