# Create Connection

# Start by creating a connection to the database.

# Use the username and password from your MySQL database:
import mysql.connector as cx

def credentials():
    mydb= cx.connect(
        host="localhost",
                      user="root",  
                          password="Oindi001**")
    
    mycusor= mydb.cursor()
    
    return mycusor,mydb






