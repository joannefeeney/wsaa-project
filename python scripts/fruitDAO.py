# fruitDAO.py
# This is a data layer that connects to a database
# Author: Joanne Feeney
# Code copied from bookDAO.py by Andrew Beatty

import mysql.connector 
# Config file
from config import mysqlkey as mysqlkey

class FruitDAO:
    host ="" 
    user = "" 
    password ="" 
    database ="" 
    connection = "" 
    cursor ="" 
    
    def __init__(self): 
        #these should be read from a config file 
        self.host=mysqlkey("host")
        self.user=mysqlkey("user")
        self.password=mysqlkey("password")
        self.database=mysqlkey("database")
        
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

    def create(self, values): 
        cursor = self.getCursor() 
        sql="insert into fruits (name, country_of_origin, price) values (%s,%s,%s)" 
        cursor.execute(sql, values) 
        
        self.connection.commit() 
        newid = cursor.lastrowid 
        self.closeAll() 
        return newid 
    
    def getAll(self): 
        cursor = self.getcursor()
        sql="select * from fruits"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray
        
    def findByID(self, id): 
        cursor = self.getcursor()
        sql="select * from fruits where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    def update(self, values): 
        cursor = self.getcursor()
        sql="update fruits set name= %s,country_of_origin=%s, price=%s  where id = %s"
        
        values = (fruits.get("name"), fruits.get("country_of_origin"), fruits.get("price"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
    
    def delete(self, id): 
        cursor = self.getcursor()
        sql="delete from fruits where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

fruitDAO = FruitDAO()
