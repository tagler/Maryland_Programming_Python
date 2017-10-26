s = input("string: ")

print("does it end in a period? ", s[-1] == ".")
print("does it contain all alpha characters? ", s.isalpha() )
print("does it contain a 'x'? ", (s.find("x")) != -1 )
print("replace e with E: ", s.replace("e", "E"))
