
class Person():
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def __str__(self):
        return("Person Name: " + self.name +
               "\nAge: " + str(self.age) +
               "\nGender: " + self.gender + "\n")


class Family():

    def __init__(self, mother, father, *kids):
        self.mother = mother
        self.father = father
        self.kids = kids
        
    def __str__(self):
        all_family = []
        all_family.append(self.mother)
        all_family.append(self.father)
        for each_kid in self.kids:
            all_family.append(each_kid)
        all_family_string = ''
        for each in all_family:
            temp = ("Person Name: " + each.name +
                    "\nAge: " + str(each.age) +
                    "\nGender: " + each.gender + "\n")
            all_family_string += temp
        return all_family_string

    def __eq__(self,other):
        return len(self.kids) == len(other.kids)

    def __lt__(self,other):
        return len(self.kids) < len(other.kids)

    def __gt__(self,other):
        return len(self.kids) > len(other.kids)
    
    def add(self, new_kid):
        all_kids = []
        for each_kid in self.kids:
            all_kids.append(each_kid)
        all_kids.append(new_kid)
        self.kids = all_kids 

#####################################################################

mother = Person("Mom", 45, "F")
father = Person("Dad", 45, "M")
kid1 = Person("Johnie", 2, "M")
kid2 = Person("Janie", 3, "F")
print(kid2)

myFamily = Family(mother, father, kid1, kid2)
print(myFamily)

kid3 = Person("Paulie", 1, "M")
myFamily.add(kid3) 
print(myFamily)

smiths = Family(mother, father, kid1)
print(smiths)
if (myFamily > smiths):
    print("we have more kids than smiths")
if (myFamily == smiths):
    print("families have the same number of kids")
if (myFamily < smiths):
    print("we have fewer kids than smiths")
          






            
