

# SIMPLE RECURSIVE FUNCTION

"""
Python limits recursive object of 1000 call
"""
#
# def hello():
#     print("Hi CFG")
#     hello()
# """
# Python limits recursive object of 1000 call -- Result in a recursion error
# """
# hello()


# i = 0
# j = 0
# def hello():
#     global i
#     global j
#     print("Hi CFG",i)
#     if i < 10:
#         i += 1
#         hello()
#     j += 1
#     print("END",j)
#
# hello()


def print_pattern(num):
    """"
    Pattern is going to be up to num numbers increasing and decreasing
    Eg: 12344321
    :param num: max number
    :return: none
    """""
    if num < 1:
       return
    else:
       print(num,end=" ")
       print_pattern(num-1)
       print(num,end=" ")
       return


# Driver Code
my_number = 5
print_pattern(my_number)


# Exercise:
# ******
#  ****
#    *

def print_num(num):
    print()

########################################

# FACTORIAL

"""
E.g. factorial of 6 (6!) is 1*2*3*4*5*6 = 720
"""


def get_factorial(x):
    if x == 1:
        return 1
    else:
        return x * get_factorial(x-1)

num = 6
print("The factorial of", num, "is", get_factorial(num))


###########################################

# FIBONACCI
"""
Fibonacci series of 5 is : 0 1 1 2 3
- Drawback: calculate the same function multiple times - so as the number becomes larger, code becomes slower
"""


def fib(n):
    if n== 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

num = 6
print("Fibonacci series of length ", num, ": ", fib(num))

for i in range(5):
    print(fib(i), end = " ")


#######################################################

"""
Return all possible combinations of strings of given length, 
which can be formed from a set of supplied characters.
Input: 
char_set = {'a', 'b'}, length = 3
Output:
aaa
aab
aba
abb
baa
bab
bba
bbb
NB: we cannot use itertools product or permutations functions.
"""
# Todo: Try with Debug tool

def get_str_combinations(char_set, l):
    """
    The function that prints all possible strings of length l.
    """
    n= len(char_set)
    get_str_combinations_rec(char_set, " ",n,l)


def get_str_combinations_rec(char_set, prefix, n, l):
    """
    Main recursive method that prints all possible strings of length l.
    """
    if l == 0:
        print(prefix)
        return
#     Add characters one by one
# form char_set recursively
# call for l = l-1
    for i in range(n):
        new_prefix = prefix + char_set[i]
#         decrease l by 1 as we just added first char
        get_str_combinations_rec(char_set,new_prefix,n,l-1)


print("Test No1")
set1 = ['a', 'b']
k = 3
get_str_combinations(set1, k)