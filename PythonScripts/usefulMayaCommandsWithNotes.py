import maya.cmds as cmds

# Create Polygon Sphere
cmds.polySphere()

# Create Polygon Sphere with name Sam_Test_GEO
cmds.polySphere(n ="Sam_Test_GEO")

# Create Polygon Sphere with radius of 10
cmds.polySphere(radius = 10)

# Help Command for polySphere command. Will return 3 columns of info. 1. Flag Shorthand 2. Flag Fully Written Out 3. Data Type flag takes
print cmds.help("polySphere")


# There are 3 types of commands Create, Edit, Query. If a flag is not specified it defaults to Create, to specify a different type of command you have to set that flag to equal True


# Query Command for radius of polySphere1
print cmds.polySphere("polySphere1", query=True, radius=True)

# If else Query command that changes result based on whether radius equals a certain value
if( cmds.polySphere("polySphere1", query=True, radius=True) == 1.0):
    print("Heyo")
else:
    print("Whop")    
    
# Edit command to change polySphere1's radius to equal 5

cmds.polySphere("polySphere1", edit = True, radius = 5)

# Repeat of the older Query command if/else returns a new answer after we tweaked the radius
if( cmds.polySphere("polySphere1", query=True, radius=True) == 1.0):
    print("Heyo")
else:
    print("Whop") 


# Returns EVERY NODE in the scene, usually want to use a filter to narrow down to just shapeNodes, or just cameras, etc.
print(cmds.ls())

# Filters for all shapes in the scene
print(cmds.ls(shapes=True))

# Filters for all cameras in the scene
print(cmds.ls(cameras=True))

# Filters for all currently selected items in the scene
print(cmds.ls(selection=True))

# Selects pShere1 in the scene
cmds.select("pSphere1")

# Deselects all items in the scene
cmds.select(clear=True)

# Adds pSphere2 to the current selection
cmds.select("pSphere2", add=True)

# Replaces whatever is currently selected with Sam_Test_GEO
cmds.select("Sam_Test_GEO", replace=True)
