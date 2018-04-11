# randomSpheres.py

import maya.cmds as cmds
import random

random.seed(1234)

result = cmds.polySpheres(r = 1, name = 'mySphere#')

transformName = result[0]

instanceGroupName = cmds.group(empty = True, name = transformName + '_instance_grp#')

for i in range(0, 50):

    instanceResult = cmds.instance(transformName, name = transformName + '_instance#')

    cmds.parent(instanceResult, instanceGroupName)

    x = random.uniform(-10, 10)
    y = random.uniform(0, 20)
    z = random.uniform(-10, 10)

    cmds.move(x, y, z, instanceResult)

    xRot = random.uniform(0, 360)
    yRot = random.uniform(0, 360)
    zRot = random.uniform(0, 360)

    cmds.rotate(xRot, yRot, zRot, instanceResult)

    scalingFactor = random(.3, 1.5)

    cmds.scale(scalingFactor, scalingFactor, scalingFactor, instanceResult)

cmds.hide(transformName)

cmds.xform(instanceGroupName, centerPivots = True)
