
s = set()
l = list()

while True:
    num = input("input a number: ")
    if num == "end.":
        break
    if int(num) not in s:
        s.add( int(num) )
    else:
        l.append( int(num) )
    
print("set values:",s)
print("duplicates not added:",l)
print("number of duplicates:",len(l))
