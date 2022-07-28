### DEMO 1 ###
"""
Show students how to create a new file and then run this file.
Explain where the result is displayed (console) and then point how to re-run the file if necessary.
"""

print('Hello, World!')
print('I hope it is sunny this weekend')

### EXERCISE 1 ###

"""
Exercise 1.1: Now that you've run your first program, try the following:

- Change the message to anything you want
- Repeat the code on multiple lines to output several messages
- Find out what happens when you remove different parts of the code (e.g. brackets)
- Don't worry if something unexpected happens. Think about what you changed and why it might have caused it to happen.
"""
print('Hello, World!I am learning Python')
print('I hope it is sunny this weekend')
### DEMO & EXERCISE 2 ###
"""
Ask studetns to use Python console in PyCharm and practice the following operations together. 
Explain where required.

5 - 6
8 * 9
6 / 2
5 / 0
5.0 / 2
5 % 2
2 * (10 + 3)
2 ** 4
What does each one do and what is its output?
Are there any outputs you didn't expect?
"""
print(5-6)
print(8*9)
print(6/2)
print(6//2)
print(9//2)
# print(5/0)
print(5.0/2)
print(5%2)
print(2*(10+3))
print(2**4)
### DEMO & EXERCISE 3 ###
"""
In your Python console type each of these
"Cat"
"Cat" + " videos"
"Cat" * 3
"Cat" + 3
"Cat".upper()
"Cat".lower()
"the lord of the rings".title()
What is the output for each one and why?
One of them causes an exception. Read the exception message. What do you think it means?
"""
print("Cat")
print("Cat" + " videos")
print("Cat" * 3)
# print("Cat" + 3)
print("Cat".upper())
print("Cat".lower())
print("the lord of the rings".title())
print("welcome to python".capitalize())
print("welcome to pythoOn".count('o'))
print("welCome".swapcase())
print("welcometocatcase".split('c'))

print("welcome".rfind('c'))
print("welcome".find('c'))
print("welcome to pythoOn".find('to'))
print("welcome to pythoOn".split('to'))

mydict = {83:  80,80:  83}
txt = "HellP Sam!"
print(txt.translate(mydict))
print( txt.translate(mydict))
print(txt)
### DEMO & EXERCISE 4 ###
"""
EXAMPLES OF STRINGS METHODS
You can copy-paste these examples into your console to save tim typing. 
Demonstrate what they do and only then complete an exercise together. 
"""

# 'Our example string object'.upper()
# 'Our example string object'.lower()
# 'Our example string object'.title()
# 'Our example string object'.count('o')
# 'our example string object'.capitalize()
print('Our example string object'.endswith('ject'))
print('Our example string object'.endswith('mock'))
print('To make a nice cuppa you need: tea, milk, sugar and a cookie '.split(','))
print('Our example string object'.replace('p', '#'))

"""
DEMO - show in PyCharm console how to type a string, use dot and a 'tab' to bring up a list of methods for an object. 
# TASK TO COMPLETE TOGETHER: check built in methods available to use for strings
'string object' + . + click TAB
use help() function
"""
print("MyTest".casefold())
### EXERCISE 5 ###

"""
Errors and casting objects into different types
Run this:
print("Cat" + 3)
it would result in Error!
Putting a number in str() converts it to a string
print("Cat" + str(3))
"""
text = "Cat" + str(3)
print(text)
car_wheel_count = 4
my_float = 3.14
result = car_wheel_count + my_float
print(round(result, 2))
### DEMO 6 ###
"""
Show the example of this program to the class and walk each line step by step:
OBJECTIVE -- demonstrate that 
"""
oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange

print(str(oranges) + " oranges")
print("costs " + str(total_cost))
"""
The oranges variable is reused twice in the program
"""

### EXERCISE 7 ###
"""
In a new Python file called cat_food.py, create a program that calculates how many cans of cat food you need to feed 10 cats
Your will need:
A variable for the number of cats
A variable for the number of cans each cat eats in a day
A print() function to output the result
Extension: change the calculation to work out the amount needed for 7 days
Example solution below (share it with students after they have had a go)
"""


cats  = 10
cans = 3
print(str(cats)+ " Cats need " + str(cans*10) +" can per day")
print(str(cats)+ " Cats need " + str(cans*7*10) +" can per week")
# cats = 10
# cans = 2
#
# total_cans = cats * cans
#
# output = str(cats) + " cats eat " + str(total_cans) + " cans"
# print(output)

### EXERCISE 7 ###
"""
Rewrite cat_food.py to use string formatting instead of joining strings with +.
An example of string formatting:
--------------------------------
user_name = 'Jenny_1995'
age = 23
output = '{} is {} years old'.format(user_name, age)
print(output)
"""
cats  = 10
cans = 3

print("{} Cats need {} can per day".format(cats,cans*10))
print( "{} Cats need {} can for 7 days".format(cats,cans*10*7))
# Example solution
# cats = 10
# cans = 2
#
# total_cans = cats * cans
#
# output = "{} cats eat {} cans".format(cats, total_cans)
# print(output)
### DEMO 8 ###
"""
Show few examples on how to join strings together:
'-'.join(my_words)
' '.join(my_words)
''.join(my_words)
"""
### EXERCISE 8 ###
"""
Perform string formatting, so that your final sentence looks like this:
guests = ["Mary", "Pete", "Eoin"]
Result:
"We are going to cinema with my classmates: Mary, Pete, Eoin and me"
Example solution below:
(We can use string interpolation and join() function to build this sentence)
"""
guests = ["Mary", "Pete", "Eoin"]
print("We are going to cinema with my classmates :{names} and me".format(names =','.join(guests)))
# guests = ["Mary", "Pete", "Eoin"]
#
# "We are going to cinema with my classmates: {names} and me.".format(
#     names = ', '.join(guests))
### DEMO & EXERCISE 9 ###
"""
String Slicing ( do these examples with students explaining every case)
S = 'ABCDEFGHI'
print(S[2:7])
S = 'Hippopotamus'
print(S[-7:-2])
S = 'ABCDEFGHI'
print(S[2:-5])
S = 'ABCDEFGHI'
print(S[2:7:2])
Slice at Beginning & End
Omitting the start index starts the slice from the index. Meaning, S[:stop] is equivalent to S[0:stop]
Omitting the stop index extends the slice to the end of the string. Meaning, S[start:] is equivalent to S[start:len(S)]
# Slice first three characters from the string
S = 'ABCDEFGHI'
print(S[:3]) 
# Slice last three characters from the string
S = 'ABCDEFGHI'
print(S[6:])
Reverse a String
You can reverse a string by omitting both start and stop indices and specifying a step as -1.
S = 'ABCDEFGHI'
print(S[::-1])
S = 'Code First Girls'
print(S[::-1])
"""
S = 'ABCDEFGHI'
print(S[2:7])
print(S[-7:-2])
print(S[2:-5])
print(S[2:7:2])
print(S[:3])
print(S[:6])
print(S[:-1])
print(S[::-1])
S = 'Code First Girls'
print(S[::-1])

S = 'Code First Girls'
print(S[:-3:])

print(S[:-3:-1])

S = 'Hippopotamus'
print(S[-7:-2])
S = 'ABCDEFGHI'
print(S[2:-5])
S = 'ABCDEFGHI'
print(S[2:8:2])
print(S[2:7:1])

## DEMO 10 ###
"""
In built functions examples
Comment / uncomment each line in turn to see what each in-built function does
"""
print('Code')
print(type('Code'))
print(len('Code'))
print(ord('C'))
print(chr(ord('C')))
print(help('Code'))
print(help(type('Code')))
txt = "CFG is awesome,I love Python"
print(txt[-8:-2])
print(txt[-2:-4:-1])
print(txt[-2:-1])
# Lesson 2
# Calculate Pizza
friends = int(input("No of friends"))
pizza_for_share = int(input("One pizza for how many people:"))
pizza = friends //pizza_for_share
if(friends % pizza_for_share ):
    pizza = pizza +1
print("{} friends require {} pizza".format(friends,pizza))

# Date and Time
import datetime
cur_time = datetime.datetime.now()
print(cur_time)
todate = datetime.date.today()
print(todate)
print("Current Year :",todate.year)
print("Current Month:",todate.month)
print("Current time: ",todate.day)
birth_date = datetime.date(2000,12,5)
print(birth_date)
print(birth_date.strftime("%d %b %Y")) #format date object into string
print(birth_date.strftime("%d %m %Y"))
#
print(datetime.datetime.strptime("14 June 2016","%d %B %Y"))#Convert string to  date time object


date_from_timestamp = datetime.date.fromtimestamp(12345678)
print(date_from_timestamp)

import datetime as dt
my_date = dt.date.today()
print(my_date)

my_time = dt.time(10,23,34,456)
print(my_time.hour)
print(my_time.minute)
print((my_time.second))

birth_date = dt.date(1984,3,14)
print(birth_date.year)
print(birth_date.month)
print(birth_date.day)


print(birth_date - my_date)


import datetime as dt
t1 = dt.date(year = 2018, month = 7, day = 12)
t2 = dt.date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)


import datetime as dt
cur_date = dt.datetime.now()
new_year = dt.datetime(2023,1,1)
time_remaining = new_year-cur_date
print(type(time_remaining))
print(f"{new_year} - {cur_date} = {time_remaining})")

import datetime as dt
penality_date = dt.date.today()
penalty_amount = 65
deadline = penality_date + dt.timedelta(14)
print(f"Pay by {deadline} with amount {penalty_amount}")

#Change to US date
import datetime as dt
uk_date = dt.datetime.today()
print(uk_date)
uk_dt_str = uk_date.strftime('%m %d %Y')
print(uk_dt_str)
us_date = dt.datetime.strptime(uk_dt_str,'%m %d %Y')
print(us_date)


mystr = "Hello I am also a CFG student Now"
print(mystr.rsplit('a',4))

mydict ={'item1':10,"item2":5,"item3":25,"item4":"Pen"}
print(mydict.setdefault("item6",200))
x =mydict.setdefault("item2",500)
print(x)