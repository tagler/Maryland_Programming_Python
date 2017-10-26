
import sys
if len(sys.argv) == 3:
    in_file = sys.argv[1]
    out_file = sys.argv[2]
else:
    in_file = input("input filename: ")
    out_file = input("output filename: ")

f = open(in_file, 'r')
g = open(out_file, 'w')

while True:
    line = f.readline()
    if not line:
        break
    else:
        g.write(line)
f.close()
g.close()
