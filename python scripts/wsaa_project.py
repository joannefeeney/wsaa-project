# wsaa_project.py
# By Joanne Feeney
# In this python project, I will create an application that provides an online user interface 
# to perform CRUD operations on a database. This will include:
# 1. A Flask server that provides the RESTful API
# 2. A web page that allows the user to interact with that RESTful API


# Imports
import requests 
import urllib.parse
import parseString 
from github import Github

url = "http://127.0.0.1:5000"

response = requests.get(url) 

# Test URL is working by printing
print (response.json())

# Above converted into a function
def readbooks(): 
    response = requests.get(URL) 
    # we could do checking for correct response code here 
    return response.json() 

    if __name__ == "__main__": 
        print (readbooks())

# Function to find by id
def readbook(id): 
    geturl = URL + "/" + str(id) 
    response = requests.get(geturl) 
    # we could do checking for correct response code here 
    return response.json()

# Function to create an item
def createbook(book): 
    response = requests.post(URL, json=book) 
# should check we have the correct status code 
    return response.json()

# Function to update an item
def updatebook(id, book): 
    puturl = URL + "/" + str(id) 
    response = requests.put(puturl, json=book) 
    return response.json()

# Function to delete an item
def deletebook(id): 
    deleteurl = URL + "/" + str(id) 
    response = requests.delete(deleteurl) 
    return response.json()

# Create a file called rest_server.py
# Make a basic server in it and test it
from flask import Flask, url_for, request, redirect, abort 

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/') 
def index(): 
    return "hello"
if __name__ == "__main__": 
    app.run(debug=True)

# Create a mapping and function for each of the possible API calls
@app.route('/books', methods=['GET']) 
def getall(): 
    return "get all"

@app.route('/books/<int:id>', methods=['GET']) 
def findbyid(id): 
    return "find by id" 

# Create
@app.route('/books', methods=['POST']) 
def create(): 
    # read json from the body 
    jsonstring = request.json 
    
    return f"create {jsonstring}" 

# Update 
@app.route('/books/<int:id>', methods=['PUT']) 
def update(id): 
    jsonstring = request.json 
    return f"update {id} {jsonstring}" 

# Delete 
@app.route('/books/<int:id>', methods=['DELETE']) 
def delete(id): 
    return f"delete {id}"

# Using either postman or CURL test each of your endpoints
'''# getall 
curl http://127.0.0.1:5000/books 

# find by id 
curl http://127.0.0.1:5000/books/1 

# create 
curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books

# update 
curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books/1 

# delete 
curl -X DELETE http://127.0.0.1:5000/books/1'''

