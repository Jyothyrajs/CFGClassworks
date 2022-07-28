import itertools
"""
itertools - iterator functions for efficient looping
- available only in python
includes a set of functions for working with iterable data sets
itertools are used to generate permutation
Rela eg: Retry steps may be DB connection
"""
# 1. Count: This function takes two optional arguments and returns an iterator.
# print the first four even numbers
result = itertools.count(start=0, step = 2)

for num in result:
    if num < 8:
        print(num)
    else:
        break

#  Print 0 to 9
result = itertools.count(start=0)

for num in result:
    if num < 10:
        print(num)
    else:
        break

#################################
# 2. Cycle: This function takes in an iterable and goes over it indefinitely​.

import itertools

result = itertools.cycle('12345')

counter = 0
for num in result:
    if counter < 10:
        print(num)
        counter = counter + 1
    else:
        break


###################################
# 3. Repeat: Takes an optional times parameter that can be used as a termination condition.
# print CodeFirstGirls two times

import itertools

result = itertools.repeat('12345',2)

for i in result:
    print(i)

###################################

# 4. Chain: This function accepts a variable number of iterables and loops through all of them, one by one.
# iterate over three lists
import itertools

list_one = ['a', 'b', 'c']
list_two = ['d', 'e', 'f']
list_three = ['1', '2', '3']

result = itertools.chain(list_one,list_two,list_three)

for i in result:
    print(i)

###################################

# 5. Compress: This function takes in an iterable and a selector,
# and returns an iterable with only those items for which the corresponding selector value is true.
""" Example selecting alist of items within a price range
To return some not null values
"""

my_list = ['Hello','welcome','Sorry']
wish = [True,True,False]

result = itertools.compress(my_list,wish)

for i in result:
    print(i)


###################################

# 6. DropWhile: An iterable and a function (predefined or lambda) is passed to it.
# Based on the condition inside the function, dropwhile keeps on dropping values from the iterable
# until it encounters the first element that evaluates to false.

my_list = [5,5,1,2,5]

def _func(item):
    return item == 0

def _funcdrop5(item):
    return item == 5

result = itertools.dropwhile(_func,my_list)

for i in result:
    print(i)


result = itertools.dropwhile(_funcdrop5,my_list)

for i in result:
    print(i)

####################################

# 7. Product: iterate over the Cartesian product of a list of iterables
"""
Eg: for  a tournament schedule
"""
my_list = ['Hello','welcome','Sorry']
wish = [True,True,False]


result = itertools.product(my_list,wish)

for i in result:
    print(i)


#####################################

# 8. iSlice: works much the same way as slicing a list or tuple.
# You pass it an iterable, a starting, and stopping point, and, just like slicing a list,
# the slice returned stops at the index just before the stopping point.

# Slice from index 2 to 4
"""
Why one more instead of normal slice - it only create the object reference of instructions.
Doesn't store in memory
Executed as and when required
"""
result = itertools.islice('CodefirstGirls',2,4)
print(list(result))

######################################

# 9. GroupBy: groups objects in an iterable.

data = [1,1,2,3,4,2,5]
for key,grp in itertools.groupby(data):
    print(f'{key}:{list(grp)}')

# group people by their age

data = [{'name': 'Soujanya', 'age': 20},
        {'name': 'Elena', 'age': 19},
        {'name': 'Betsy', 'age': 19},
        {'name': 'Ling', 'age': 23}]

group_data = itertools.groupby(data,key=lambda x:x['age'])

for key,grp in group_data:
    print(f'{key}:{list(grp)}')

######################################

# 10. Tee: used to create any number of independent iterators from a single iterable.
"""
Usecase : for simulation
"""
iterator1,iterator2 = itertools.tee('Welcome')

print(list(iterator1))
print(list(iterator1))
print(list(iterator2))

######################################

# 11. Zip Longest: advanced zip elements function

x = [1,2,3,4,5,6]
y = ['a','b','c']
result = list(zip(x,y))
print(result)


result = itertools.zip_longest(x,y)
print(list(result))

result = itertools.zip_longest(y,x)
print(list(result))


# create our own grouper utility function


nums = [iter([1,2,3])] * 3
print(nums)
print(*nums)




######################################

# 12. Permutation: all the possible combinations in which a set or string can be ordered or arranged.

word = 'CFG'

result = itertools.permutations(word)

for p in list(result):
    print(p)

word = 'CFG'

result = itertools.combinations(word,2)

for p in list(result):
    print(p)

# EXERCISE
# strs = ['eat', 'tea', 'ate', 'nat', 'tan', 'bat']
#
# output:
#     ['eat', 'tea', 'ate'],
#     ['nat', 'tan'],
#     ['bat']
import itertools

strs = ['eat', 'tea', 'ate', 'nat', 'tan', 'bat']

grouped_data = itertools.groupby(strs,key=lambda x:sorted(x))
for key, grp in grouped_data:
    print(list(grp))