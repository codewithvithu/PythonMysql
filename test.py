import mysql.connector

dbcon = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

if dbcon:
    print("Connected")
else:
    print("Connection Error")