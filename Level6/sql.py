import sqlite3
connect=sqlite3.connect("c://sqlite//hcl.db")
cur=connect.cursor()
# cur.execute("select*from filelog")
# sql="""insert into filelog values(?,?);"""
# data=(100,"c://capstone//r1.txt")
# cur.execute(sql,data)
# connect.commit()
cur.execute("select * from filelog where id=100")
rows=cur.fetchall()
for r in rows:
    print(r)