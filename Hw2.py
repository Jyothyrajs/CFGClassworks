# Task3 :
# Question 1
chairs = '15'
nails = 4
total_nails = chairs * nails #Convert the chairs into integer
message = 'I need to buy {} nails'.format(total_nails)
print(message)

# Question 2
my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# Question 2
# box_count = int(input("Number of boxes:"))
# eggs_per_box = int(input("Number of eggs per box:"))
# eggs_per_omelette = int(input("Number of eggs required for one omelette:"))
# omelette_count = (box_count * eggs_per_box ) // eggs_per_omelette
# print("You can make {} omelettes with {} boxes of eggs".format(omelette_count,box_count) )

# Question 4
# Complete a series of tasks to format strings

# Task 1 - Replace the (.) character with (!) instead. Output should be “I love coding!”

my_str = "I love coding."
my_str = my_str.replace( '.','!' )
print(my_str)
# Task 2
my_str_1 = "EVERY Exercise Brings Me Closer to Completing my GOALS."
my_str_1 = my_str_1.lower()
print(my_str_1)
# Task 3
my_str_2 = "We enjoy travelling"
ans_1 = (my_str_2[0] == 'A')
print(ans_1)
# Task 4
my_str_3="1.458.001"
# Type your code here:
ans_2 = len(my_str_3)
print(ans_2)

# Question 5
# Task 1: "thon".
wrd="Python"
ans_1 = wrd[2:]
print(ans_1)
# Task 2 - Slice the word until "o". (Pyth)
wrd="Python"
ans_1 = wrd[:4]
print(ans_1)

# Task 3 - Now try to get "th" only.
wrd="Python"
ans_1 = wrd[2:4]
print(ans_1)

# Task 4 - Now slice the word with steps of 2, excluding first and last characters

wrd="Python"
ans_1 = wrd[1:-1:2]
print(ans_1)

# Question 6
for number in range(4):
	output = 'o' * number
	print(output)
# Question 7
def calculate_vat(amount):
	return (amount * 1.2)
total = calculate_vat(100)
print(total)

# Write a new function to print a ‘cashier receipt’ output for a shop (any shop – clothes, food, events etc).
# It should accept 3 items, then sum them up and print out a detailed receipt with TOTAL.

# Question 8
# Input:
# Item_1_name = ‘Trainers’
# Item_1_price = 50.45
# Item_2_name = ‘T-shirt
# Item_2_price = 12
# Output:
# Trainers	50.45
# T-shirt	12.00
# TOTAL       	62.45



def cashier_receipt(item_count):
	items = [];
	for i in range(item_count):
		item = { }
		item_name = input("Item name :")
		item['name'] = item_name
		item_price = int(input("Item Price:"))
		item['price'] = item_price
		items.append((item))
	# print(items)
	total_cost = 0
	for i in items:
		total_cost += i['price']
		print(f"{i['name']}  {i['price']}")
	print("Total    ",total_cost)

no_of_items = int(input("No of items purchased : "))
cashier_receipt(no_of_items)




	# for i in range(item_count):
	# 	print(items[i])
	# item_1_name =  input("Item1 name :")
	# item_1_price = int(input("Item1 Price:"))
	# item_2_name = input("Item1 name :")
	# item_2_price = int(input("Item1 Price:"))
	# item_3_name = input("Item1 name :")
	# item_3_price = int(input("Item1 Price:"))