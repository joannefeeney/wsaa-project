# File for app functions

# returns all the books in the database table 
def getall(): 
    return [{}] 

# returns one book 
def findById(id): 
    return {} 

# inserts a book into the database 
def create(book): 
    return book 

# updates the book 
def update(id, book): 
    return book 

# deletes the book with the id 
def delete(id): 
    return True


# Testing MySql_Connector file
from zstudentDAO import studentDAO 

#create 
latestid = studentDAO.create(('mark', 45)) 
# find by id 
result = studentDAO.findByID(latestid); 
print (result) 
#update 
studentDAO.update(('Fred',21,latestid)) 
result = studentDAO.findByID(latestid); 
print (result) 
# get all 
allStudents = studentDAO.getAll() 
for student in allStudents: 
    print(student) 
# delete 
studentDAO.delete(latestid)