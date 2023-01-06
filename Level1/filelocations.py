import os
from time import perf_counter
def drive_search(drive):
    c=0
    s=input("enter search")
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
start_time=perf_counter()
d=input("drive name")
drive_search(d)
end_time=perf_counter()
print(f'{end_time-start_time} seconds taken')
