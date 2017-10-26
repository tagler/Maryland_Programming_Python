
def add_to_dict(number,dic):
    for each in dic:
        dic[each] = dic[each]+1
    return dic

number = 1
dic = {'a':1,'b':2,'c':3}
print( add_to_dict(number,dic) )
