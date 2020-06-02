import maya.cmds as cmds

#----------------------------
# Lists
#----------------------------

a = []

b = [0,1,2,3,4]

c = [3.14, "abc", [1,2,3,4]] # A list with a nested list. Remember len(c) would return 3 because the nested list counts as a single object. len(c[2]) would return 4 though

d = list("Python") # Returns ['P', 'y', 't', 'h', 'o', 'n']

e = list(range(0,10)) # Returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


b + c # Returns [0, 1, 2, 3, 4, 3.14, 'abc', [1, 2, 3, 4]] remember order matters in string concatenation

c + b # Returns [3.14, 'abc', [1, 2, 3, 4], 0, 1, 2, 3, 4]

b * 3 # Returns [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

3.14 in c # This is a membership check, returns True or False if the element is in the list

1 in c # Returns False 

1 in c[2] # Returns True

# Since lists are mutable if we run the below code

b[2] = 28

print(b) # b will maintain the changed value

c[0][0] # Returns 1 the second square brackets allows us to access specific values in the nested list. You can keep adding square brackets for each level of nested lists you wish to access

c[1:] # Returns ['abc', [1, 2, 3, 4]]



e1 = ["a","b","c"]
f1 = ["1","2","3"]

e2 = ["a","b","c"]
f2 = ["1","2","3"]

e1.append(f1) # Result: ['a', 'b', 'c', ['1', '2', '3']] # append adds whatever object you are appending as an object of the list
e2.extend(f2) # Result: ['a', 'b', 'c', '1', '2', '3'] # extend will see if the object is a list and if so it will add every single value of the argument list as their own object in the list


g = []
g.append("Python") # Result: ['Python'] #
g = []
g.extend("Python") # Result: ['P', 'y', 't', 'h', 'o', 'n'] #

h = [1,2,3]
h.insert(0,"a") # Result: ['a', 1, 2, 3] # insert will add whatever second argument "a" in this case at the specified index "0" in this case and shift every item in the list to the right of 0 one index over

if "a" in h:
    h.remove("a") # Removes specified item from list but throws an error if the item is not in the list so safe to always check to see if it exists before you remove it

del h[0] # Removes specified index from list and all items to the right of this index move back one index spot


#----------------------------
# Sorting Lists
#----------------------------

# There are two ways to sort a list. 
# 1.In place sort method
a.sort()
# 2. Sorted function
sorted(a)

# The difference being that a.sort() will change a to stay sorted after its called, sorted(a) would return a sorted list but after you call a again it won't maintain the sort change

a.sort(reverse=True) # Descending Sort
sorted(a, reverse=True) # Descending Sort

i = ["dog", "cat", "DOG", "CAT"]

i.sort() # Result: ['CAT', 'DOG', 'cat', 'dog'] when sorting strings, the priority is case sensitive then letter order 