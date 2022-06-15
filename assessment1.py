with open('Todo.txt') as fh:
	text = fh.read()
  	count = 0
	for i in text:
		if i >='A' and i <= 'Z':
			count = count + 1
	print(count)


def reverese_str(myStr):
	print(myStr[::-1])

mystring = input("String to reversse:")
reverese_str(mystring)



# print(max(my_list))
def max_element(my_list):
	max_len = 0
	for i in (my_list):
		c_item = i
		c_len = len(c_item)
		if( c_len > max_len):
			max_item = c_item
			max_len = c_len
	return max_item

my_list = ['cat','Horse','elephant','dog','ABCDEFGRT']
max_item = max_element(my_list)
print(max_item)

def add(x,y):
	return x + y
def subtract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	return x/y

choice = int(input("Select your choice \n 1: Addition \n 2: Subtraction\n3:Multiplication \n 4:Division \n 0:Exit "))
if choice >= 1 and choice <= 4:
	num1 = int(input("First Number:"))
	num2 = int(input("Second Number:"))
	if choice == 1:
		result = add(num1,num2)
	elif choice == 2:
		result = subtract(num1, num2)
	elif choice == 3:
		result = multiply(num1, num2)
	else:
		result = divide(num1, num2)
	print("Result :",result)
else:
	print("Invalid choice")

s = 'Hello'
print(s.count('l'))
print(s.count('h'))
print(s.count('H'))


print(chr(88))
print(ord('c'))

s = '2020-11-10_sales.csv'
print (s[:-4])

l = ['A']
l.append(3)
print(l[0])
k = ('l')
print(k[0])
languages = ['French', 'English']

# another list of language
languages1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
languages.extend(languages1)

d = {'A':1}
d['k'] = 3
print(d)