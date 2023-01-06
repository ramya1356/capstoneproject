import re
import logging
class searchLog():
    def __init__(self):
        logging.basicConfig(filename="filelog8.txt",level=logging.INFO)
    def dearchLog(self,filename):
        file=open("filelog8.txt","r")
        str="ssssss.txt"
        data=re.compile(str)
        res=data.search(str)
        line=file.readline()
        print(res)
# if __name__=='__main__':
#     obj=searchLog()
#     obj.dearchLog("tttr.txt")
