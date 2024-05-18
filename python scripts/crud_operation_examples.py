# Examples of CRUD operation on MySql

# Connect to MySql database
import mysql.connector 

db = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="", 
    database="wsaa" 
) 

# Insert data
cursor = db.cursor() 
sql="insert into student (name, age) values (%s,%s)" 
values = ("Mary",21) 

cursor.execute(sql, values) 

db.commit() 
print("1 record inserted, ID:", cursor.lastrowid) 
mycursor.close() 
connection.close()

# View data
cursor = db.cursor() 
sql="select * from student where id = %s" 
values = (1,) 

cursor.execute(sql, values) 
result = cursor.fetchall() 
for x in result: 
    print(x) 
mycursor.close() 
connection.close()

# Update data
cursor = db.cursor() 
sql="update student set name= %s, age=%s where id = %s" 
values = ("Joe",33, 1) 

cursor.execute(sql, values) 

db.commit() 
print("update done") 
mycursor.close() 
connection.close()

# Delete data
cursor = db.cursor() 
sql="delete from student where id = %s" 
values = (1,) 

cursor.execute(sql, values) 

db.commit() 
print("delete done") 
mycursor.close() 
connection.close()
