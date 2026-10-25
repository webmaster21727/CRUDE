import mysql.connector as data
try:
    data= data.connect(host="localhost",user="root",password="",database="data")
    cursor=data.cursor()
    sql="INSERT INTO sss (id,name,mo) VALUES(5,'xyz',111111)"     
    cursor.execute(sql)
    a=data.commit()         
    data.rollback() 
    if cursor.rowcount >0:
        print("data is inserted ")
    else:
        print("data is not valid ")  
    
except Exception as e:
    print("error is happende",e)
finally:
    cursor.close()
    data.close()
     
