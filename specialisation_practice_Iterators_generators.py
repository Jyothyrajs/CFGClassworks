
"""
Using a generator comprehension, define a generator for the series:

(0, 2).. (1, 3).. (2, 4).. (4, 6).. (5, 7)
"""

series = ((i,i+2) for i in range(0,10) if i != 3)
for item in series:
    print(item)

even_gen = ((i for i in range(100) if i%2 == 0))
for item in even_gen:
    print(item)

categ = (("apple" if i < 3 else "pie") for i in range(5))
print(categ)
for i in categ:
    print (i)

# Read a large file

def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

print(csv_reader("team2.csv"))


# Row count of file

def csv_file_count(file_name):
    csv_gen = csv_reader(file_name)
    row_count = 0
    for row in csv_gen:
        row_count += 1
    return row_count

file_line_len = csv_file_count("team2.csv")
print("No of lines:",file_line_len)


def csv_reader(file_name):
    for row in open(file_name,"r"):
        yield row

print(csv_reader("team2.csv"))

csv_gen = (row for row in open("team2.csv","r"))
print(next(csv_gen))
print(csv_gen.__next__())

# Row count of file

def csv_file_count(file_name):
    csv_gen = csv_reader(file_name)

    row_count = 0
    for row in csv_gen:
        row_count += 1

    return row_count

file_line_len = csv_file_count("team2.csv")
print("No: of lines:",file_line_len)

# Generate infinite sequence

def gen_infinite_seq():
    num = 0
    while True:
        num += 1
        print(num, end = " ")

gen_infinite_seq()

def gen_infinite_seq():
    num = 0
    while True:
        num += 1
        yield num

seq = gen_infinite_seq()
print(seq)
for i in range(5):
    print(next(seq))