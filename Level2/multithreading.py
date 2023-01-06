import threading 
from time import perf_counter
import os



def task1():
    print(os.popen("fsutil fsinfo drives").read())
    print(os.system('cmd /c "wmic logicaldisk list brief"'))


def task2(drive,s):
    c=0

    for root, dir, files in os.walk(drive):
        for name in files:
            filepath=os.path.join(root,name)
            if s in name:
                c=c+1
                print(filepath)
    if c==0:
        print("file not found")
    else:
        print(f"{c}files.")



d=input("drive name")
s=input("enter search")
start_time=perf_counter()
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2,args=(d,s,))
t1.start()
t2.start()
t1.join()
t2.join()
end_time=perf_counter()

print(f'{end_time-start_time} seconds')
