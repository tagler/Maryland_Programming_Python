def outside1():
    def add(a,b):
        return a+b
    return add

def outside2(a,b):
    def add():
        return a+b
    return add()

def outside3():
    return lambda a,b : a+b


f = outside1()
f(1,3)

outside2(1,3)

g = outside3()
g(1,3)
