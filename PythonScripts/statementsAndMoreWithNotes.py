import maya.cmds as cmds
import maya.OpenMaya as om

#--------------------
# Statements
#--------------------

# Assignment
a = 10
b = "python"

# Print Statement
print("Heyooo")

# If/Else

if a < 10:
    print("less than")
elif a == 10:
    print("equals")
else:
    print("greater than")


if None: # None is equivalent as False in if/else statements
    print("Will never show")
    
test1 = "Hello"
test2 = ""

if test1: # This returns a True statement because the string is not empty
    print("This is a True Statement")
else:
    print("This is a False Statement")


if test2: # This returns a False statement because the string is empty
    print("This is a True Statement")
else:
    print("This is a False Statement")
    
list1 = ["hey"] # Will evaluate to True in a if/else
list2 = [] # Will evaluate to False in a if/else

dict1 = {"hey":1} # Will evaluate to True in a if/else
dict2 = {} # Will evaluate to False in a if/else
    
tuple1 = (1) # Will evaluate to True in a if/else
tuple2 = () # Will evaluate to False in a if/else

num1 = 0 # Returns False
num2 = 1 # Returns True
num3 = 100000 # Returns True

# For Loop
for x in range(0,10):
    if x % 2:
        continue # Continue execution of loop
    else:
        print(x)
        
# While Loop
while True:
    if exitLoop():
        break # Exit the loop


# Function
def add(input_a, input_b):
    return input_a + input_b # Return Statement, if you do not define a return value then the function will return None
   
    
# Arguments with an "=" and value are called default arguments which means if you dont pass in a value it will use the default value for that argument
def create_sphere(tx, ty, tz, sx=10, sy=10, sz=10): 
    print("translate ----> {0}, {1}, {2} //".format(tx,ty,tz))
    print("scale ----> {0}, {1}, {2} //".format(sx,sy,sz))
    
create_sphere(1,2,3) # uses default values for sx sy and sx
create_sphere(1,2,3,4,5,6) # doesnt use any default values
create_sphere(1,2,3,sz=100) # This is a keyword argument to specify you want dont want to use the default value of sz. KEYWORD ARGUMENTS MUST GO AFTER NORMAL ARGUMENTS CANNOT BE BEFORE THEM

# Pass By Reference

def num_swap(number):
    number=80
    print(number)

my_num = 4
print("Before ---> {0}".format(my_num))
num_swap(my_num) # Function does not change number in variable outside of function
print("After ---> {0}".format(my_num))


def pass_by_reference(a_list):
    a_list.append("4")
    a_list.append("5")
    a_list.append("6")
    
my_list = [1,2,3]

print("Before ---> {0}".format(my_list))
pass_by_reference(my_list) # Function DOES hold new numbers appended to it after function. This happens because the object doesnt change and we are still looking at its reference in memory so the container is in the same place but the inside of the container changes
print("After ---> {0}".format(my_list))
    

def pass_by_reference2(a_list):
    alt_list = list(a_list) # To make function not hold changes, we need to copy the list and edit that one in the function. 
    alt_list.append("4")
    alt_list.append("5")
    alt_list.append("6")
    
my_list = [1,2,3]

print("Before ---> {0}".format(my_list))
pass_by_reference2(my_list)
print("After ---> {0}".format(my_list))
    
    
    
# Import Statement
import os
import maya.cmds as cmds


sel = cmds.ls(sl=True)

if len(sel) >= 2:
    for s in sel:
        print(s)
elif len(sel) == 1:
    print("Please select another object")
else:
    print("No objects selected")
    
    
    
True and True # Returns True
True and False # Returns False
False and False # Returns False
True or True # Returns True
True or False # Returns True
False or False # Returns False

# Order of Operations gives "and" a higher priority than "or" so it will always do a "and" before the "or"s unless you use parenthesis

True and False or True # Returns True
True or True and False # Returns True 
(True or True) and False # Returns False 



# Errors
cmds.error("This is an error") # Errors will stop your scripts at where they are and throw a Python exception
om.MGlobal.displayError("This is a display error") # displayErrors will NOT stop your scripts and wont throw a Python exception

# Warnings
cmds.warning("This is a warning") # Warnings will NOT stop your scripts
om.MGlobal.displayWarning("This is a display warning") # No difference between cmds.warning and om.MGlobal.displayWarning

# Info
print("This is an info statement") # Does not display in Maya 
om.MGlobal.displayInfo("This is a display info statement") # Does display in Maya





sel = cmds.ls(sl = True)
children = cmds.listRelatives(sel, children=True) # returns all first level children of selected objects

frame = cmds.currentTime(query=True) # Returns current frame you are on in animation time slider 

for child  in children:
    if child.startswith("pC"):
        attr = "{0}.ty".format(child)
        cmds.setAttr(attr, frame)
        
hi = 0
hi += 1 # Adds 1 to hi and reassigns it to hi so basically is "hi = hi + 1
hi -= 1 # Subtracts 1 to hi and reassigns it to hi so basically is "hi = hi -1"

my_string = "Python"

while my_string: # Constantly removes the first letter of the string until it is an empty string which is considered False in the while loop check
    print(my_string)
    my_string = my_string[1:]
    
    
    
print(cmds.about(version=True)) # Prints what version maya you are using