#OOPS
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print("woof")
dog1 = Dog("buddy",3)
dog2 = Dog ("Max",5)
print(dog1.name)
print(dog2.age)

dog1.bark()

print("------------------------------")
#Inheritance and super function
class servicedog(Dog):
    def __init__(self,name,age,service):
        super().__init__(name,age)
        self.service = service

    def perform_service(self):
        prin(f"{self.name} is performing {self.service} service")

dog1 = servicedog("Buddy",3,"bath")
dog2 = servicedog("max",5,"grooming")
print(dog2.service)

class Example:
    def __init__(self,data):
        self.__data = data
    def get_data(self):
        return self.__data

    def set_data(self,value):
        self.__data = value

obj = Example(100)
print(obj.get_data())
obj.set_data(200)
print(obj.get_data())

print("------------------------------")
class cat:
    def make_sound(self):
        print("Meow")
class Duck:
    def make_sound(self):
        print('quack')
def make_animal_sound(animal):
    animal.make_sound()
cat1 = cat()
duck1 = Duck()
make_animal_sound(cat1)
make_animal_sound(duck1)
print("================Exceptional handling======================")
try:
    x= 1/0
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Please assign value")
finally:
    print("Code completed")

print("================Exceptional handling======================")


import logging
logging.basicConfig((filename='exaple.log',level=logging.DEBUG,format='%(asctime)s%(levelname)s%(message)s'))
def add(x,y):
    logging.info(f"Adding (x) and (y)")
    return x+y
def subtract(x,y):
    logging.info(f"subtracting (x) and (y)")
    return x-y
import logging
def divide(x,y):
    logging.info(f"Dividing {x} and {y}")
    try:
        return x/y
    except ZeroDivisionError as ex:
        logging.error(f"Error occured :{ex}")
        return None
a = 10
b = 0
c = add(a,b)
d= subtract(a,b)
e = divide(a,b) 
logging.debug((f"c={c}, d={d},e={e}"))

import pdb
def fun():
    x = 1%1
    return x
pdb.set_trace()
res = fun()
print(res)

