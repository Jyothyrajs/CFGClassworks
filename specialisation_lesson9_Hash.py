# # Demo 1
#
# # # hash for integer unchanged
# import functools
#
# print('Hash for 100 is:', hash(100))
# # hash for decimal
# print('Hash for 100.55 is:', hash(100.55))
# # hash for string
# print('Hash for CFG is:', hash('CFG'))
# # hash for tuple
# word = ('g', 'i', 'r', 'l', 's')
# print('The hash is:', hash(word))
#
# # implement a class
# """ Any implementation of class with hash must implement __eq__() & __hash__() methods"""
# class CFGStudent:
#     def __init__(self,age,name):
#         self.name = name
#         self.age = age
#
#     # To check whether two instances are equal
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age
#
#     """To allow a specific implementation of class to be hashed
#       -- as a tuple here
#     """
#     def __hash__(self):
#         print("Tha hash is")
#         return hash((self.age,self.name))
#
# #
# person = CFGStudent(30, 'Nina')
# print(hash(person))
#
# ###################################################################
#
# # GENERAL DICTIONARY EXERCISES
#
# """
# Python program to find the sum of all items in a dictionary.
# Input : {'a': 100, 'b':200, 'c':300}
# Output : 600
# """
#
# # option 1
# def return_sum(my_dict):
#     sum = 0
#     for value in my_dict.values():
#         sum += value
#     return sum
#
#
# # option 2
# import functools
# def return_sum(my_dict):
#     return functools.reduce(lambda x,y:x+y,my_dict.values())
#
#
#
# #
# dict = {'a': 100, 'b': 200, 'c': 300}
# print("Sum :", return_sum(dict))
#
# #####################################################################
#
# """
# Ways to sort list of dictionaries by values in Python.
# 1. We are going to use itemgettor operator
# """
#
# from operator import itemgetter
#
# my_list = [
#     {"name": "Zainab", "age": 20},
#     {"name": "Natasha", "age": 20},
#     {"name": "Sahitya", "age": 19}]
#
#
# """
# # using sorted and itemgetter to print list sorted by both age and name
# """
# print("Sort by age:")
# print(sorted(my_list,key=itemgetter('age')))
#
# print("Sort by name:")
# print(sorted(my_list,key=itemgetter('name')))
#
# print("Sort by age and name:")
# print(sorted(my_list,key=itemgetter('age','name')))
#
# # using sorted and itemgetter to print list sorted by age in descending order
# print("Descending order by age: ")
# print(sorted(my_list,key=itemgetter('age'),reverse=True))

"""
Python – Replace words from Dictionary
Input : 
test_str = ‘CodeFirstGirls best for girls’, repl_dict = {“girls” : “all keen learners”}
Output : 
CodeFirstGirls best for all keen learners.
Explanation: 
“girls” word is replaced by lookup value.
"""

def replace_str(test_str,repl_dict):
    new_str = ""
    for str in test_str.split(' '):
        if str in repl_dict.keys():
            new_str = new_str+" "+repl_dict[str]
        else:
            new_str = new_str + " " + str
    return new_str

test_str = "CodeFirstGirls best for girls"
repl_dict = {"girls": "all keen learners"}
print(replace_str(test_str, repl_dict))



