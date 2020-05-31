import sys # Gives access to BE computer, interface of computer, system files
import os # Gives access to Operating System
import maya.cmds as mc # Gives access to Maya commands, and we aliased it as mc for shorthand

sys.stdout.write('Hello World')  # std -> standard      out -> output

mc.textCurves(t = "Hello World") # Generates Nurb Curves that spell out "Maya" by default, can change font with f="font_name" and text with t="Custom Text Here"
mc.planarSrf(n = "Hello3DWorld_GEO") # Since our previous call creates a nurbs and doesnt unselect it, we can call planarSrf which generates a planar surface on the selected object (The nurbs) and then makes a planar object from it, also the n='Insert name' flag allows us to make a custom name for our object
    