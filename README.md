# Web Services and Applications Project
## By Joanne Feeney
### May 2024
************************************

In this reposotiry, I have two folders:
- requirements
- python scripts

The requirements folder contains all the requirements to run the scripts (it may also contain extra requirements that
are not required however, happen to be installed on my PC)


The python scripts folder contains all the programs I have written for this project.

Within this folder there is another folder called "staticpages" which contains my interface html file and my ajax javascript file.

*************************************

## Description
For this python project, I have created an application that provides an online user interface to perform CRUD operations on a database of fruits. This includes:

1. A Flask server that provides the RESTful API
2. A web page that allows the user to interact with that RESTful API

I did not get time to add move this web page to pythonanywhere so it can only be accessed from a local host (http://127.0.0.1:5000)
by running sql and by running "python .\flask_server.py" on your local machine. To connect to the sql database, I have a hidden config folder containing
the password required to gain access to the wsaa database & hte fruits table.

I currently (as of 19/05/2024) have three active URLs:
- http://127.0.0.1:5000
- http://127.0.0.1:5000/fruits
- http://127.0.0.1:5000/fruit_interface.html

The fruit_interface.html is currently working for updating & deleting the table on this page however other CRUD functions are not working and it does not 
appear to be connected properly to my sql database whereas /fruits is. I am hoping to figure this out by the deadline tomorrow.

