#Read operations

file = open('5.3_example_one.txt','r')
print(file)

# with readLine
file = open('5.3_example_one.txt','r')
content = file.readline()
print("Read with readline:",content)
file.close()

file = open('5.3_example_one.txt','r')
print("With for loop")
for i in range(4):
    print(i,file.readline())


file = open('5.3_example_one.txt','r')
content = file.read()
print("Read with readline:",content)
file.close()

content = file.read(2)
print("Read only specified chars:",content)

file = open('5.3_example_one.txt','r')
content = file.read()
print("With read:",content)
file.close()

file = open('5.3_example_two.txt','r')
content = file.readlines()
length = len(content)
print("Read with readlines:",content)
print("lines length:",length)
file.close()

file = open('5.3_example_two.txt','r')
content = file.readline()
print("Read with readline:",content)
file.close()

file1 = open('/Users/jyothyrajs/Downloads/report.csv','r')
print(file1)
file1.close()

file2 = open('/Users/jyothyrajs/Downloads/KS3.xlsx','r')
print(file2)
file2.close()

file3 = open('/Users/jyothyrajs/Downloads/KS3 (1).xlsx','r')
print(file3)
file3.close()

# pretty print

#Write operations
file = open('5.3_example_one.txt','w')
file.write("I am re writing the file")
file.close()

file = open('5.3_example_one.txt','a')
file.write("\ncat horse piggy fox")
file.write("\nEnd")
file.close()
# print(file)


#Using context manager
with open("5.3_example_two.txt",'r') as textfile:
    print(textfile)

file = open("movies.txt",'a')
file.write("Pay bills\n Read emails")
movie_quotes = [
    "\nI'm gonna make him an offer he can't refuse. (THE GODFATHER)",
    "\nMay the Force be with you. (STAR WARS)",
    "\nThere's no place like home. (THE WIZARD OF OZ)",
]
file.write(' '.join(movie_quotes))
print("Success")

### EXERCISE 1 ###
"""
Create a to-do list program that writes user input to a file
​
The program should:
​
Ask the user to input a new to-do item
Read the contents of the existing to-do items
Add the new to do item to the existing to-do items
Save the updated to-do items
​
NB: You will need to manually create a new file called todo.txt in the same folder as your program before you start.
"""

# You solution here

with open("Todo.txt",'a') as my_todo:
  my_todo.write("Check Channel\nReview Topics\n")

new_content = input("New item to do")
new_content += '\n'
with open("Todo.txt",'a+') as my_todo:
    prev_to_do = my_todo.read()
    to_do = prev_to_do + "\n" +new_content
    my_todo.write(to_do)

# while user_input:
#     user_question = input("Would you like to add an item to the list?\n")
#     if user_question.casefold() == 'y':
#         new_item = input("new item:")
#         if new_item in to_do_list:
#             print("This item is on the list")
#         else:
#             to_do_list.append(f"\n * {new_item}")
#     else:
#         user_input = False
#
# with open('todo.txt', 'a+') as to_do_file:
#     for item in to_do_list:
#         to_do_file.write(item)

with open('todo.txt', 'r') as file:
    contents = file.readlines()
    for item in contents:
        print(item)

#Find the word count in a file

word = "file"
count = 0
with open("lesson5.py",'r') as fp:
    for line in fp.readlines():
        if word in line:
            count = count+1
print(count)

word = "Git".lower()
count = 0
with open("hello.py",'r') as fp:
    for line in fp.readlines():
        print(line)
        line = line.lower()
        for char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            line = line.replace(char," ")
        words = line.split()
        print(words)
        for w in words:
            if w==word:
                count = count+1
print(count)