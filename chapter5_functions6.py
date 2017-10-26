def sort(l):
    new = []
    lcopy = l[:]
    while len(new) != len(l):
        lcopy2 = lcopy[:]
        for each in lcopy2:
            if each == max(lcopy2):
                new.append(each)
                lcopy.remove(each)
                break
    return new  

def reverse(l):
    new = []
    lcopy = l[:]
    while len(new) != len(l):
        lcopy2 = lcopy[:]
        for each in lcopy2:
            if each == min(lcopy2):
                new.append(each)
                lcopy.remove(each)
                break
    return new  

values = [10,40,30,20,5]
print(values)
print(sort(values))
print(reverse(values))
print(reverse(sort(values)))
print(values)
