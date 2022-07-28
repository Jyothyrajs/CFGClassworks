import re
"""
Regular expressions are tiny specialized programming language embedded inside python and made available through re module.
Regular expressions patterns are compiled into a series of byte codes which are executed by a matching engine written in C.
It can be used as sequence of characters that form a search pattern.
import re module inorder to work with regular expressions
"""
"""
Regular expression functions:
    search : Returns a match object if there is any match anywhere in the string
    findall : returns a list containing all matches 
    split   : Returns a list where the string has been split at each match
    sub : Replaces one or more matches with a string
    match : checks if RE matches at the beginning of the string
    finditer - Find all matches of RE in the string and returns them as an iterator

match methods/Attribute:
  group() - return the string matched by RE
  span() - Returns the tuple containing start and end positions of the match
  start() - Returns the starting position of the match
  end() - returns the ending position of the match  
"""

"""
Search 
Return : first match object with span
"""
# Exercise 1
pattern = "pattern"
my_str = "It's pattern matching with regular expression"
res = re.search(pattern,my_str)
print(res)

# Exercise 2
pattern = "\d{3}"
my_str = "It's pattern matching with regular 103 expression in 2022"
res = re.search(pattern,my_str)
print(res)

# Exercise 3
pattern1 = "[0-9]+"
pattern2 = "[0-9][1-7]"
my_str = "It's pattern matching with regular 103all expression in 2022"
res = re.search(pattern1,my_str)
print(res)
res = re.search(pattern2,my_str)
print(res)



"""
match : checks if RE matches at the beginning of the string

"""
pattern = "It['i]s"
my_str = "It's pattern matching with regular 103 expression in 2022"
res = re.match(pattern,my_str)
print(res)

"""
findall - Returns a list containing all the matches
"""
pattern1 = "[0-9]+"
pattern2 = "[0-9][1-7]"
my_str = "It's pattern matching with regular 103all expression in 2022"

res_findall = re.findall(pattern1,my_str)
print(res_findall)
res_findall = re.findall(pattern2,my_str)
print(res_findall)

"""
finditer - Find all matches of RE in the string and returns them as an iterator
"""
pattern1 = "[0-9]+"
my_str = "It's pattern matching with regular 103all expression in 2022"

res_finditer = re.finditer(pattern1,my_str)
for i in res_finditer:
    print(f"{i.group()} spans { i.span()}")

"""
split : returns a list 
"""
pattern = "^I"
my_str = "It's learning Regex"
words = re.split(pattern,my_str)
print(words)
res_search = re.search(pattern,my_str)
print(res_search)
res_findall = re.findall(pattern,my_str)
print(res_findall)

pattern = "\d"
my_str = "It4's lear6dning Re8gex"
words = re.split(pattern,my_str)
print(words)
res_search = re.search(pattern,my_str)
print(res_search)


"""
sub: replaces the matches with the given string
syntax:

sub(<pattern>, <replace string>,<text>,count)
"""
# Exercise

pattern = "\d"
my_str = "It4's lear6dning Re8gex"
new_str = re.sub(pattern,"\t",my_str)
print(new_str)

"""Compilation Flags:
ASCII,A - match only ASCII characters
DOTALL,S - match any character including newline
IGNORECASE, I - Do case insensitive matches
LOCALE,L - Do a locale aware match
MULTILINE,M - Do the match at the beginning of the string and at new line
VERBOSE,X - allows to specify expression in more readable form

"""
"""Compile and Ignore case"""

pattern = '(ab)*'
my_str = "abbcabb"
p = re.compile(pattern)
res = p.match(my_str)
print(res)

my_str = "aBbcabb"
p = re.compile(pattern,re.I)
res = p.match(my_str)
print(res)

# #####################################################
#
# # EXAMPLE 8 --- PRACTICAL EXAMPLE
#
# """
# We have a list of mock trade ids that need to be processed, so that we
# extract the date string from each id
# """
# pattern = ".*(\d{8}-\d{5})$"

#
trade_ids = [
    "ghjd-gfjv-20220615-12345",
    "vbfd-dusi-20181103-11111",
    "pomm-xxsa-20041222-22222",
]
# '''
# Match and extract a date in a trade id. Might be good idea to compile the pattern#
# '''
#
pattern = ".*(\d{8})"
patt = re.compile(pattern)
res = []
for i in trade_ids:
    res.extend( patt.findall(i))
print(res)

# Using lambda & map
import datetime
dates = []
res = list(map(lambda trade:patt.findall(trade),trade_ids))
for i in res:
    dates.extend(i)
# for i in dates:
#     datetime.datetime.strptime("%d%m%Y").date()
print(dates)
