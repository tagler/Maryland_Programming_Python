
class Person():
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def __str__(self):
        return("Person Name: " + self.name +
               "\nAge: " + str(self.age) +
               "\nGender: " + self.gender)
    
