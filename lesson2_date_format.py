# Example 1
name = input("Enter Name")
location = input("Where Are you from?")
print(f"My Name is {name}, I am from {location}")

# Example 2
from datetime import date
age = int(input("Your Age"))
today_date = date.today()
yr = (today_date.year) - age
print(f"You born in {yr}")


#Exercise My birthday
from datetime import date
import datetime
import time
birth_day = datetime.date(1984,3,14)
this_birthday = birth_day.replace(year=date.today().year+1)
days_to_go = date.today() - this_birthday
print(days_to_go)
print(datetime.tzinfo)



#Example3 : Claculate no of pizzas you have to buy if 1 pizza shared by two members
no_of_friends = int(input("Number of friends at your house"))
# Method1
no_of_pizza = (no_of_friends+1)//2
# Method2
if(no_of_friends%2 == 0):
    no_of_pizza = (no_of_friends//2)
else:

    no_of_pizza = (no_of_friends // 2) +1
print(f"You need  {no_of_pizza} Pizzas")

#Example 4: Modules and packages
#strftime -- format
#strptime -- parse string to date
import datetime
print(datetime.datetime.now())

date_of_birth = datetime.date(2022,6,1)
print(date_of_birth)
print(date_of_birth.strftime("%d %b %Y"))
print(date_of_birth.strftime("%d %a %B %Y"))

#Example 5 : Add the dates
import datetime

my_date = datetime.datetime.strptime("01 June 2022","%d %B %Y")
future_date = my_date+ datetime.timedelta(10)
print(future_date)

#Example Update Penalty due pay within 14 days
import datetime
issue_date = input("Enter issue date in DDMMYYYY format")
pay_by = datetime.datetime.strptime(issue_date,"%d%M%Y") + datetime.timedelta(14)
pay_by_ft = pay_by.strftime("%d %b %Y")
print(f"Pay by {pay_by_ft} to reduce 65")

pay_by_ft = pay_by.strftime("%d %m %Y")
print(f"Pay by {pay_by_ft} to reduce 65")

#Example for loop
# for number in range(10):
#     print(number,end=' ')

"""Example 10 : Sum of sequence numbers 1,2,3,4,5"""
sum = 0
for n in range(1,6):
    sum = sum + n
print(sum)

word = 'hello'
for c in word:
    print(c,end=' ')

# Example 11: Encoding hi to xyzhabcxyziabc
word = 'hello'
secret_word = ''
for c in word:
    secret_word = secret_word+'xyz'+c+'abc'
print(secret_word)

#To DO :  Decode it back
secret_word = 'xyzhabcxyzeabcxyzlabcxyzlabcxyzoabc'
word = ''
prefix = 'xyz'
suffix = 'abc'
i = 0
while i < len(secret_word):
    i = i + len(prefix)
    if i < len(secret_word):
        word = word + secret_word[i]
        i = i+1
    print(word)
    i = i +len(suffix)
print(word)



#Example 11:While loop : allow entry based on store capacity
store_capacity = 5
while store_capacity > 0:
    print(f"You are welcome:  {store_capacity} space available ")
    store_capacity = store_capacity - 1

#Example 12: function
def hello(name):
    print(f"Hello {name}")

def intro(name,job="Software Engineer"):
    print(f"Hello, I am {name}, I work as a {job}")
def sum(x):
    total = 0
    for n in range(1,x+1):
        total = total+n
    return total
hello("Jyothy")
intro("Jyothy","Cloud Engineer")
intro(job=" Engineer",name="Jyothy")
intro("Jyothy")#Default argument
print(f" Sum = {sum(5)}")

#Variable length argument
def print_nums(*nums):
    print(nums)

print_nums(1,2,3,4)


#Keyword arguments kwargs
def register(**kwargs):
    print(kwargs)

register(name="Jyothy",city="UK")
register(name="Jyothy",city="UK",job="Engineer")

#Todo: Function to calculate return area of circle
def area(radius):
    return 3.14 * (radius**2)
radius = int(input("Radius of circle :"))
area_v = area(radius)
print("Area of circle with radius {} : {}".format(radius,area_v))
