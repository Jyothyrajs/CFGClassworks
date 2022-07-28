# create class & Objects Examples
class Cat:

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print('Meow')

    def get_info(self):
        print(f'breed : {jake.breed} age: {jake.age} Friend: {jake.friend.name} and name : {jake.name} ')

    def birthday(self):
        self.age += 1

    def set_friend(self,friend):
        self.friend = friend
        friend.friend = self

# Create  objects
jake = Cat("Jake",1,'Persian')
# jake.get_info()
jake.meow()
tim = Cat("Tim",5,'Tabby')
# tim.get_info()
tim.birthday()
tim.set_friend(jake)
tim.get_info()
jake.get_info()


# Inheritance

class Vehicle:
    def vehicle_method(self):
        print("In Vehicle")

class Car(Vehicle):
    def car_method(self):
        print("from Car")

class Van(Vehicle):
    def van_method(self):
        print("from Van")

veh = Vehicle()
veh.vehicle_method()
van = Van()
van.van_method()

# Implement Multiple and Multilevel inheritance examples
class Camera:

    def camera_method(self):
        print("I can take photos")


class Radio:

    def radio_method(self):
        print("I can play Songs")


class MobilePhone(Camera, Radio):

    def cell_phone_method(self):
        print("I can take photos & play songs")


cell_phone_a = MobilePhone()
cell_phone_a.camera_method()
cell_phone_a.radio_method()

# Polymorphism
# Overloading

# Overriding
class Vehicle:
    def print_details(self):
        print("This is parent Vehicle class method")


class Car(Vehicle):
    def print_details(self):
        print("This is child Car class method")


class Cycle(Vehicle):
    def print_details(self):
        print("This is child Cycle class method")


car_a = Vehicle()
car_a. print_details()

car_b = Car()
car_b.print_details()

car_c = Cycle()
car_c.print_details()

# Method overloading

class Car:

   def start(self, a, b=None):
        if b is not None:
            print(a + b)
        else:
            print(a)

my_car = Car()
my_car.start(1)
my_car.start(1,2)


import abc


class Shape1(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return


class Triangle1(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        area = 3.24 * self.r * self.r

class Cylinder(Shape):
    def area(self):
        pass

"""
STATIC & CLASS METHODS
Class methods are used for factory purposes, in the below code @classmethod details() is used to create a class object from a birth year instead of age. 
Static methods are utility functions and work on data provided to them in arguments (NOTE: no 'self' passed in).
"""

from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def check_age(age):
        return age > 18


person1 = Person('Jenny', 20)

person2 = Person.details('Fatima', 1992)

print(person1.name, person1.age)
print(person2.name, person2.age)

print(Person.check_age(33))