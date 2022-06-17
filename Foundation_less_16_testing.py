"""
This is a possible interview coding question. Let's check the task,
implement our solution and then write tests for it:

Task
Given an integer x perform the following conditional actions:

If x is odd, return 'Red'
If x is even and in the inclusive range of 2 to 5, return 'Blue'
If x is even and in the inclusive range of 6 to 20, return 'Red'
If x is even and greater than 20, return 'Blue'

# Constraint notes:
# an input integer is alway withing the range 1 to 100 inclusive
"""

def is_within_range(num, _min, _max):
    if _min <= num <= _max:
        return True
    return False

def is_even(num):
    return num %2 ==0

def red_or_blue(num):
    if not is_even(num) or (is_even(num) and is_within_range(num, 6, 20)):
        return 'Red'
    if (is_even(num) and num >20) or num in [2,4]:
        return 'Blue'

