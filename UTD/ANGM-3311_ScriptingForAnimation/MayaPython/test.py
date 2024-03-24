import maya.cmds as cmds

class Settings_Window(object):
    
    #constructor
    def __init__(self):
        self.window = 'settingsWindow'
        self.title = 'Settings Window'
        self.size = (800, 600)
        
        #close old window if still open
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
            
        #create new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size, s=True)
        cmds.columnLayout(adjustableColumn=True)
        
        #create UI elements
        cmds.text(self.title)
        cmds.separator(h=20, style='none')
        
        self.cityGridSize = cmds.floatFieldGrp(numberOfFields=2, label='City Grid Size', value1=10, value2=10)
        self.buildingHeight = cmds.floatFieldGrp(numberOfFields=2, label='Building Height', value1=1, value2=10)
        self.customSeed = cmds.intFieldGrp(label='Custom Seed', value1=0)
        self.customObjectGroupName = cmds.textFieldGrp(label='Custom Object Group', text='CustomObjectGroup')
        self.neglectObjectGroupName = cmds.textFieldGrp(label='Neglect Object Group', text='NeglectObjectGroup')
        
        #display window
        cmds.showWindow(self.window)
        
        
if __name__ == '__main__':
    Settings_Window()