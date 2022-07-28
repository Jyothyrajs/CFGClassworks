
# Demo assert

"""
Example 1
GOOD INPUT: add_vat(vat=20, prices=[24, 0.15, 32.45, 0])
BAD INPUT: add_vat(vat=20, prices=[24, 0.15, '10', 32.45])
"""

def add_vat(vat, prices):
    """
    Add commission to every price item in the provided iterable.

    :param vat: float, vat percentage
    :param prices: iterable, net prices as per customers' receipt
    :return: list of prices with added vat
    """
    new_prices = [(price / 100 * vat) + price for price in prices]
    return new_prices

print(add_vat(vat=20, prices=[24, 0.15, '10', 32.45]))

def apply_discount(product, discount):
    """
    Add a discount to the price.
    :param product: dict obj, item spec including price
    :param discount: float discount expressed in percent
    :return: float new price
    """
    price = round(product['price'] * (1.0 - (discount / 100)), 2)
    assert 0 <= price <= product['price'], "The discount price is incorrect"
    return price


### VALID INPUT (comment / uncomment  to use as necessary)###
trainers = {'name': 'Running Trainers', 'price': 79.99}
discount  = 200 #(represents 25%)
print(apply_discount(trainers, discount))


### INVALID INPUT (comment / uncomment to use  as necessary)###
trainers = {'name': 'Running Trainers', 'price': 79.99}
discount  = 200 #(represents 200%) --> Assertion Error will be raised
print(apply_discount(trainers, discount))




# #
# # # EXAMPLE 1
# denominator = int(input("Please enter a number to divide by: "))
# try:
#     division_result = 100 / denominator
#     print(division_result)
#
# except ZeroDivisionError:
#     print("You cannot divide by 0, please try gain")
#
# # EXAMPLE 2
# number = int(input('Enter a number in the range 5-10: '))
#
# try:
#     if  number < 5 or number > 10:
#         raise Exception
#
#     division_result = 100 / number
#     print(division_result)
#     print("Well Done")
# # except ZeroDivisionError:
# #     print("You cannot divide by 0, please try gain")
# except:
#     print("Your number is NOT in the requested range")
# # #
# # Example
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#
# # # EXAMPLE 3 - user defined errors
# # # class ValueIsBelowHundredError(ValueError):
# # #     """Raised when value is below 100"""
# # #     pass
# # # EXAMPLE 4 - debugging
# #
# def debugging_n_breakpoints():
#     my_list = []
#     for i in range(10):
#         new_i = 10 + i
#         print('new value is: ', i)
#         my_list.append((new_i))
#     return my_list
# #
# debugging_n_breakpoints()
#
# #########################################################
# ###                     PRACTICE                      ###
# #########################################################
# """ Practice #1
# - Manage the program execution by validating user’s name and age.
# - Raise Validation and Assertion errors for invalid input.
# - Write a registration record into a new file.
#
# file requirements:
# New member name: Doe, John and age 14
# New member name: Kent, Clark and age 19
# New member name: Quinn, Harley and age 10
#
# """
def validate_fullname(fullname):
    if ',' not in fullname or len(fullname) <= 4:
        raise ValueError("Name not in correct format .. input comma bw names")


def validateAge(age):
    if age < 14 or age > 19:
        raise ValueError("Age is to be in 14-19")
try:
    is_success = False
    full_name = input("Enter your full name (lastname,firstname) : ")
    validate_fullname(full_name)
    age = int(input("Enter your age 14-19: "))
    validateAge(age)

    with open ('registration.txt',"a+") as filep:
        filep.write(full_name)
        filep.write(str(age))
        filep.write("\n")
except ValueError as e:
    print(f"Value incorrect {e}")
except FileNotFoundError:
    print("File not exist")
else:
    is_success = True
finally:
    if is_success:
        print("You are successfull")


#
#


# File Not Found Exception
is_success = False
denominator = int(input("Denominator: "))
file_name = input("File name: ")

try:
    result = 100/denominator
    with open (file_name,'r+') as filep:
        filep.write(str(result))
        filep.write('\n')
except ZeroDivisionError:
    print("Can't divide by zero")
except FileNotFoundError:
    print("File not exist")
else:
    is_success = True
finally:
    if is_success:
        print("Successfully finished the task")
    else:
        print("Task failed")
#
# # #Example 2
class NumberIsNotINRange(ValueError):
    pass

try:
    number = int(input("Enter Number in the range(1,5)"))
    if number > 5 or number < 1:
        raise NumberIsNotINRange
    result = 100/denominator
    print(result)

except NumberIsNotINRange:
    print("Not in range")
except ValueError:
    print("Your number is not Valid")
except:
    print("Something went wrong")

# """
# Example grading score - illustration only, not reflected real CFG grading scheme
#
# The program is to ask a score as user input, and display its grade. The program quit when user input/type 'exit'
# example:
# input: Enter student's score: 90
# output: A (90)
#
# input: Enter student's score: exit
# output: [Program exit, nothing to display]
#
# Grading Scheme:
# 0 - 50   : E
# 51 - 65  : D
# 66 - 79  : C
# 80 - 89  : B
# 90 - 100 : A
#
# Practice:
# The program is broken, can you please fix it?
# """
#
#
def get_grade(score):
    if 0 <= score <= 50:
        grade = 'E'
    elif 51 <= score <= 65:
        grade = 'D'
    elif 65 <= score <= 79:
        grade = 'C'
    elif 80 <= score <= 90:
        grade = 'B'
    else:
        grade = 'A'
    return grade


while True:
    student_score_str = input("Enter student's score: ")
    if student_score_str.casefold() == 'exit':
        print('Exit. Bye.')
        break
    student_grade = get_grade(int(student_score_str))
    print(f'{student_grade} ({student_score_str})')


# print("Input the students score.. Type exit once finished")
# scores = []
# while(True):
#     score = input()
#     if score.casefold() == 'exit':
#         break
#     scores.append(int(score))

"""
Extension:
Instead of asking a score one by one (too much user input), 
can you modify the input to accept a comma separated scores instead, and display the average score.

Input: [90, 80, 50]
Output:
A (90)
B (80)
E (50)
Average score is 73.33
"""

def get_grade(score):
    if 0 <= score <= 50:
        grade = 'E'
    elif 51 <= score <= 65:
        grade = 'D'
    elif 65 <= score <= 79:
        grade = 'C'
    elif 80 <= score <= 90:
        grade = 'B'
    else:
        grade = 'A'
    return grade


scores_list = input("Enter scores seperated by comma:")
scores = scores_list.split(',')
score = [int(x) for x in scores]
print(score)
for curr_score in score:
    student_grade = get_grade(curr_score)
    print(f'{student_grade} ({curr_score})')


"""File Not Found Exception"""

# File Not Found Exception
is_success = False
denominator = int(input("Denominator: "))
file_name = input("File name: ")

try:
    result = 100/denominator
    with open (file_name,'r+') as filep:
        filep.write(str(result))
        filep.write('\n')
except ZeroDivisionError:
    print("Can't divide by zero")
except FileNotFoundError:
    print("File not exist")
else:
    is_success = True
finally:
    if is_success:
        print("Successfully finished the task")
    else:
        print("Task failed")