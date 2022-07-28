
# Class Attribute and instance attribute

class Dog:
    # class attribute
    type = "Mammal"

    # Instance sttribute
    def __init__(self,name):
        self.name = name

    def get_name(self):
        print(f"My name is : {self.name}")

# Driver code
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Instance attributes
Rodger.get_name()
Tommy.get_name()

print("Rodger is {}".format(Rodger.__class__.type))
print("Tommy is {}".format(Tommy.__class__.type))

"""
Inheritance: Provides reusability of code
Inheritance is the capability of a class to derive or inherit the properties of another class. The class which derives the 
properties is called derived class and the class from which properties are derived is called base class
Single Inheritance : - Derive characteristics from a single class
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def get_details(self):
        print("I am {} of age {}".format(self.name,self.age))

class Employee(Person):
    def __init__(self,name,age,id,post):
        super(Employee, self).__init__(name,age)
        self.id = id
        self.title = post

    def get_details(self):
        super().get_details()
        print("I work as {} with ID number {} ".format(self.title,self.id))


p1 = Person("Jyothy",35)
e1 = Employee("Chris",30,102,"S/W Programmer")
p1.get_details()
e1.get_details()

"""
Multiple Inheritance & Multi level
"""
class Company:
    def __init__(self,name,location):
        self.company_name = name
        self.location = location

    def get_details(self):
        print("It is {} located in {}".format(self.company_name,self.location))

"""
Multiple inheritance
"""
class Company_Employee(Employee,Company):
    def __init__(self,name,age,id,post,company,location):
        Employee.__init__(self,name,age,id,post)
        Company.__init__(self,company,location)

    def get_details(self):
        Employee.get_details(self)
        Company.get_details(self)


ce = Company_Employee("Sundar Pichai",40,"G01","CEO","Google","USA")
ce.get_details()

# Polymorphism

p1 = Person("Jyothy",35)
p1.get_details()

e1 = Employee("Chris",30,102,"S/W Programmer")
e1.get_details()

"""
Abstract classes and methods
"""
from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_details(self):
        print("I am {} of age {}".format(self.name,self.age))

    @abstractmethod
    def add_pension(self,id,type):
        pass

    @abstractmethod
    def get_pension_details(self):
        pass

class Employee(Person):

    def __init__(self,name,age,id,post):
        super(Employee, self).__init__(name,age)
        self.id = id
        self.title = post

    def get_details(self):
        super().get_details()
        print("I work as {} with ID number {} ".format(self.title,self.id))

    def add_pension(self,type):
        self.pension_type = type

    def get_pension_details(self):
        return self.pension_type


emp1 = Employee("Chris",30,102,"S/W Programmer")
emp1.get_details()
emp1.add_pension("Service")
print(emp1.get_pension_details())

# TypeError: Can't instantiate abstract class Person with abstract methods add_pension, get_pension_details
p1 = Person("Jyothy",35)
p1.get_details()


# Static methods

class Book:
    __counter = 0

    def __init__(self,name,id):
        self.name = name
        self.id = id
        type(self).__counter += 1
        # Book.__counter += 1  # directly with class name


    @staticmethod
    def no_of_books():
        return Book.__counter


python = Book("Fundamentals of Python","001")
print(python.no_of_books())
print(Book.no_of_books())

python = Book("Fundamentals of SQL","002")
print(python.no_of_books())
print(Book.no_of_books())


# Class methods

class Pet:
    _class_info = " Pet Animals"

    @classmethod
    def about(cls):
        print("Class is about ",cls._class_info)

class Dog(Pet):
    _class_info = "Dogs"

class Cat(Pet):
    _class_info = "Cats"

Pet.about()
d = Dog()
d.about()
Cat.about()