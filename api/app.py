from flask import Flask, request, jsonify
import dictionary

app = Flask(__name__)

@app.route("/produtos/<int:id>", methods = ['GET'])
def show_product(id:int):
    return dictionary.return_product(id)

app.run(debug=True)