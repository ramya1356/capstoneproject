import os
class SystemDriveFinder:
    def __init__(self):
        pass
    def find_drives(self):
        drives=[]
        for x in range(65,91):
            if os.path.exists(chr(x)+":"):
                drives.append(chr(x))
        return drives[0]
if __name__=='__main__':
    obj=SystemDriveFinder()
    print(obj.find_drives())