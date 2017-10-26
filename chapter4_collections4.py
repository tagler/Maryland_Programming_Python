import string

s = set()
d = dict()

while True:
    data = input("enter a line (q to quit): ")
    if data == 'q':
        break
    for p in string.punctuation:
        if p in data:
            data = data.replace(p,' ')
    words = data.strip().lower().split()
    for each in words:
        if each in d:
            d[each] = d[each] + 1
        else:
            d[each] = 1

print( "dictionary: ", d)
print( "sorted by words: ",
       sorted(d.items(), key=lambda x:x[0], reverse=False) )
print( "sorted by counts (big to small): ",
       sorted(d.items(), key=lambda x:x[1], reverse=True) )
