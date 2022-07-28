### DEMO 1 ###
"""
Program to check if temperature is freezing (0 or below)
​
Example:
Input: What is the temperature? 10
Output: Temperature is freezing: False
"""
temp = float(input("What is the temperature ?"))
if(temp <= 0):
    status = True
else:
    status = False
print( f"Temperature is freezing:{status}")

### EXERCISE 1 ###
"""
You have a budget of £10 and want to write a program to decide which burger restaurant to go to.
​
Input the price of a burger using input()
Check whether the price is less than or equal (<=) 10.00
Print the result in the format below
Burger is within budget: True
Hint: remember to convert the input from a string to a decimal with float()
Example:
Input: How much is a burger? 9.45
Output: Burger within budget: True
"""
price = float(input("How much is a burger?"))
if price <= 10:
    in_budget = True
else:
    in_budget = False
print(f"Burger within budget:{in_budget}")
msg = f"Burger within budget:{in_budget}"
print(msg)
msg = "Burger within budget:{}".format(in_budget)
print(msg)

### DEMO 2 ###
"""
This program will work out if you should visit Mars based on whether you want to visit and if you can afford it.
​
Example:
Input: 
Would you like to visit Mars (y/n)? y
Can you afford to visit Mars (y/n)? y
​
Output: You should visit Mars: True
"""

### EXERCISE 2 ###
"""
Add code to your burger program to input whether the restaurant has a vegetarian option
​
The output should say whether the cost is within budget AND has a vegetarian option
​
Example:
Input:
How much a burger? 10
Is there any vegetarian options (y/n) ? y
Output:
Restaurant meets criteria: True
"""
​
​
​
### DEMO 3 ###
"""
This program checks whether you are an admin and you have entered the right password:
"""
​
​
​
### EXERCISE 3 ###
"""
Rewrite the output of your burger program to use if statements
​
If it is a good choice it should be:
​
    "This restaurant is a great choice!"
​
If it is not a good choice it should be:
​
    "Probably not a good idea"
"""

### DEMO 4 ###
"""
Elif and Else statements explained with examples
​
Else EXAMPLE
"""
name = input("What is your name? ")
is_admin = name == 'admin'

password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'

if is_admin and is_password_correct:
    print('Welcome')

else:
    print('Go away')

"""
You can use multiple elif statements together.
Elif EXAMPLE
"""

dog_size = int(input('How big is the dog? '))

if dog_size > 75:
    print('That is a big dog')

elif dog_size < 10:
    print('That dog could fit in my pocket')

elif dog_size < 25:
    print('That is a small dog')

else:
    print('That is an average dog')

### EXERCISE 4 ###
"""
Now that you've finished your burger, you want to pay for your food. 
Let's write a program to calculate your meal and apply a discount if applicable.
If your total meal costs more than £20 and you have a discount, the price will be reduced by 10%. 
The program should print "Discount applied" or "No discount" depending on whether the discount criteria was met.
​
Example:
Input:
How much did the meal cost? 25
Do you have a discount (y/n)? y
Discount applied
Total cost: 22.5
"""
meal = int(input("How much did the meal cost? "))
discount = input('Do you have a discount (y/n)?')
if( discount.lower() == 'y' and meal > 20):
    meal = meal * .9
    print(f"Discount Applied & Bill is {meal}")
else:
    print(f"No discount & Bill is {meal}")


"""
2 Elif Exercise:
You're cooking a pizza and need to check that the oven is at the right temperature.

Write a program to:
Ask the user to input the temperature
Prints "The oven is too hot" if the temperature is over 200
Prints "The oven is too cold" if the temperature is under 150
Prints "The oven is at the perfect temperature" if the temperature is 180
Prints "The temperature is close enough" for any other temperature
​
Example:
Input:
What is the temperature of the oven? 180
Output:
The oven is at the perfect temperature
"""

### DEMO 5 ###
"""
Random library demo, roll the dice
random.randint(start, stop)
"""
import random
choice = int(input("Head- 1/Tail--0  ?"))
sel = random.randint(0,1)
if(sel == choice):
    print(" WIN")
else:
    print(f"Sorry toss is {sel} Try Again")

### EXERCISE 5 ###
"""
This program uses random to simulate a coin flip.
​
To finish the program you will need to add the following:
​
If the random coin flip matches the choice input by the user then they win
Otherwise if the random coin flip does not match the choice input by the user then they lose
"""
​
# import random
#
# def flip_coin():
#     # your code goes here
#
# choice = input('heads or tails: ')
# result = flip_coin()
#
# print('The coin landed on {}'.format(result))

################################################
###           PALINDROME EXERCISE            ###
################################################

"""
Palindrome Check
​
Write a function that takes a non-empty string 
and that returns a boolean representing whether the string is a palindrome.
​
Think and plan your solution first. 
"""

def isPalindrome(string):
    l = 0
    r = len(string) - 1
    while l < r:
        if( string[l] != string[r]):
            return False
        l = l + 1
        r = r - 1
    return True

print(isPalindrome('hannah'))  # should return True

print(isPalindrome('mummy'))  # should return False

print(isPalindrome('I'))  # should return True