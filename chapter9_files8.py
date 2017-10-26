import sys

if len(sys.argv) > 1:
    files = sys.argv[1:] 
else:
    files = ["text1.txt", "text2.txt"]

names_list = []
for each_file in files:
    with open(each_file,'r') as f:
        names_in_file = []
        for line in f:
            names_in_file.append( line.strip() )
        names_list.append( names_in_file)

names_dict = {}
for each_file in names_list:
    for each_name in each_file:
        if each_name in names_dict:
            names_dict[each_name] += 1
        else:
            names_dict[each_name] = 1

dict_ordered = sorted(names_dict.keys())
for each in dict_ordered:
    print(each,"\t",names_dict[each])


 

        
        
