
import sys
if len(sys.argv)>1:
        if sys.argv[1] == "-t":
            files = sys.argv[2:]
        else:
            files = sys.argv[1:]
else:
    files = ['text1.txt','text2.txt']

total_lines = 0
total_chars = 0
total_words = 0
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
    f.close()
    total_lines += number_lines
    total_chars += number_chars
    total_words += number_words
    
print("\ntotal lines:", total_lines)
print("total characters:", total_chars)
print("total words: ", total_words)
print("\n")
    
