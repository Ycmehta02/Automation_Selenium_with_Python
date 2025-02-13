#insert, update, delete, select

insert_q = "insert into student values(104,'XYZ')"
update_q = "update student set sname='Mary' where sid=104;"
delete_q = "delete from student where sid=104"
select_q = "select * from student"

import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", password="root", database="mydb")
    cur = con.cursor()  # thorugh cursor the operations will be performed on DB
    cur.execute(insert_q)  # query execution with cursor
    # cur.execute(update_q)
    # cur.execute(delete_q)
    # cur.execute(select_q)
    con.commit()  # commit transaction
    con.close()
except:
    print("Connection unsuccessful")

print("Done")
