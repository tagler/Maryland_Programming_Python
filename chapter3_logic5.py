s = input("input multiple numbers as a string: ")
l = s.split()
print(l)
x = 0
while x < len(l):
    if float( l[x] ) > 0:
        print(l[x],"is greater than 0")
    x += 1

    

    
