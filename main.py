import mysql.connector


conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "passworDmax15$",
    database = "webscraping_db"
)
cursor = conn.cursor()


#=========================== LOAD DATA FROM MYSQL==========================
old_data = {}

query = "SELECT * FROM bbc"

cursor.execute(query)
result = cursor.fetchall()
for row in result:
    title = row[0]
    detail_link = row[2]
    old_data[detail_link] = title