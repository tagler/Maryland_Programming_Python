import sys
import os
import time

if len(sys.argv) == 3:
    files_in_dir = os.listdir( sys.argv[1] )
    size_limit = sys.argv[2]
else:
    size_limit = 500
    files_in_dir = os.listdir()

for file in files_in_dir:
    if os.path.getsize(file) > size_limit:
        print("filename: ",file)
        print("size: ", os.path.getsize(file))
        print("last modification date: ", time.ctime(os.path.getctime(file)),"\n" )
