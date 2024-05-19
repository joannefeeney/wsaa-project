# fruitDAO.py
# This is a data layer that connects to a database
# Author: Joanne Feeney
# Code copied from bookDAO.py by Andrew Beatty

import mysql.connector 
# Config file
import config as config

class FruitDAO:
    host ="" 
    user = "" 
    password ="" 
    database ="" 
    connection = "" 
    cursor ="" 
    
    def __init__(self): 
        # Read from my config file 
        self.host=config.host
        self.user=config.user
        self.password=config.password
        self.database=config.database
        
    def getCursor(self): 
        self.connection = mysql.connector.connect( 
            host=self.host, 
            user=self.user, 
            password=self.password, 
            database=self.database 
        ) 
        self.cursor = self.connection.cursor() 
        return self.cursor 
    
    def closeAll(self): 
        self.connection.close() 
        self.cursor.close()  

    def create(self, fruit): 
        cursor = self.getCursor() 
        sql="insert into fruit (name, country_of_origin, price) values (%s,%s,%s)" 
        values = (fruit.get("name"), fruit.get("country_of_origin"), fruit.get("price"))
        cursor.execute(sql, values) 
        
        self.connection.commit() 
        newid = cursor.lastrowid 
        fruit["id"] = newid
        self.closeAll() 
        return fruit 
    
    def getAll(self): 
        cursor = self.getCursor()
        sql="select * from fruit"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for row in results:
            #print(result)
            returnArray.append(self.convertToDict(row))
        
        self.closeAll()
        return returnArray
        
    def findByID(self, id): 
        cursor = self.getCursor()
        sql="select * from fruit where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result)
    
    def update(self, id, fruit): 
        cursor = self.getCursor()
        sql="update fruit set name= %s, country_of_origin=%s, price=%s where id = %s"
        
        values = (fruit.get("name"), fruit.get("country_of_origin"), fruit.get("price"),id)
        cursor.execute(sql, values)
        self.connection.commit()

        self.closeAll()
        return fruit
    
    def delete(self, id): 
        cursor = self.getCursor()
        sql="delete from fruit where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")
        return True
    
    def convertToDict(self, resultLine):
        fruitKeys = ["id", "name", "country_of_origin", "price"]
        currentkey = 0
        fruit = {}
        for attrib in resultLine:
            fruit[fruitKeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return fruit

fruitDAO = FruitDAO()