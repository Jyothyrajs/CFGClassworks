
"""
Decorator --
- starts with @name-of-decorator
"""

"""
1. Pass function as argument to another object
Demo example
"""
def add_one(x):
    return x+1

def sub_one(x):
    return x-1

def operate(func,x):
    return func(x)

print(operate(add_one,3))
print(operate(sub_one,3))

"""
2. A Function can return another function
Demo example
"""
def outer_func():

    def inner_func():
        print("Hello S/W 5 Team")

    return inner_func # without () Does not execute or call it

print(outer_func())
ex_func = outer_func()
ex_func()


# More example

def pet_owner(num):
    def first_pet():
        return "Hi I am German Shepherd"

    def second_pet():
        return "Hello, I am a Rottweiller"

    def third_pet():
        return " I am a puppy"

    if num == 1:
        return first_pet
    elif num == 2:
        return second_pet
    else:
        return third_pet

first = pet_owner(1)
sec = pet_owner(2)
third = pet_owner(3)

print(first)
print(sec)
print(third)

print(first())
print(sec())
print(third())

"""
3. A decorator takes in a function, adds some functionality and returns it
"""
def enhancer(func):

    def inner_wrapper():
        print("Before func called ")
        func()
        print("After func call")

    return inner_wrapper

def simple_func():
    print("I am a function")

decorated = enhancer(simple_func)
print(decorated)
decorated()


def enhancer(func,x):

    def inner_wrapper():
        print("Before func called ")
        print(func(x))
        print("After func call")

    return inner_wrapper

def add_one(x):
    return x+1

decorated = enhancer(add_one,2)
print(decorated)
decorated()

# Special syntactical sugar for decorator


def enhancer(func):
    def inner_func(x):
        print("Inner function")
        func(x)  #Doesn't return anything
        return func(x) #Returns the value as in the function definition
    print("It is a decorator function")
    return inner_func

@enhancer
def simple_func2(x):
    print(f"I am a function with value {x}")
    return 2*x


print(simple_func2(5))

# Decorator function with arguments

def divide(a,b):
    return (a/b)

def clever_divide(func):
    def inner_wrapper(a,b):
        print("Lets divide ",a," by ",b)
        if b== 0:
            print("Cannot divide by zero")
            return
        return func(a,b)
    return inner_wrapper

@clever_divide
def divide(a,b):
    return (a/b)

print(divide(22,3))
print(divide(22,0))


## 3. Make general decorators that work with any number of parameters.

## EXAMPLE
def universal_decorator(func):
    def inner_wrapper(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner_wrapper

@universal_decorator
def my_args(*a):
    return len(a)

print(my_args(2,3,4))
print(my_args(2,4))

# Exercise - Write a Run twice decorator
def run_twice_fun(func):
    def inner_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return inner_wrapper

@run_twice_fun
def divide_3x(a,b,c):
    print(a/b/c)

print(divide_3x(2,4,5))
print(divide_3x(4,7,5))

@run_twice_fun
def divide(a,b):
    print(a/b)

print(divide(3,2))


##########################################################################

## Chain decorators together ###

def equal_sign(func):
    def inner(*args, **kwargs):
        print("=" * 30)
        func(*args, **kwargs)
        print("=" * 30)
    return inner


def pipe_sign(func):
    def inner(*args, **kwargs):
        print("|" * 30)
        func(*args, **kwargs)
        print("|" * 30)
    return inner

@equal_sign
@pipe_sign
def display_msg(msg):
    print(msg)


display_msg("Welcome decorator")

# Exercise- Class decorator to square the result of a function

class SquareDeco():
    def __init__(self,simple_function):
        self.function = simple_function

    def __call__(self,*args,**kwargs):
        result = self.function(*args,**kwargs)
        return result * result

@SquareDeco
def multiply(a,b):
    print("Multiplying")
    return a * b

print(multiply(20,3))

# Exxercises
# Create a Timer decorator
# Create a memorize decorator

