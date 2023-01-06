import logging
import os
class Filelog():
    def __init__(self):
        logging.basicConfig(filename="stylelog1.txt",level=logging.WARNING)
    def find(self):
        try:
            f=open("r1.txt","r")
        except FileNotFoundError as msg:
            logging.exception(msg)

if __name__=='__main__':
    obj=Filelog()
    obj.find()
