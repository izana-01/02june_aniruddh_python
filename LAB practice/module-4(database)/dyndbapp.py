import sqlite3 

try:
    dbcon=sqlite3.connect("tempdb.db")
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
i = int(input("Enter number of students to insert: "))
for j in range(i):
     name = input("Enter student name: ")
     city = input("Enter student city: ")
     tbl_insert = "insert into studinfo(name,city) values (?,?)"
     try:
        dbcon.execute(tbl_insert, (name, city))
        dbcon.commit()
        print("Data inserted successfully")
     except Exception as e:
        print(e)
        break

#delete table
d= int(input("Enter ID of student to delete: "))
tbl_delete=f"delete from studinfo where id={d}"
try:
    dbcon.execute(tbl_delete)
    dbcon.commit()
    print("Data deleted successfully")
except Exception as e:
    print(e)

"""tbl_insert="insert into studinfo(name,city) values (?,?) " 
try:
    dbcon.execute(tbl_insert)
    dbcon.commit()
    print("Data inserted successfully")
except Exception as e:
    print(e)"""