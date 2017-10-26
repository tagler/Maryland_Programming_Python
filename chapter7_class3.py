
class Worker():

    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years
    def pension(self):
        return self.years*(0.1*self.salary)
    def name(self):
        return self.name

class Manager(Worker):

    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)
    def pension(self):
        return self.years*(0.2*self.salary)

class Executive(Manager):

    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)
    def pension(self):
        return self.years*(0.3*self.salary)


            
