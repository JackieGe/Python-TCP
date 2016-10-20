import mysql.connector as mariadb

marriadb_connection = mariadb.connect(user='root', password='jackie', database='mysql')
cursor = marriadb_connection.cursor()
cursor.execute("select Db from db")

for Db in cursor:
    print Db
print ("Db name: {}".format(Db))

marriadb_connection.close()