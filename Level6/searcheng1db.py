import sqlite3

class Search1DB():
    def __init__(self):
        self.connect = sqlite3.connect("c://sqlite//hcl.db")
        self.cur = self.connect.cursor()
    def searcDB(self,fil):
        self.f="filename"
        sql="""select * from filelog1 where filename like'%{0}'""".format(fil,)
        self.cur.execute(sql)
        row=self.cur.fetchone()
        if row==None:
            return 0
        else:
            return row
    def insertDB(self,filename):
        sql="""insert into filelog1(filename) values(?);"""
        data=(filename,)
        self.cur.execute(sql,data)
        self.connect.commit()
        return "record added"
if __name__=='__main__':
    dbObj=Search1DB()
    print(dbObj.connect)
    print(dbObj.cur)