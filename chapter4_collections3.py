import string

s = set()

while True:
    data = input("enter a line (q to quit): ")
    if data == 'q':
        break
    for p in string.punctuation:
        if p in data:
            data = data.replace(p,' ')
    words = data.strip().lower().split()
    for each in words:
        if each not in s:
            s.add(each)
    
print( sorted(s) )
print( len(s) )
