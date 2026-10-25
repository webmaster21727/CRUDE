import mysql.connector as data

db=data.connect( host="localhost", user="root",password="",database="data")
cursor=db.cursor()
cursor.execute("SELECT VERSION()")
d=cursor.fetchone()
print("version is %s"%d)
print(db)
#print(cursor)
db.close

