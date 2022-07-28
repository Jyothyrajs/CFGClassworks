
# Counter
import csv
from collections import Counter

"""
collections : Collection module implements the specialised container types alternative to general purpose containers list, dict, set and tuple
"""
"""
Counter: is a dictionary sub class where the elements are stored as keys and the count of each element in the iterable is stored as value.
Counter returns 0 for a missing value instead of keyerror
"""
my_list = [1,2,3,42,4,2,5,6,3]
c = Counter(my_list)
print(c)
print(c[3])

a = Counter(a=1, b=2, c=3, d=4)
print(a)

""" Named Tuple : Returns a new sub class named typename. Th eobjects created are iterable and indexable.  assigns a name to each position in the tuple to make it more readable and self documented. It allows to access the fields by name instead of index """

tpl = (1,2,3,4)
print(tpl[2])


from collections import namedtuple

tpl = namedtuple("shopping_items",'grocery clothes cosmetics')
print(tpl[1])
today = tpl(grocery='Sugar',clothes='Shirt',cosmetics='Face cream')
print(today)
print(today.grocery)

# Exercise: To create the to do list details into a named tuple from a csv file

from collections import namedtuple
import csv

todolist_tpl = namedtuple('ToDoList_details','Task,Priority,No_hrs')
# map applies the function to each item in iterable
# _make  - make a new instance from the existing iterables
todo_list = map(todolist_tpl._make,csv.reader(open('todolist.csv','r')))
for item in todo_list:
    print(item.Task)

#  Add the list into mysql
# Refer CFG_Project_db_code.py

# Deque
from collections import deque

d = deque('ghi')
for i in d:
    print(i)

d.append('k')
print(d)
print(d.pop())
d.appendleft('q')
print(d)
d.popleft()
print(d)

# Deque applications
# Return the last 10 lines of a file

def tail(filename,n=10):
    with open(filename) as f:
        return deque(f,5)

print(tail('python_mysql_connection.py'))

"""
ChainMap: datastructure that allows multiple dictionaries as single one
- create a single updatable view
- chainmap stores underlying dictionaries by reference(dict can be from different modules)
Usecases:
    - searching through multiple dictionaries
    - Providing a chain of default values
    - Performance critical applications that frequently compute subsets of dictionary
"""

from collections import ChainMap

toys = {'Blocks': 30, 'Monopoly': 20}
computers = {'iMac': 1, 'Chromebook': 800, 'PC': 400}
clothing = {'Jeans': 40, 'T-Shirt': 10}

inventory = ChainMap(toys,clothing,computers)
for item in inventory.items():
    print(item)

#     Output
# ('iMac', 1)
# ('Chromebook', 800)
# ('PC', 400)
# ('Jeans', 40)
# ('T-Shirt', 10)
# ('Blocks', 30)
# ('Monopoly', 20)

# Reference: https://florimond.dev/en/posts/2018/07/a-practical-usage-of-chainmap-in-python/#:~:text=ChainMap%20is%20a%20data%20structure,create%20a%20single%2C%20updateable%20view.


"""

ORDERED DICT : dictionary sub class designed to remember the order of its items
- ordered dict iterate over the keys and values in the same order it is inserted
    - designed to be good at reordering operations
    - Dictionary compares the  contents
    -  Each entry in the dictionary will be remembered
    -  Extra memory to maintain the order of insert
regular dict - designed to be very good at mapping operations
- while creating sequence, the order of ordered dictionary using list/ tuple is same as that of the sequence
- but in case of set, order is not known untill it is created
- iterating through ordered dictionary can be done using key directly or with items(), values() and key()
- big win in terms of memory usage and iteration efficiency
- new methods move_to_end() and popitem()
- in regular dict - equality returns true if elements in both dictionary are same
- In ordered dictionary, the equality depends on the order of items in the list even if same set of items are present
"""
from collections import OrderedDict

ord_dict  = OrderedDict()
ord_dict['Banana'] = 2
ord_dict['Dates'] = 5
print(ord_dict)
ord_dict.pop('Dates')

ord_dict['Apple'] = 8
ord_dict['Guava'] = 10

for key in ord_dict:
    print(key)

# Reversed ordered dictionary
for key in reversed(ord_dict):
    print(key)


# Exercise: Sort the dictionary by values

for key,_ in sorted(ord_dict.items(), key = lambda item:item[1]):
    ord_dict.move_to_end(key)

for key in ord_dict:
    print(key)
# Exercise: calculate time for sort

from time import perf_counter

start = perf_counter()
for key,_ in sorted(ord_dict.items(), key = lambda item:item[1]):
    ord_dict.move_to_end(key)
end =  perf_counter()
elapsed_time = end-start
print("Elapsed time : ",elapsed_time)