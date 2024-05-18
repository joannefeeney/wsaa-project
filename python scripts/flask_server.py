# Basic Flask server

# Imports
from flask import Flask

# Flask
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# GET, POST etc. function
@app.route('/')
def index():
    return "Hello Joanne"

# GET
@app.route('/fruits', methods=['GET'])
def getall():
    return "Get all fruits"

# GET by id
@app.route('/fruits/<int:id>', methods=['GET'])
def findbyid(id):
    return "Find by id"

# POST (create new)
@app.route('/fruits', methods=['POST'])
def create():
    # This will read json from the body
    # Cannot test in browser, only by POSTMAN
    return "Create"

if __name__ == "__main__":
    app.run(debug = True)

