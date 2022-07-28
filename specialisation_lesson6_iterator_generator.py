# ITERATOR - SUGGESTION run this demo / exercise in the console

nums = [2, 4, 1, 9, 6]

nums_iter = iter(nums)
print(nums_iter)

str = 'CFG is Cool'
lst = [1,2,3,4]
tple = (1,2,4,5)
dict = {1:"a",2:"b","c":"rt"}

str_iter = iter(str)
print(str_iter)
print(str_iter.__next__())
print(next(str_iter))

lst_iter = iter(lst)
print(lst_iter)

tple_iter = iter(tple)
print(tple_iter)

dict_iter = iter(dict)
print(dict_iter)
print(next(dict_iter))


print(next(nums_iter))


# what happens next when our list comes to an end?
# uncomment and try

print(next(nums_iter))


# ALTERNATIVELY  - traversing

nums_iter = iter({1, 2, 3, 4, 5})
print(nums_iter.__next__())


# this one will throw an error
print(nums_iter.__next__())

###########################
'''
The dir() function can be used to see the list of available methods on the iterable object.
'''
from pprint import pprint as pp

pp(dir(nums_iter))

pp(dir(lst))

pp(dir(str))

###########################


# Create our own ITERATOR

class EvenNumbers:

   def __init__(self):
       pass

   def __iter__(self):
       self.num = 0
       return self

   def __next__(self):
       next_num = self.num
       self.num += 2
       return self.num



# run code

evens = EvenNumbers()
even_iter = iter(evens)
print(even_iter)

print(next(even_iter))
print(next(even_iter))
print(next(even_iter))
print(next(even_iter))


# First example can dangerously run in infinite loop.
# Let's create a new object with an appropriate condition.

class EvenNumbers2:
    def __init__(self,size):
        self.size = size

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num < self.size*2  :
            self.next_num = self.num
            self.num += 2
            return self.num
        else:
            StopIteration

evens = EvenNumbers2(5)
even_iter = iter(evens)
for n in even_iter:
    print(n)

"""
Create a new CircleSequence class. 
It should accept an iterable, which represents our data source 
and a number, which tells us how many items should be produced.
For example 
c = CircleSequence('xyz', 5)
print(list(c))        # prints x, y, z, x, y
c2 = CircleSequence([1,2], 5)
print(list(c2))        # prints 1,2,1,2,1
"""


class CircleSequenceIterator:

    def __init__(self, data, limit):
        self.size = limit
        self.data = data
        self.index = 0

    # def __iter__(self):
    #     for i in self

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration
        else:
            self.value = self.data[self.index%len(self.data)]
            self.index = self.index+1
            return self.value

class CircleSequence:
   def __init__(self,data,limit):
       self.size = limit
       self.data = data


   def __iter__(self):
       return CircleSequenceIterator(self.data,self.size)

c = CircleSequence('xyz', 5)
print(list(c))

c2 = CircleSequence([1, 2], 10)
print(list(c2))


# GENERATOR

# A simple generator function
def my_gen():
   n = 1
   print("First element")
   yield n

   n += 1
   print("Second element")
   yield n

   n += 1
   print("Third element")
   yield n

g = my_gen()
next(g)
next(g)
next(g)

# this will throw an error
# next(g)


# GENERATOR EXPRESSION

my_list = [1, 3, 6, 10]

# NOTE: we square each term using list comprehension
new_list = [x ** 2 for x in my_list]

"""# NOTE: same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis () !"""

generator = (x ** 2 for x in my_list)

print(new_list)
print(generator)

# use next() or for loop to get items from generator
print(next(generator))

for i in generator:
    print(i)

###########################################

"""
Generators are easier to implement. 
Rule of thumb: iterators to create classes, generators to create functions. 
Compare example below. 
"""


# ITERATOR


class PowerThreeSequence:
    def __init__(self,max_):
        self.max_ = max_
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.max_:
            raise StopIteration
        else:
            result = 3**self.n
            self.n += 1
            return result

# GENERATOR

def power_three_sequence(max_items=0):
    n = 0
    while( n < max_items):
        yield 3**n
        n = n+1

#
my_iter = PowerThreeSequence(5)
for i in my_iter:
    print(i)
#
#
my_generator = power_three_sequence(5)
for i in my_generator:
    print(i)