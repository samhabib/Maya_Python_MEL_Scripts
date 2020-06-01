import maya.cmds as cmds

#file -f -new; -> Open new file forcefully
cmds.file(f=True, new=True)

#polyCube -w 1 -h 2 -d 3 -sx 1 -sy 2 -sz 3 -ax 0 1 0 -cuv 4 -ch 1;
cmds.polyCube(w=1,h=2,d=3,sx=1,sy=2,sz=3,ax=(0,1,0),cuv=4,ch=1)

#select -r pCube1; difference between MEL and Python is that in MEL objects go last, in python objects go first
cmds.select("pCube1", replace=True)
#select -tgl pCube1; will select if unselected or deselect if selected
cmds.select("pCube1",toggle=True)
#select -add pCube1; will add item if unselected
cmds.select("pCube1",add=True)
