import pymysql

try:
    db=pymysql.connect(host='localhost', user="root", password="", database="abpy")
    print("Database connection successful")
except Exception as e:
    print(e)