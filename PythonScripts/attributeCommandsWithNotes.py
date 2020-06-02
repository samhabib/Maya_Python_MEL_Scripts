import maya.cmds as cmds

cmds.polyCube(n="cube")

# Returns translate X value of object named "cube"
cmds.getAttr("cube.translateX")

# Returns translate X,Y,Z value of object named "cube"
cmds.getAttr("cube.translate")

# Returns boolean whether translate X (tx is shorthand flag name) is locked
cmds.getAttr("cube.tx", lock=True)

# Returns boolean whether translate X is Keyable
cmds.getAttr("cube.tx", keyable=True)

# Returns boolean whether cube is visible
cmds.getAttr("cube.visibility")


# Selecting an object means you dont have to specify the name of the object when you do the getAttr call. Still need to do the Period "." tho
cmds.select("cube")
cmds.getAttr(".tx")


cmds.polySphere(n="sphere")

# Sets sphere tx to 10
cmds.setAttr("sphere.tx", 10)

# Sets sphere tx to 20
cmds.setAttr("sphere.tx", 20)

# Sets sphere rotate x, y, and z values to 10, 20, 30 respectively. Specifying type is sometimes necessary
cmds.setAttr("sphere.rotate", 10, 20, 30, type="double3")

# Locks sphere's tx value
cmds.setAttr("sphere.tx", lock=True)

# Unlocks sphere's tx value
cmds.setAttr("sphere.tx", lock=False)

# Makes sphere's tx value not keyable and hides it from channel box
cmds.setAttr("sphere.tx", keyable=False)

# Makes sphere's tx value keyable and places it back in the channel box if it was removed
cmds.setAttr("sphere.tx", keyable=True)