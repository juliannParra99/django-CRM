# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

# Import the required module for working with MySQL
import mysql.connector

# Establish a connection to the MySQL server
dataBase = mysql.connector.connect(
    host='localhost',  # Hostname of the MySQL server
    user='root',       # Username for database access
    passwd='123456789river'  # Password for the user
)

# Prepare a cursor object to interact with the database
cursorObject = dataBase.cursor()

# Create a new database named 'elderco'
cursorObject.execute("CREATE DATABASE elderco")

# Commit the changes to the database
dataBase.commit()

# Print a message indicating the successful completion: para ver la ejecucion de este archivo ejecutar en la terminal:  python mydb.py
print("All Done!")


##Este archivo es solo para crear la base de datos  con el objeto: cursorObject en este caso, pero una vez creado ya no es necesario. Esto tambien se peude crear desde los comandos proporcionados por la base de datos etc. 