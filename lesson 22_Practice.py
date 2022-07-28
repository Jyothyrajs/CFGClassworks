

def myfunc(a,b):
 return a+b

res = map(myfunc,(1,2,3),(3,4))
print(res)


# Exercise 1
def triple(num):
 return (num*3) + 3

print(triple(3))

# Exercise 1- Using lambda
triple2 = lambda num:(num*3) + 3
triple3 = lambda n,m:n+m
print(triple2(3))
print(triple3(6,3))

print(triple2)
print(triple2(4))


# Exercise 2
def add_five(number):
  return number+5


my_list = [1,2,3]

new_list = list(map(add_five,my_list))
print(new_list)

# with lambda
print(list(map(lambda number:number+5,[1,2,3])))


# Exercise 3
my_list = [1,2,3]
print(map(lambda number:number+5,my_list))

print(set(map(lambda number:number+5,my_list)))

print(list(map(lambda number:number+5,my_list)))

# Exercise 3 - Filter
numbers = [1,2,3,5,29,34,12,8,5]
print( numbers)

def gtfive(number):
  if numbers>5:
    return True
  else:
   return False

def gtfive(number):
 return number > 5

res = list(filter(gtfive,numbers))
print(res)

print(list(filter (lambda number:number < 5,numbers)))
print(list(filter (lambda number:number == 5,numbers)))
print(list(filter(lambda num:num%3,my_list)))

# Exercise 4 - Reduce - faster than external for loop
from functools import reduce

numbers = [1,2,3,5]
print(numbers)

def sum(a,b):
 return a+b

print(reduce(sum,numbers))

print(reduce(lambda a,b:a+b,numbers))

print(reduce(lambda a,b:a*b,numbers))

print(list(map(lambda a:a+5,numbers)))


"""
Simply a useful example to know.

Task:
Search through a list of dictionaries to find the only one
dictionary that you need by value.

Let's say we need to find some info on a specific CFG student.
Out data structure is as follows: every student is represented as a dictionary
and all dictionaries are held in a list.
We need to find one student by her name.
"""

students = [
    {'name': "Jane", 'age': 43, 'specialisation': 'Software'},
    {'name': "Priya", 'age': 24, 'specialisation': 'Data'},
    {'name': "Diana", 'age': 18, 'specialisation': 'Data'}
]

# get info for a student called 'Priya' ( a search criteria can be anything:
# an ID, a name, name and surname together and many more)

print(list(filter(lambda students:students['name']=='Priya' ,students)))
print(list(filter(lambda name: name ['name'] == 'Priya', students)))

#Exercise 5 - Regular expressions {2} exactly 2 times
# {2,7} 2 to 7 times
import re

my_str = 'Jyothy'
regex= '[^abc]'
matches = re.match(regex,my_str)
print(matches)

my_str = 'Nano degree is fun'
regex= 'Nano\s\w+\s'
matches = re.match(regex,my_str)
print(matches)

regex= 'Nano\s\w+\s\w+'
matches = re.match(regex,my_str)
print(matches)


# o/p: is fun
my_str = 'Nano degree is fun'
regex1= 'is\sfun'
regex2= '[^Nano\s]'
matches = re.match(regex1,my_str)
print(matches)
matches = re.match(regex2,my_str)
print(matches)

my_str = 'Nano degree is fun'
regex1= 'is\sfun'
regex2= '[^Nano\s\w\s]'
matches = re.search(regex1,my_str)
print(matches)
my_str = 'Nano degree is fun'
matches = re.match(regex1,my_str)
print(matches)
my_str = 'Nano degree is fun'
matches = re.search(regex2,my_str)
print(matches)

my_str = "Software and Data Science 777 are fun Science 898 is another fun"
regex = "Sci[\w\s]+\d+"
for matched in re.finditer(regex,my_str):
  print(matched)
  print(matched.group())
  print(matched.span())


my_str = "Software and Data Science 777 are fun Science 898 is another fun"
regex = "fun"
for matched in re.finditer(regex,my_str):
  print(matched)
  print(matched.group())
  print(matched.span())

my_str = "Software and Data Science 777 are fun Science 898 is another fun"
regex = "Data\s\w+\s"
for matched in re.finditer(regex,my_str):
  print(matched)
  print(matched.group())
  print(matched.span())

my_str = "Software and Data Science 777 are fun Science 898 is another fun"
regex = "and\s\w+\s."
for matched in re.finditer(regex,my_str):
  print(matched)
  print(matched.group())
  print(matched.span())

my_str = "Software and Data Science 777 are fun Science 898 is another fun"
regex = "and\s\w+\s."
matched =  re.sub(regex,my_str,'SQL')
print(matched)

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."
regex = "data\s(\w+\s)"
for matched in re.findall(regex,my_str):
 print(matched)


my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."
regex = "(\w+)?\sdata\s(\w+\s)"
for matched in re.findall(regex,my_str):
 print(matched)








list = ['hello','Jyothy','Hi123']

regex= '*[^abc]'
matches = re.match(regex,list)