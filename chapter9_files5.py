
import sys
if len(sys.argv) == 3:
    in_file = sys.argv[1]
    out_file = sys.argv[2]
else:
    in_file = input("input filename: ")
    try:
        f = open(in_file, 'r')
    except OSError:
        print("input filename error")
        sys.exit()
    out_file = input("output filename: ")
    try:
        g = open(out_file, 'w')
    except OSError:
        print("output filename error")
        sys.exti()

while True:
    line = f.readline()
    if not line:
        break
    else:
        g.write(line)
f.close()
g.close()
