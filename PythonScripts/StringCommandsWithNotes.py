import maya.cmds as cmds
import os

#-----------------------------
# Strings
#-----------------------------

# Python strings are immutable, which means they cannot be changed after they are created. Strings can be manipulated but the results will be a new string object

empty_string = ''

single_quotes = 'String literal in single quotes'

double_quotes = "String literal in double quotes"

escape_sequence = "\tInsert tab \nInsert new line"

# Documentation quotes (triple quotes) are used to associate documentation with a specific module, function, class, or method
doc_string = """ This is a doc string """

# Concatenating string combines them into a new string object 
s1 = "hello "
s2 = "world"
concatenate = s1 + "my " + s2


# Repetition will repeat a string the number of times specified
s1 * 10

# Iterating over a string
for c in s1:
    print(c)

# Search for a char or a substring in a string will return a True or False boolean

"h" in s1 # Returns True
"h" in s2 # Returns False
"hel" in s1 # Returns True

# len function returns string length
number_of_chars = len(s1)


# Indexing
s1[0] # Return first char in string
s1[1] # Returns second char in string
s2[-1] # Returns last char in string
s2[-3] # Returns 3rd char from the end of a string

# Slicing
test = "abcdefg"
test[0:3] # Returns abc returns chars from the first char to the third char (3 is the 4th index spot but it is non inclusive for the second spot)
test[2:5] # Returns cde

test[2:] # Returns cdefg, starts from third char and goes to the end
test[:3] # Returns abc, starts from beginning and goes to third char
test[:-1] # Returns abcdef full string besides last char
test[-1:] # Returns g only the last char

test[0:5:2] # Returns ace, third number is the step pace which determines the rate your slicing moves through the string, since it is 2 here it grabs every second char in a range of 0:5

test[::-1] # Returns gfedcba, since the step is negative it goes backwards through the string 


#String Functions
s1.upper() # Returns a new string object that changes all letters in string to be uppercase
s1.lower() # Returns a new string object that changes all letters in string to be lowercase

s1.isupper # Returns true if all letters are upper case
s1.islower # Returns true if all letters are lower case

heyo = "whoopwhoopwhoop"
heyo.find("whoop") # Returns starting index of the first time the substring "whoop" is found in the variable heyo

num = "1"
num.isdigit() # Returns True if the string num is a digit
num.zfill(4) # Returns 0001, pads the number you give it till it contatins that many digits, useful for scripts dealing with numbering renders or autosaves

s1.split(' ') # Returns a list of strings that are split up based on whatever is passed into the function, in this case its splits up a string into multiple strings that have spaces in between them


s3 = "test_my_ string"
s3.split('_') # Returns ['test', 'my', ' string']


test2 = "Maya is Cool" 
test2 = "m" + test2[1:] # Since strings are immutable we have to be clever how we change the string value and maintain the variable

test2 = test2.replace("Cool", "Awesome") # Another way is to use functions


# os.environ grabs all paths that are under the argument Enviroment Variable
paths = os.environ["MAYA_SCRIPT_PATH"]
# They are seperated by ; so split for readability
paths = paths.split(";")
# Iterate over the paths for a nice clean new line output
for p in paths:
    print(p)

#-----------------------------
# Escape Sequences
#-----------------------------

# \n when printed acts as a new line
print("newline: \n")
print("line 1\nline 2\nline 3\n")

# \t when printed acts as a tab
print("tab \t")
print("line 1\n\tline 2\n\t\tline 3\n")

# \" is used when you want to have a double quote as a character inside of your string
print("double quote: \"")
print("this \"is\" a string")

# \\ is used when you want to have a backslash a character inside of your string without it being confused as the start of an escape sequence
print("backslash: \\")
print("C:\\new_folder")

# Raw String starts with r and then the string and will not need the use of escape sequences
r"C:\new_folder"



#-----------------------------
# String Formatting
#-----------------------------

a = 1
b = 2 
c = 4.123

"The sum of a + b is {0}".format(a+b) # Returns "The sum of a + b is 3"
"a: {0} b: {1} c: {2}".format(a,b,c) # Returns "a: 1 b: 2 c: 4.123"
"a: {0:04d}".format(a) # Returns "a: 0001" :04d is saying to format the string to 4 digits similar to the zfill function
"c: {0:0.2f}".format(c) # Returns "c: 4.12" :0.2f is saying to format the string to a two decimal float it will round the value 

"The sum of a + b is %s"%(a+b) # Returns "The sum of a + b is 3" but this way is depecrated in Python 3 so its less common

"c: %0.2f" # Returns "c: 4.12" :0.2f is saying to format the string to a two decimal float it will round the value. This way is also depecrated in Python 3 
