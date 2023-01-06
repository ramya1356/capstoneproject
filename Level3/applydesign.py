import os
class Drive:
    def __init__(self):
        pass
    def find(self):
        o=os.popen("fsutil fsinfo drives").read()
        print(o)
        return o

        #print(os.system('cmd /c "wmic logicaldisk list brief"'))
if __name__ == '__main__':
        obj = Drive()
        obj.find()