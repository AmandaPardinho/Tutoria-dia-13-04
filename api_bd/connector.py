import mysql.connector

bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "amanda03",
    database = "ecommerce"
)

cursor = bd.cursor()