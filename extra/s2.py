'''import os
dir='c:\\group1 capstoneproject\\'
d1={}
for root,dirs,files in os.walk(dir):
    for dir in dirs:
        d1[dir]=os.listdir(root+"/"+dir)
print(d1)'''
import multiprocessing as mp
print("no of processors:",mp.cpu_count())