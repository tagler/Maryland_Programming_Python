
import sys
if len(sys.argv)>1:
    files = sys.argv[1:]
else:
    files = ['text1.txt','text2.txt']

for file in files:
    f = open(file,'r')
    print("***",file,"***")
    number_lines = 0
    number_chars = 0
    number_words = 0
    for line in f:
        number_lines += 1
        number_chars += len(line)
        number_words += len(line.strip().split())
    print("\ntotal lines:", number_lines)
    print("total characters:", number_chars)
    print("total words: ", number_words)
    print("\n")
    f.close()

    
