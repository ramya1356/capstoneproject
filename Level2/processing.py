from time import perf_counter
import os
import multiprocessing as mp


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
if __name__=='__main__':
    d=input("drive name")
    s=input("enter search")
    p1=mp.Process(target=task1)
    p2=mp.Process(target=task2,args=(d,s))
    start_time = perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time=perf_counter()

    print(f'{end_time-start_time} seconds')