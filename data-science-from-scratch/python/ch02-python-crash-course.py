## Modules (p. 19)
import re
my_regex = re.compile("[0-9]+", re.IGNORECASE)
print("search:", my_regex.search("abc123def"))
# search: <re.Match object; span=(3, 6), match='123'>

from collections import defaultdict
lookup = defaultdict(int)


## Functions (p.20)
def double(x):
    "Doubles given number"
    return \
        x * x

print(double(4))

# higher-order function
def apply_to_one(f):
    return f(1)

print(apply_to_one(lambda x: (x + 1) * (x + 2)))

# lambda can be applied to the args immediately too
print((lambda x: x + 1) (10))

# default arguments
def my_print(message = 'my default'):
    print('Hello', message)

my_print()


## Strings (p.21)
#################

len('len tak tak')

# formatted strings (f-strings)
first_name = 'Juraj'
last_name = 'Martinka'
print(f"Hello {first_name} {last_name}")


## Exceptions
try:
    1 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')

## Lists

# define a list and print every third element
my_list = [1, 2, 3, 5, 7, 11, 15, 16, 17]
my_list[::3]

# modify the list
x = [1,2,3]
x.extend(range(10))
x.append(101)
x

# this gives ValueError if the number of items doesn't match
# "not enough values to unpack" or "too many values to unpack"
a,b = [1,2]
print(a, b)


## Tuples - like lists but you cannot change them

(1,2)[0]

#(1,2)[1] = 20
# TypeError: 'tuple' object does not support item assignment

def sum_and_product(x, y):
    return (x + y), (x * y)
a,b = sum_and_product(100, 200)
print(a, b)


## Dicstionaries

empty_dict = {}
grades = {"Joel": 80, "Tim": 95}

# you get a KeyError for keys ont present in the dictionary
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

# membership check
"Tim" in grades

# can I use lists as keys?
xkey = [1,2,3]
# Not possible: TypeError
# {xkey: "XX"}