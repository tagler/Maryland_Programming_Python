
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
