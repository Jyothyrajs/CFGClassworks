import csv

field_names = ['name', 'age']

data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
    {'name': 'John', 'age': 48}
]

with open('team2.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)
    print("Success")
#
import csv
with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    print(spreadsheet)
    for row in spreadsheet:
        print(row)
    print("Read Success")

#
# ### EXERCISE 2 ###
# """
# This program is supposed to read data about trees from a file to find the shortest tree.
# Complete the program adding code to open 'trees.csv'.
# ​
# The trees.csv file included with your student guides.
# Save the csv file in the same folder as your Python program!
# """
#
import csv
heights = []
column_names = []
with open('trees.csv','r') as csv_file:
    spreadsheet =csv.DictReader(csv_file)
    # for row in spreadsheet:
    #     column_names.append(row)
    #     break
    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)
    # table_keys = column_names[0].keys()
    # for item in table_keys:
    #     print(item)
    print(heights)
    print(min(heights))

#
#
# for row in spreadsheet:
#     tree_height = row['height']
#     heights.append(tree_height)
#
# shortest_height = min(heights)
# print(shortest_height)
#
# import csv
# with open('trees.csv', 'r') as csv_file:
#     spreadsheet = csv.DictReader(csv_file)
#     heights = []
#     for row in spreadsheet:
#         tree_height = row['height']
#         heights.append(tree_height)
#     shortest_height = min(heights)
#     print(shortest_height)
#     # min_ht = 0
#     # for row in spreadsheet:
#     #      tree_height = row['height']
#     #      if ( tree_height < )
#
#
# ### EXERCISE 3 ###
# """
# PROBLEM SOLVING WITH PYTHON -->
# ​
# Write a Python program to count the occurrences of a word in a text file.
# Your program will take a word from the user and count the number of occurrences of that word in a file.
# ​
# (use file: 5.3_example_one.txt, save this file in the same folder as your Python program! )
# """
# counter = 0
# file_name = input("Input file path:")
# myword = input("Enter word")
# with open(file_name,"r") as myfile:
#     content = myfile.read()
#     occ = content.count(myword)
#     print(occ)
#
# with open(file_name,"r") as myfile:
#     for line in myfile:
#         line.strip()
#         words = line.split()
#         for word in words:
#             if(word == myword ):
#                 counter += 1
#     print(counter)