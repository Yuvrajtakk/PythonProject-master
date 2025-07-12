def add(*args):
    print(args)  #(10, 20, 30, 50, 70)
    print(type(args))  #<class 'tuple'>
    print(args[0]) #10
    sum = 0
    for n in args:
        sum += n
    return sum

def calculator(n, **kwargs):
    print(kwargs)  #{'add': 5, 'multiply': 10}
    print(type(kwargs))  #<class 'dict'>
    print(kwargs["add"]) #5
    for key, value in kwargs.items():
        print(key)
        print(value)
        # add
        # 5
        # multiply
        # 10
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n) #100



print(add(10, 20, 30, 50 , 70)) #180
calculator(5,add = 5, multiply = 10)

class Car:
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]

# my_car =Car(make= "Nissan") - key error 'model'
my_car =Car(make= "Nissan", model= "GT-R")
print(my_car.model) #GT-R

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car =Car(make= "Nissan")
print(my_car.make) #Nissan

