a = int( input("number 1: ") )
b = int( input("number 2: ") )

if a != b:
    result = 0
    for x in range(min(a,b),max(a,b)+1):
        result += x
    print(result)
else:
    print(a)
    
