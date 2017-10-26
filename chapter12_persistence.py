# *** dbm ***
import dbm
a = "string"
# export
with dbm.open("filename.txt","c") as file1:
    file1['number 1'] = a
# import
with dbm.open("filename.txt","r") as file2:
    value = file2['number 1']

# *** pickle ***
import pickle
a = 100
b = 200
# export
with open("filename2.txt","wb") as file1:
    pickle.dump(a,file1)
    pickle.dump(b,file1)
# import
with open("filename2.txt","rb") as file2:
    value2 = pickle.load(file2)
    value3 = pickle.load(file2)

# *** shelve ***
import shelve
a = {'100' : '1000'}
b = {'200' : '2000'}
c = {'300' : '3000'}
# export
with shelve.open("filename3.txt") as file1:
    file1['first'] = a
    file1['second'] = b
    file1['third'] = c
# import
with shelve.open("filename3.txt") as file2:
    value4 = file2['second']
    value5 = file2['third']

    
