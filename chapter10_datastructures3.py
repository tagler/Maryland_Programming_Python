
list_lists = []
with open("data.txt",'r') as f:
    for line in f:
        data_list = line.split()
        list_lists.append( data_list )

d = {}
for each_line in list_lists:
    n = each_line[0]
    c = each_line[1]
    p = int( each_line[2] )
    if n not in d:
        d[n] = {c : p}
    else:
        if c not in d[n]:
            d[n][c] = p
        else:
            d[n][c] += p

print(d,"\n")

for person in d:
    for tech in d[person]:
        print(person, tech, d[person][tech])







        
