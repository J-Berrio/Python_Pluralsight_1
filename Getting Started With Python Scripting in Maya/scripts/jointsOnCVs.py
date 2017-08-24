#Identify function to use for Maya commands - mc
import maya.cmds as mc

#Find selected components
selCVs = mc.ls(sl=True, fl=True)

#Get the size of selection
selSize_CV = len(selCVs)

#For Loop - for all CVs in selection, run the following cmds
for cvs in range(0, selSize_CV, 1):
    #Find the position of each CV
    findCV_X = mc.getAttr(selCVs[cvs] + ".xValue")
    findCV_Y = mc.getAttr(selCVs[cvs] + ".yValue")
    findCV_Z = mc.getAttr(selCVs[cvs] + ".zValue")
    #Clear selection 
    mc.select(cl=True)#<- this prevents joints from being parented to curve
    #Create a joint for each selected CV.
    mkJnt = mc.joint()#If you're creating an object that's not a joint, query the object's Return Value from the Docs
    #Align a joint to each CV in selection
    #NOTE - If you're making an object whose command creates more that one node, make sure to access the object's transform node with [0]
    #NOTE - In this code, if you swap mc.joint() with mc.polyCube(), we would need [0] after the variable "mkJnt" in order to access the transform node of the object
    mc.setAttr(mkJnt + ".tx", findCV_X)
    mc.setAttr(mkJnt + ".ty", findCV_Y)
    mc.setAttr(mkJnt + ".tz", findCV_Z)