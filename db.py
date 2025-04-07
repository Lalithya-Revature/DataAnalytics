# import mysql.connector
# conn=mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="root",
#     database="DataRevature"
    
# )
# cursor=conn.cursor()
# cursor.execute("select * from employee")
# for row in cursor:
#     print(row)
# conn.close()

import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

print(myDB)
