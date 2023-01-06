import sqlite3
class SearchDB():
    def __init__(self):
        pass
    def searcDB(self,filename):
        self.connect = sqlite3.connect("c://sqlite//hcl.db")
        self.cur = self.connect.cursor()
        sql="""select * from filelog where filename=?;"""
        args=(filename,)
        self.cur.execute(sql,args)
        row=self.cur.fetchone()
        print(row)
if __name__=='__main__':
    obj=SearchDB()
    obj.searcDB(input())  #obj.searcDB('c://capstone//r1.txt')