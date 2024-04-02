import maya.cmds as cmds
import random

class Settings_Window(object):
    
    #constructor
    def __init__(self):
        self.window = 'settingsWindow'
        self.title = 'Settings Window'
        self.size = (800, 600)
        self.already_seen = set()
        self.generatedBuldingList = [] 
        
        #close old window if still open
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
            
        #create new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size, s=True)
        cmds.columnLayout(adjustableColumn=True)
        
        #create UI elements
        cmds.text(self.title)
        cmds.separator( height=20, style='out' )
        
        self.cityGridSize = cmds.floatFieldGrp(numberOfFields=2, label='City Grid Size', value1=10, value2=10)
        self.buildingNumber = cmds.intSliderGrp(label='Building Number', field=True, minValue=1, maxValue=1000, value=10)
        self.buildingHeight = cmds.floatFieldGrp(numberOfFields=2, label='Building Height', value1=1, value2=10)
        self.buildingRotationLimits = cmds.floatFieldGrp(numberOfFields=2, label='Building Rotation Limits', value1=0, value2=360)
        self.distanceBetweenBuildings = cmds.floatFieldGrp(label='Distance Between Buildings', value1=5)
        self.customSeed = cmds.intFieldGrp(label='Custom Seed', value1=0)
        self.customObjectGroupName = cmds.textFieldGrp(label='Custom Building Models Group Name', text='CustomObjectGroup')
    
        
        cmds.separator( height=20, style='none')
        #generate button
        # cmds.button(label='Generate', command=self.generate)
        cmds.button(label='Generate', command=self.generate_city)
        cmds.separator( height=20, style='none')
        cmds.button(label='Reset', command=self.delete_city)
        
        cmds.separator( height=20, style='out')
        cmds.text(label='Debug Log')
        cmds.separator( height=10, style='none')
        self.debugLog = cmds.scrollField(editable=False, wordWrap=True, width=800, height=120)
        
        #display window
        cmds.showWindow(self.window)
    
    
    def generate_city(self, *args):
        print('Generating City')
        cmds.scrollField(self.debugLog, edit=True, insertText='Generating City\n')
        cmds.refresh(f=True)
    
        
        cityGridSize = cmds.floatFieldGrp(self.cityGridSize, query=True, value=True)
        buildingNumber = cmds.intSliderGrp(self.buildingNumber, query=True, value=True)
        buildingHeight = cmds.floatFieldGrp(self.buildingHeight, query=True, value=True)
        buildingRotationLimits = cmds.floatFieldGrp(self.buildingRotationLimits, query=True, value=True)
        distBetweenBuildings = cmds.floatFieldGrp(self.distanceBetweenBuildings, query=True, value1=True)
        customSeed = cmds.intFieldGrp(self.customSeed, query=True, value1=True)
        customObjectGroupName = cmds.textFieldGrp(self.customObjectGroupName, query=True, text=True)

        # check if building group exists
        if not cmds.objExists("BuildingGroup"):
            cmds.group(em=True, name="BuildingGroup")
            cmds.polyCube(name="BuildingTemplate", width=1, height=1, depth=1)
            cmds.parent("BuildingTemplate", "BuildingGroup")
        
        # if the user entered a valid customObjectGroupName, use that group
        if cmds.objExists(customObjectGroupName):
            buildingGroup = customObjectGroupName
            cmds.delete("BuildingGroup")
        else:
            buildingGroup = "BuildingGroup"

        # make a city group
        cmds.group(em=True, name="CityGroup")

        for i in range(buildingNumber):
            if (customSeed != 0):
                random.seed(customSeed)
            
            # make a building
            xPos = random.uniform(-cityGridSize[0]/2, cityGridSize[0]/2)
            #make xpos a multiple of 5
            xPos = round(xPos / distBetweenBuildings) * distBetweenBuildings
                
            yPos = random.uniform(-cityGridSize[1]/2, cityGridSize[1]/2)
            #make ypos a multiple of 5
            yPos = round(yPos / distBetweenBuildings) * distBetweenBuildings

            pos = (xPos, yPos)
                
            
            # pick a random building from the building group
            possibleBuildings = cmds.listRelatives(buildingGroup, children=True)
            possibleBuilding = random.choice(possibleBuildings)
            
            if pos not in self.already_seen:
                self.already_seen.add(pos)
                cmds.instance(possibleBuilding, name="Building" + str(i))
            
                # position, scale, and rotate the building
                cmds.move(pos[0] + random.randrange(0, (distBetweenBuildings - 1)), 0, pos[1] + random.randrange(0, (distBetweenBuildings - 1)), "Building" + str(i))
                cmds.scale(1, random.uniform(buildingHeight[0], buildingHeight[1]), 1, "Building" + str(i))
                cmds.rotate(0, random.uniform(buildingRotationLimits[0], buildingRotationLimits[1]), 0, "Building" + str(i))
                cmds.parent("Building" + str(i), "CityGroup")
                self.generatedBuldingList.append("Building" + str(i))
                print("Building" + str(i) + " created")
                cmds.scrollField(self.debugLog, edit=True, insertText="Building" + str(i) + " created\n")
            
            cmds.refresh(f=True)
                
        
        
        #make a plane the size of city grid size and add it to the city group
        cmds.polyPlane(name="CityPlane", width=cityGridSize[0], height=cityGridSize[1], sx=1, sy=1)
        cmds.parent("CityPlane", "CityGroup")
        
        
    def delete_city(self, *args):
            print('Deleting City')
            cmds.scrollField(self.debugLog, edit=True, insertText='Deleting City\n')
            cmds.refresh(f=True)
            
        
            cmds.delete("CityGroup")
            cmds.delete("BuildingGroup")
            
            #clear the list
            self.generatedBuldingList.clear()
            self.already_seen.clear()
            cmds.scrollField(self.debugLog, edit=True, insertText='City Deleted\n')
            cmds.refresh(f=True)
            
            

        
if __name__ == '__main__':
    Settings_Window()