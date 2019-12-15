#!/usr/bin/env python3
import os

from collections import Counter

filename=input("Enter the filename =>")

f= open(filename,"w")

read_data = input("Enter some texts to the file->")

f.write(read_data)

print("Filename is",os.path.basename(f.name))

location = os.getcwd()+'/'+f.name

print("The file location is",location)

file_stats=os.stat(filename)

print(file_stats)

print("The file size is in Bytes->",(file_stats.st_size))

f.close()

file = open(filename, "r", encoding="utf-8-sig")

wordcount = Counter(file.read().split())

print("Words\tCounter\n")
for item in wordcount.items():
    print("{}\t{}".format(*item))


