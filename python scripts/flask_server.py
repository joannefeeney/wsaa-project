# flask_server.py
# Basic Flask server
# Author: Joanne Feeney
# Code copied from WSAA lectures by Andrew Beatty

# Imports
from flask import Flask, request, jsonify
from fruitDAO_skeleton import fruitDAO 

# Flask
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# GET, POST etc. function
@app.route('/')
def index():
    return "Hello Joanne"

# GET
@app.route('/fruits', methods=['GET'])
def getall():
    # return "Get all fruits"
    return jsonify(fruitDAO.getAll())

# GET by id
@app.route('/fruits/<int:id>', methods=['GET'])
def findbyid(id):
    # return "Find by id"
    return jsonify(fruitDAO.findByID(id))

# POST (create new)
@app.route('/fruits', methods=['POST'])
def create():
    # This will read json from the body
    jsonstring = request.json
    # Cannot test in browser, only by POSTMAN  
    fruit = {}
    fruit["name"] = jsonstring["name"]
    fruit["country_of_origin"] = jsonstring["country_of_origin"]
    fruit["price"] = jsonstring["price"]

    return jsonify(fruitDAO.create(fruit))

# PUT (update)
@app.route('/fruits/<int:id>', methods=['PUT'])
def update(id):
    # Request json only
    jsonstring = request.json
    fruit = {}
    fruit["name"] = jsonstring["name"]
    fruit["country_of_origin"] = jsonstring["country_of_origin"]
    fruit["price"] = jsonstring["price"]

    return jsonify(fruitDAO.update(id, fruit))

# DELETE
@app.route('/fruits/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(fruitDAO.delete(id))

if __name__ == "__main__":
    app.run(debug = True)

