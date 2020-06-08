import maya.cmds as cmds
import maya.OpenMaya as om

#-----------------------
# twoItemVisibilityScrub.py
# ----------------------
# A simple script that takes a selection of two items and will make keyframe visibility 
# for one of them on Frame 1-2 and the other will be keyframed visibility Frame 2+
#
# Only intended to be used in Modeling stage because it makes use of frames which would mess with animations
#

# Performs the bulk of the work, sets the keyframe visibility on and off frames
def setVisibilityKeyframes(keyableObject, onVisibilityKeyframe, offVisibilityKeyframe):
    cmds.currentTime(onVisibilityKeyframe)
    cmds.setAttr("{0}.v".format(keyableObject), True)
    cmds.setKeyframe("{0}.v".format(keyableObject))
    cmds.currentTime(offVisibilityKeyframe)
    cmds.setAttr("{0}.v".format(keyableObject), False)
    cmds.setKeyframe("{0}.v".format(keyableObject))

selectedItems = cmds.ls(sl=True)
selectedItemsLength = len(selectedItems)
if(selectedItemsLength == 2):
    # Checks to see if items visibilities are keyable
    firstItemVisibilityKeyable = cmds.getAttr("{0}.v".format(selectedItems[0]), k = True)
    secondItemVisibilityKeyable = cmds.getAttr("{0}.v".format(selectedItems[1]), k = True)
    if(firstItemVisibilityKeyable and secondItemVisibilityKeyable):
        setVisibilityKeyframes(selectedItems[0], 1, 3)
        setVisibilityKeyframes(selectedItems[1], 2, 1)
        om.MGlobal.displayInfo("Successful")
    elif(firstItemVisibilityKeyable):
        om.MGlobal.displayError("The second selected item doesnt have keyable visibility")
    elif(secondItemVisibilityKeyable):
        om.MGlobal.displayError("The first selected item doesnt have keyable visibility")
    else:
        om.MGlobal.displayError("Neither selected items have keyable visibility")
        
elif(selectedItemsLength < 2):
    om.MGlobal.displayError("Not enough items selected, need 2 items with keyable visibility selected")
else:
    om.MGlobal.displayError("Too many items selected, need 2 items with keyable visibility selected")