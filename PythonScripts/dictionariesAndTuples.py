import maya.cmds as cmds

#----------------------------
# Dictionary
#----------------------------

# Dictionaries are mutable which means they can be changed

# Indexing
d = {} # Empty Dictionary

d = {"red":255,"green":0,"blue":255} # Dictionary with three items

d["red"] # Returns 255
d["green"] # Returns 0

d["blue"] = 155

d["blue"] # Returns 155

d["black"] # Returns error because there is no black key
d.get("black") # Returns None because the key does not exist thus making it Error safe  

# Membership

"cyan" in d # Returns False
"blue" in d # Returns True

d.keys() # Returns list of contained keys
d.values() # Returns list of contained values
d.items() # Returns list of (key,item) tuples contained in the dictionary

for key in d.keys(): # Prints values of dictionary
    print(d[key])

for item in d.items(): # Prints key ----> values of dictionary
    print("{0} ---> {1}".format(item[0], item[1]))


#----------------------------
# Tuples
#----------------------------

# Tuples are immutable

# Empty tuple
t = ()

# Two item tuple
t = (5, "abc")

t[0] # Returns 5

t[0] = 2 # Throws an error