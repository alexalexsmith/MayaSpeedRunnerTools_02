#Simple motion trail rig python script
import maya.cmds as cmds

selectedCurve = cmds.ls (sl=True)
motionPathCurve = cmds.rename(selectedCurve[0], 'motionPath_Curve_')
cmds.delete(motionPathCurve, constructionHistory = True)
myLocator = cmds.spaceLocator (name='MotionPath_Loc_')
AxisArray = ['Z', 'X', 'Y']
for axis in AxisArray:
    cmds.setAttr ((myLocator[0] + 'Shape.localScale' + axis), 200)
    cmds.setAttr ((myLocator[0] + '.translate' + axis), keyable=False)
    cmds.setAttr ((myLocator[0] + '.rotate' + axis), keyable=False)
    cmds.setAttr ((myLocator[0] + '.scale' + axis), keyable=False)

cmds.select(myLocator[0], motionPathCurve)
motionPathNode = cmds.pathAnimation(fractionMode=False, follow=True, followAxis='x', upAxis='y', worldUpType="vector")
cmds.cutKey(motionPathNode)

AttributeArray = cmds.listAttr( motionPathNode, s=True, keyable=True)
for newConnection in AttributeArray:
    cmds.addAttr(keyable=True, attributeType='float', longName = newConnection, defaultValue=0.0)
    cmds.connectAttr((myLocator[0] + '.' + newConnection), (motionPathNode + '.' + newConnection))
