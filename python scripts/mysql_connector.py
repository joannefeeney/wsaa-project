# CRUD operation on MySql

import mysql.connector 

class StudentDAO:
    host ="" 
    user = "" 
    password ="" 
    database ="" 
    connection = "" 
    cursor ="" 
    
    def __init__(self): 
        #these should be read from a config file 
        self.host="localhost" 
        self.user="root" 
        self.password="" 
        self.database="wsaa" 
        
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
        sql="insert into student (name, age) values (%s,%s)" 
        cursor.execute(sql, values) 
        
        self.connection.commit() 
        newid = cursor.lastrowid 
        self.closeAll() 
        return newid 
    
    def getAll(self): 
        # your code here 
        
    def findByID(self, id): 
        #your code here 
    
    def update(self, values): 
        #your code here
    
    def delete(self, id): 
        # your code here 
studentDAO = StudentDAO()
