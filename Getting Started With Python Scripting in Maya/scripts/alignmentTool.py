#Define function used to run maya commands with Python - mc
import maya.cmds as mc

##OAT - Object Alignment Tool
#Instructions: first select source, then target

#This declares variable objAligner
string = objAligner

#This prevents the duplication of our window
if mc.window(objAligner, ex=True):
    mc.deleteUI(objAligner, window=True)

#Create a window for the object aligner that is not resizeable
objAligner = mc.window(title="Object Alignment Tool", s=False, wh=(300, 100))
#Create an adjustable column layout
mc.columnLayout(adj=True)
#Instructions
mc.text(l="Instructions: select source, then target")
#Add a button to our window
mc.button(l="Go Aligner Go!", w=300, h=100, c="aligner()")
#Show the window
mc.showWindow(objAligner)

#This creates a function (named "aligner()") that runs a series of code
def aligner():
    #This creates a parent constraint with no offset
    prtCns = mc.parentConstraint()
    #This removes the parent constraint
    mc.delete(prtCns)