# test_file.py
# This is a script to test whether fruitDAO & flask server are working correctly
# Author: Joanne Feeney
# Code copied from zteststudentDAO.py by Andrew Beatty

from fruitDAO import FruitDAO

fruit_dao = FruitDAO()

newfruit = {
  "name":"mango", 
  "country_of_origin":"india",
  "price":6
  }

# Create
fruit = fruit_dao.create(newfruit)
fruitid = fruit["id"]

# Find by ID
result = fruit_dao.findByID(fruitid)
print("Test create and find by id")
print(result)

# Update
newfruitvalues = {"name": "banana", "country_of_origin": "malaysia", "price": 2}
fruit_dao.update(fruitid, newfruitvalues)
result = fruit_dao.findByID(fruitid)
print("Test update")
print(result)

# Get all
print("Test get all")
allfruits = fruit_dao.getAll()
for fruit in allfruits:
  print(fruit)

# Delete
fruit_dao.delete(fruitid)
print("Test delete")