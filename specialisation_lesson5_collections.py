# COUNTER
# keeps the count of elements in the iterable
# key represents the elements and value represents the count of that element in the iterable
from collections import Counter

a_list = [1, 2, 2, 3, 4, 4, 4, 10]
a_string = 'CodeFirstGirls'
a_dict = {'a': 5, 'b': 3, 'c': 5, 'd': 5, 'e': 1}

# counting objects

c_list = Counter(a_list)
c_string = Counter(a_string)
c_dict = Counter(a_dict.values())
c_dict_k = Counter(a_dict)

print(c_list)
print(c_string)
print(c_dict)
print(c_dict_k)

# OrderedDictionary
# class collections.OrderedDict()
# ORDEREDDICT
""""
ORDERED DICT : dictionary sub class designed to remember the order of its items
- ordered dict iterate over the keys and values in the same order it is inserted
    - designed to be good at reordering operations
    - Dictionary compares the  contents
    -  Each entry in the dictionary will be remembered
    -  Extra memory to maintain the order of insert
regular dict - designed to be very good at mapping operations
- while creating sequence, the order of ordered dictionary using list/ tuple is same as that of the sequence
- but in case of set, order is not known untill it is created
"""
from collections import OrderedDict

d = OrderedDict([('apple', 5), ('orange', 6)])
print(d)

d['kiwi'] = 7
print(d)

d['melon'] = 8
print(d)

d['banana'] = 1
print(d)

# create empty OrderedDict and populate

o = OrderedDict()
o['key1'] = "value1"
o['key2'] = "value2"
print(o)

"""Default Dictionary - proides a default value for the dictionary created
eliminate KeyError"""

# DEFAULTDICT

# string example
from collections import defaultdict

state_capitals = defaultdict(str)
print(state_capitals)

state_capitals['Alaska']
print(state_capitals)

# list example

basket = [('Fruit', 'Pear'), ('Vegetable', 'Tomato'), ('Fruit', 'Peach')]
dd = defaultdict(list)

for k, v in basket:
    dd[k].append(v)

print(dd)

# CHAIN MAP

from collections import  ChainMap

# define two dictionaries with at least some keys overlapping.
dict1 = {'apple': 1, 'banana': 2}
dict2 = {'coconut': 1, 'date': 1, 'apple': 3}

# create two ChainMaps with different ordering of those dicts.
combined_dict = ChainMap(dict1, dict2)
reverse_ordered_dict = ChainMap(dict2, dict1)

print(combined_dict)

for k, v in combined_dict.items():
    print(k, v)


print(reverse_ordered_dict)

for k, v in reverse_ordered_dict.items():
    print(k, v)

""" Named Tuple : assigns a name to each position in the tuple to make it more readable and self documented. It allows to access the fields by name instead of index """
# NAMED TUPLE

from collections import namedtuple

Person = namedtuple('Person', ['age', 'height', 'name'])

# alternatively

Person1 = namedtuple('Person', 'age height name')

anna = Person(30, 165, 'Anna')
marie_liz = Person1(age=25, height=178, name='Marie Elizabeth')

print(anna.age)
print(anna.name)


############### EXERCISES ###############


"""
Use a defaultdict to store a count for each character that appears in a given string. 
Print the most common character in this dictionary.
Example:
'CodeFirstGirls Nanodegree'
output: e
"""
# Naomi's Solution
from collections import Counter, defaultdict

test_string = 'CodeFirstGirls Nanodegree'

c_test = defaultdict(str, Counter(test_string))
highest_occurrence = max(c_test.values())
highest_freq_chars = {key for (key,value) in c_test.items() if value == highest_occurrence}
print(highest_freq_chars)


# Solution 2

from collections import defaultdict

s = "CodeFirstGirl"

letter_count = defaultdict(int)

for character in s:
    letter_count[character] += 1
for i,ch in enumerate(letter_count.items()):
    print(i,ch)

print(letter_count)
for k,v in letter_count.items():
    print(k,v)

from collections import defaultdict

s = "CodeFirstGirl"

letter_count = defaultdict(int)

for character in s:
    letter_count[character] += 1
for ch in letter_count:
    print (letter_count[ch])
most_common_character = max(letter_count, key = lambda key: letter_count[key])

print(most_common_character)


"""DEQUEUE"""

from collections import deque
d = deque('CodeFirstGirls Nanodegree')
d.append('!')
print(d)

d.appendleft('*')
print(d)

d= deque('123')
d.pop()
print(d)

d= deque('123')
d.popleft()
print(d)

d= deque('123')
d.rotate(1)
print(d)


# USER LIST

from collections import UserList


class MyUniqueList(UserList):

    def add_in_middle(self, item):
        count = -1
        for i in self:
            count += 1

        self[int(count / 2)] = item


my_list = MyUniqueList([1, 2, 3, 4, 5])
print(my_list)

my_list.add_in_middle("CFG")
print(my_list)