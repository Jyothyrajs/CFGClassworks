### DEMO 1 ###
"""
List values can be accessed using their index in square brackets
"""
name = ['Jyothy','Emily', 'Munich']
print(name)
### EXERCISE 1 ###
"""
When I'm travelling in the winter I often forget to pack warm clothes. 
Let's write a program to help me to remember the right clothes.

The program should check if the first item in the clothes list is "shorts". 
If it is it should change the value to "warm coat".
"""

clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]
if (clothes[0] == 'shorts'):
    clothes[0] = 'warm coat'
print(clothes)
teams = [['Emily','Luke'],['John','Lee'],['Jyothy']]
print(teams[0])
### DEMO 2 ###
cost = [1,22,12,21,32,42,14]
print(len(teams))
print(len(cost))
print(max(cost))
print(min(cost))

costs = [1.2, 4.3, 2.0, 0.5]
print(len(costs))
print(max(costs))
print(min(costs))

print(costs)
print("Sorting:")
print(sorted(costs))
print(reversed(costs))
print(list(reversed(costs)))

costs_rev_sorted = sorted(costs,reverse=True)
print(costs_rev_sorted)

print(list([1,2,3]))
# print(list(1)) wont work
"""
Examples of list functions (NB: functions and methods are different!)
"""
#
### EXERCISE 2 ###
"""
Make a list of game scores. Using list functions write code to output information of the scores in the following format:

    Number of scores: 10
    Highest score: 200
    Lowest score: 3

Extension: Output all of the scores in descending order
"""

game_score = [12,2,3,12,32,22,11,7,8,5]
print("Number of Scores:", len(game_score))
print("Highest Score:",max(game_score))
print("Lowest score:",min(game_score))
print("Sorted in desc : ", sorted(game_score,reverse=True))

### DEMO 3 ###
"""
append() and in

You can check if an value is in a list using the IN operator. 
If the value is in the list it will result in True and False if it is not.
"""

stud_name = ['Jyothy','Emily', 'Munich']
print(stud_name)
# name = input("Which student you are looking for: ")
name = "Emily"
if name in stud_name:
    print("{} is in the class ".format(name))
else:
    print(f"{name} Not found in the class; so adding {name} ")
    stud_name.append(name)

### EXERCISE 3 ###
"""
Whenever I'm shopping and I buy some bread I always forget to buy butter. 
Create a list and if 'bread' is in the list, add 'butter' to the shopping list.

Try running the program with and without bread in the list to check that your program works.

Remember the in operator checks if an item is in a list and the .append() method adds an item to a list.
"""
shopping_list = [
'bread',
    'cheese',
    'pop tarts',
    'carrots',
]
# item = input("Item to check:")
item = 'bread'
if item in shopping_list:
    print(f"{item} in the list, so adding butter")
    shopping_list.append("butter")
print(shopping_list)

### DEMO 4 ###
"""
Using lists and for loops together
"""
for item in shopping_list:
    print(item)
### EXERCISE 4 ###
"""
I want to work out how much money I've spent on lunch this week. I've created a list of what I spent each day.
Write a program that uses a for loop to calculate the total cost
"""

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0
for cost in costs:
    total_cost += cost
print("Total Cost:",round(total_cost,2))
print("Using sum:",round(sum(costs),2))

### DEMO 5 ###
"""
Using FOR LOOP to create a new list
"""
low_cost = []
low_cost = [ item_cost for item_cost in costs if item_cost<2 ]
print(low_cost)
double_cost = [ item_cost*item_cost for item_cost in costs ]
print(double_cost)

### EXERCISE 5 ###
"""
write a list comprehension expression to build a new list of EVEN numbers ONLY from range(5)

your sample output should be [0, 2, 4]
"""

new_list = [num for num in range(5) if num%2 == 0]
print(new_list)

### DEMO 6 ###
"""
Values in a dictionary are accessed using their keys
"""
person = {
    'name': "Jyothy",
   'Age': 38,
    'Gender': 'F',
    'Height' : 154,
    5:'Five'
}
print(person)
print(person['name'])
print(person[5])
### EXERCISE 6 ###
"""
 Print the values of name, post_code and street_number from the dictionary
"""
address = {
    'name':"John",
    'post_code':"LN 12A",
    'street_number':32,
    'location': {
        'lat':127,
        'long':33
    }
}
print(address)
print("Address:",address['name'])
print("Post code:",address['post_code'])
print("Street number:",address['street_number'])
print("Location:", address['location'])
### DEMO 7 ###
"""
Dictionaries in Lists --> Putting dictionaries inside a list is very common
"""
people = [{'name':'apple','cost':20},{'name':'pear','cost':18},{'name':'Orange','cost':15}]
for i in people:
    print(f"{i['name']} : {i['cost']}" )
### EXERCISE 7 ###
"""
Using a for loop, output the values name, colour and price of each dictionary in the list
"""
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]
for fruit in fruits:
    print(f"{fruit['name']} {fruit['colour']} {fruit['price']}")

### DEMO 8 ###
"""
Random choice -- The choice() function in the random module returns a random item from a list
"""

### EXERCISE 8 ###
"""
Write a program to create a random name. 
You should have a list of random first-names and a list of last-names. 
Choose a random item from each and display the result.

Extension: Using list of verbs and a list of nouns, create randomised sentences
"""
import random
possible_names = ['Anete', 'Emily', 'Jane', 'Do', 'John']
possible_last_n = ['Zepa', 'Rand']
print(f"{random.choice(possible_names)} {random.choice(possible_last_n)}")

### DEMO 9 ###
"""
Tuple examples -- immutable
- allow duplicates
"""
order = ('croissant','coffe','juice')
for i in order:
    print(i)
print(order.count('coffe'))
print(order.index('coffe'))
### DEMO 10 ###
"""
Set examples :unoredered, unindexed, no duplicates
"""
my_set = {1,2,3,4,5,'hi',9}
my_set.add('welcome')
print(my_set)

my_set = {1,2,3,4,5, 'hi', 7}
my_set.add(44) #adding adds at the end but different to apend
print(my_set)
#
for i in my_set:
   print(i)

ls = [1,2,3,4,5,2,3,4,7]
my_set_from_ls = set(ls)
print(my_set_from_ls)