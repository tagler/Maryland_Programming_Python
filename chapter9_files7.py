import sys
import os

if len(sys.argv) == 3:
    file1 = sys.argv[1] 
    file1 = sys.argv[2] 
else:
    file1 = "text1.txt"
    file2 = "text2.txt"

list_names1 = []
list_names2 = []

with open(file1,'r') as f1:
    for line in f1:
        list_names1.append(line.strip())

with open(file2,'r') as f2:
    for line in f2:
        list_names2.append(line.strip())

print( [each_name for each_name in list_names1 if each_name in list_names2] )



 

        
        
