import sqlite3 

try:
    dbcon=sqlite3.connect("temp.db")
    print("Database connection successful")
except Exception as e:
    print(e)

#table create
tbl_create="create table studinfo(id integer primary key autoincrement,name text,city text)"

try:
    dbcon.execute(tbl_create)
    print("Table created successfully")
except Exception as e:
    print(e)

#table insert

tbl_insert="insert into studinfo(name,city) values ('aniruddh' ,'vadodara') , ('shyam','ahmedabad') , ('yashita','delhi');"

try:
    dbcon.execute(tbl_insert)
    dbcon.commit()
    print("Data inserted successfully") 
except Exception as e:
    print(e)

#update table
tbl_update="update studinfo set  name='shyam' , city='surat' where id=2"
try:    
    dbcon.execute(tbl_update)
    dbcon.commit()
    print("Data updated successfully")
except Exception as e:
    print(e)

#delete table
tbl_delete="delete from studinfo where id=2"
try:
    dbcon.execute(tbl_delete)
    dbcon.commit()
    print("Data deleted successfully")
except Exception as e:
    print(e)