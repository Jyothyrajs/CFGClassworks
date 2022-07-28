from functools import reduce

add_two_nums = lambda x,y: x+y
res = add_two_nums(3,4)
print(res)

"""
Lambda function is an anonymous function without a name. In python, lambda function is created with the keyword lamda.
Lambda construction consists of keyword lambda, a bound variable and body
Lambda is known as immediately invoked function expression

Characteristics:
It can only contain expressions and can't include statements in its body
It isa written as single line of expression
It does not support type annotations
It can be immediately invoked(IIFE)

Syntax: lambda <parameter_list> : <expression>

bound variable: is an argument to function
Eg: lambda x: x + 1

(lambda x: x + 1)(2)  --- > 3


lambda function is an expression, so it can be named

add_one = lambda x: x + 1
add_one(3)
-- no paranthesis around the arguments
-- multi arguments are represtented as list separated by comma

"""


# Immediately Invoked Function Expression - IIFE
add_two_nums = (lambda x,y: x+y)(6,7)
print(add_two_nums)

full_name = lambda f_name,l_name : f"Full name : {f_name.title()} {l_name.title()}"
print(full_name("jyothy","sanish"))

# Map function
"""
Map applies a function to all items in the list. Instead of passing each element to function and collecting result,
 with map we can apply the function to each element in the list
 map( function_to_apply, list_of_inputs)
"""

# With normal function
def to_square(x):
    return x*x

my_list = [x for x in range(10,29)]
sq_list = []
for i in my_list:
    if to_square(i) :
        sq_list.append(i)
print(sq_list)

""" 
With map 
# map(function_to_apply, list_of_inputs)  
"""


def to_square(x):
    return x*x

my_list = [x for x in range(10,29)]
sq_list = list(map( to_square,my_list))
print(sq_list)



# even =( lambda x :  x%2 and 'odd' or 'even')(6)
# print(even)
sq_list = list(map(lambda x: x*x, my_list))
print(sq_list)

"""
Filter: Create a list of elements which a function returns True
"""
def is_even(x):
    if not x%2:
        return  x

my_list = [x for x in range(10,29)]

# With map
map_list = list(map(is_even,my_list))
print(map_list)
#With Filter
filter_list = list(filter(is_even,my_list))
print(filter_list)

# Filter using lambda
even_list = list(filter(lambda x: not x%2,my_list))
print(even_list)
list = list(filter(lambda x: x>10,my_list))
print(list)

"""
Reduce - is for performing some computation on an iterable
- reduce applies a function to the items in an iterable with two at a time, progressively combining
them to produce a single result
Syntax: reduce( <function>, <iterable>)
- reduce start with applying function on first two elements of the iterable. Then the result applies 
with the third element and so on.
"""
from functools import reduce
def sum(s,x):
    return s+x

my_list = [x for x in range(10,29)]

sum_list = reduce(lambda x,y:x+y,my_list)
print(sum_list)

highest = reduce(lambda x,y: x if x>y else y, my_list)
print(highest)
#  Class Exercise -- find specialisation for a student
students = [
    {'name': "Jane", 'age': 43, 'specialisation': 'Software'},
    {'name': "Priya", 'age': 24, 'specialisation': 'Data'},
    {'name': "Diana", 'age': 18, 'specialisation': 'Data'}
]
stname = input("Name of student:")

for x in (filter(lambda x : x['name']== stname,students)):
    print(x['specialisation'])

# print(list(filter(lambda students:students['name']=='Priya' ,students))) Error