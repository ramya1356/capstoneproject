import os
import threading
from searcheng1db import Search1DB

class FileSearcher(threading.Thread):

    def __init__(self):
        self.s=""
        pass
    def task2(self,drive,s):
        try:
            c = 0
            for root, dir, files in os.walk(drive):
                for name in files:
                    filepath = os.path.join(root, name)
                    if s in name:
                        c = c + 1
                        return filepath
            if c == 0:
                print("file not found")
            else:
                print(f"{c}files.")

        except:
            print("no error")
    def run(self):
        pass
if __name__ == '__main__':

    drive,file=input("drivename"),input("file name")
    obj = FileSearcher()

    dbobj=Search1DB()
    res=dbobj.searcDB(file)
    if res==0:
        data=obj.task2(drive,file)
        print(data)
        dbobj.insertDB(data)
    else:
        print(res)

