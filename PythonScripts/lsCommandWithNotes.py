import maya.cmds as cmds
#-----------------
# ls command
#-----------------

# Returns a filtered list of objects based on the flags we pass in

cmds.ls() # Returns all objects in the scene

cmds.ls(transforms=True) # Returns all transform nodes in a scene

cmds.ls(shapes=True) # Returns all shape nodes in a scene

cmds.ls(cameras=True) # Returns all camera nodes in a scene

selection = cmds.ls(selection=True) # Returns all selected objects -sl

for sel in selection:
    cmds.setAttr("{0}.v".format(sel), False) # Grabs all items in the selection sets their visibility (or .v property) to false making them invisible

for sel in selection:
    cmds.setAttr("{0}.v".format(sel), True) # Makes all selected items visible
    
test = cmds.ls(sl=True, showType=True) # Returns all selected items and also shows what type of object they are as a seperate item in the list. The type item will immediately follow whatever object it is showing its the type of  
print(test[1])

cmds.ls(type="mesh") # Returns all nodes in scene with type "mesh" otherwise known as shape nodes
cmds.ls(type="transform") # Returns all nodes in scene with type "transform"
cmds.ls(assemblies=True) # Returns all top level nodes in outliner
cmds.ls(references=True) # Returns all references to the file
cmds.ls("persp") # Returns all objects name "persp" in scene
cmds.ls("p*", transforms=True) # Returns all transform nodes that start with the letter p (does not have to be of length > 1)
cmds.ls("*Cube*", transforms=True) # Returns all transform nodes that contain the word Cube (Case sensitive) in it
