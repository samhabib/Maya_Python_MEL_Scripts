#-----------------------------------
# Python Core Data Types
#-----------------------------------

# In Python everything is an object in the sense that it can be assigned to a variable or be passed into a function as an argument

# Integers
100
-4

# Floating Point Numbers or Floats
10.34
-3.523

# Octal (base 8)
0177

# Hex (base 16)
0xffff

# Binary (base 2)
0b110011

# Complex Numbers
3+4j
2j
2.0+2.0j

# Strings
"Hello World"
"Test Test"

# Lists
[1,2,3]
["abc",["a","b","c"],1]

# Dictionaries
{"a":1,"b":2,"c":"abc"}

# Tuples (Difference between list and tuples is that a tuple cannot be changed after its created 
(1,2,3)

# Files
test_file = open("readme.txt","r")

# Others
None
True
False

# Using the python "type" function tells you what type an argument passed into it is
type(100) # would return Result: <type 'int'>

# Valid variable names can be made up of numbers, letters, or underscores
a = 3
test_variable_01 = 1
_my_name = "Sam"

# Invalid variable names (variables cannot start with numbers or be named after certain keywords like print or True)
01_test = 123
print = 456


#-----------------------------------
# Python Operators
#-----------------------------------

5 + 5 # = 10
5 - 2 # = 3
5.5 * 2 # = 11.0 if float in expression then result will be a float
20 / 10 # = 2
15 % 2 # = 1 % or modulus returns the remainder of 15/2 otherwise 1

#Truncation occurs if there is no float in the division expression, to get the correct value you must use a float in the expression
3 / 2 # = 1
3 / 2.0 # = 1.5 

a = 5
b = 3
a / b # = 1
a / float(b) # = 1.6666666666666667 #
int(2.5) # = 2
5 // 2.0 # = 2.0 the double slash // is the floor operator so it rounds down in division

# Order of Operations takes place in Python

# Comparison

10 > 2 # = True

2 > 10 # = False

2 >= 2 # = True

10 != 10 # False

9 != 10 # True

10 == 1- # True

a = 5 
b = 3
if(a > b):
    # do something
    pass
else:
    # do something else
    pass