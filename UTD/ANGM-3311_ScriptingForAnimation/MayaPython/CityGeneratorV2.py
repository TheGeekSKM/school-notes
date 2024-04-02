import random

import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import maya.cmds as cmds


def get_maya_main_win():
    """Return the Maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window), QtWidgets.QWidget)


class CityGeneratorWin(QtWidgets.QDialog):
    """Say Hello Window class"""

    def __init__(self):
        """Initialise the object"""
        super(CityGeneratorWin, self).__init__(parent=get_maya_main_win())
        self._set_win()
        self._define_widgets()
        self._layout_ui()
        self._connect_signals()

    def _set_win(self):
        """Set window settings"""
        self.setWindowTitle("City Generator")
        self.resize(500, 200)
        self.already_seen = set()
        self.generatedBuldingList = []
    
    def _define_city_size_widgets(self):
        """Define the city size widgets"""
        self.city_size_lbl = QtWidgets.QLabel("City Size:")
        self.city_size_x = QtWidgets.QSpinBox()
        self.city_size_x.setValue(10)
        self.city_size_x.setRange(1, 500)
        self.city_size_y = QtWidgets.QSpinBox()
        self.city_size_y.setValue(10)
        self.city_size_y.setRange(1, 500)
    
    
    def _define_building_number_widgets(self):
        self.building_number_lbl = QtWidgets.QLabel("Building Number:")
        self.building_number = QtWidgets.QSpinBox()
        self.building_number.setValue(10)
        self.building_number.setRange(1, 1000)
        
    
    def _define_building_size_widgets(self):
        self.building_height_lbl = QtWidgets.QLabel("Building Height:")
        self.building_height_min = QtWidgets.QSpinBox()
        self.building_height_min.setRange(1, 100)
        self.building_height_min.setValue(1)
        self.building_height_max = QtWidgets.QSpinBox()
        self.building_height_max.setRange(1, 100)
        self.building_height_max.setValue(5)
        
    
    def _define_building_rotation_widgets(self):
        self.building_rotation_lbl = QtWidgets.QLabel("Building Rotation Limits:")
        self.building_rotation_min = QtWidgets.QSpinBox()
        self.building_rotation_min.setRange(0, 360)
        self.building_rotation_min.setValue(0)
        self.building_rotation_max = QtWidgets.QSpinBox()
        self.building_rotation_max.setRange(0, 360)
        self.building_rotation_max.setValue(360)
        
    
    def _define_distance_between_buildings_widgets(self):
        self.distance_between_buildings_lbl = QtWidgets.QLabel("Distance Between Buildings:")
        self.distance_between_buildings = QtWidgets.QSpinBox()
        self.distance_between_buildings.setValue(5)
        
    
    def _define_custom_seed_widgets(self):
        self.custom_seed_lbl = QtWidgets.QLabel("Custom Seed:")
        self.custom_seed = QtWidgets.QSpinBox()
        self.custom_seed.setValue(0)
        
    
    def _define_custom_object_group_widgets(self):
        self.custom_object_group_lbl = QtWidgets.QLabel("Custom Building Models Group Name:")
        self.custom_object_group = QtWidgets.QLineEdit("CustomObjectGroup")
        
    
    def _define_custom_material_name_widgets(self):
        self.custom_material_name_lbl = QtWidgets.QLabel("Custom Material Name:")
        self.custom_building_material_name = QtWidgets.QLineEdit("CustomBuildingMaterial")
        self.custom_building_material_name.setPlaceholderText("Enter the material name") 
        self.custom_ground_material_name = QtWidgets.QLineEdit("CustomGroundMaterial")
        self.custom_ground_material_name.setPlaceholderText("Enter the material name")
        
    def _define_generate_reset_buttons(self):
        self.generate_btn = QtWidgets.QPushButton("Generate")
        self.reset_btn = QtWidgets.QPushButton("Reset")
    
    def _define_debug_log(self):
        self.debug_log = QtWidgets.QTextEdit()
        self.debug_log.setReadOnly(True)

    def _define_widgets(self):
        """Define the UI elements/widgets"""
        self._define_city_size_widgets()
        self._define_building_number_widgets()
        self._define_building_size_widgets()
        self._define_building_rotation_widgets()
        self._define_distance_between_buildings_widgets()
        self._define_custom_seed_widgets()
        self._define_custom_object_group_widgets()
        self._define_custom_material_name_widgets()
        self._define_generate_reset_buttons()
        self._define_debug_log()
        
    def _layout_city_size_widgets(self):
        self.city_size_layout = QtWidgets.QHBoxLayout()
        self.city_size_layout.addWidget(self.city_size_lbl)
        self.city_size_layout.addWidget(self.city_size_x)
        self.city_size_layout.addWidget(self.city_size_y)
    
    def _layout_building_number_widgets(self):
        self.building_number_layout = QtWidgets.QHBoxLayout()
        self.building_number_layout.addWidget(self.building_number_lbl)
        self.building_number_layout.addWidget(self.building_number)
        
    def _layout_building_size_widgets(self):
        self.building_height_layout = QtWidgets.QHBoxLayout()
        self.building_height_layout.addWidget(self.building_height_lbl)
        self.building_height_layout.addWidget(self.building_height_min)
        self.building_height_layout.addWidget(self.building_height_max)
        
    def _layout_building_rotation_widgets(self):
        self.building_rotation_layout = QtWidgets.QHBoxLayout()
        self.building_rotation_layout.addWidget(self.building_rotation_lbl)
        self.building_rotation_layout.addWidget(self.building_rotation_min)
        self.building_rotation_layout.addWidget(self.building_rotation_max)
    
    def _layout_distance_between_buildings_widgets(self):
        self.distance_between_buildings_layout = QtWidgets.QHBoxLayout()
        self.distance_between_buildings_layout.addWidget(self.distance_between_buildings_lbl)
        self.distance_between_buildings_layout.addWidget(self.distance_between_buildings)
        
    def _layout_custom_seed_widgets(self):
        self.custom_seed_layout = QtWidgets.QHBoxLayout()
        self.custom_seed_layout.addWidget(self.custom_seed_lbl)
        self.custom_seed_layout.addWidget(self.custom_seed)
        
    def _layout_custom_object_group_widgets(self):
        self.custom_object_group_layout = QtWidgets.QHBoxLayout()
        self.custom_object_group_layout.addWidget(self.custom_object_group_lbl)
        self.custom_object_group_layout.addWidget(self.custom_object_group)
        
    def _layout_custom_material_name_widgets(self):
        self.custom_material_name_layout = QtWidgets.QVBoxLayout()
        self.custom_material_name_layout.addWidget(self.custom_material_name_lbl)
        self.custom_material_name_layout.addWidget(self.custom_building_material_name)
        self.custom_material_name_layout.addWidget(self.custom_ground_material_name)
        
    def _layout_generate_reset_buttons(self):
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.addWidget(self.generate_btn)
        self.button_layout.addWidget(self.reset_btn)
        
    def _layout_debug_log(self):
        self.debug_log_layout = QtWidgets.QVBoxLayout()
        self.debug_log_layout.addWidget(self.debug_log)
        
    def _layout_main_widget(self):
        self.main_layout.addLayout(self.city_size_layout)
        self.main_layout.addLayout(self.building_number_layout)
        self.main_layout.addLayout(self.building_height_layout)
        self.main_layout.addLayout(self.building_rotation_layout)
        self.main_layout.addLayout(self.distance_between_buildings_layout)
        self.main_layout.addLayout(self.custom_seed_layout)
        self.main_layout.addLayout(self.custom_object_group_layout)
        self.main_layout.addLayout(self.custom_material_name_layout)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.debug_log_layout)
        self.setLayout(self.main_layout)

    def _layout_ui(self):
        """Layout the UI elements/widgets"""
        self.main_layout = QtWidgets.QVBoxLayout()
        
        self._layout_city_size_widgets()
        self._layout_building_number_widgets()
        self._layout_building_size_widgets()
        self._layout_building_rotation_widgets()
        self._layout_distance_between_buildings_widgets()
        self._layout_custom_seed_widgets()
        self._layout_custom_object_group_widgets()
        self._layout_custom_material_name_widgets()
        self._layout_generate_reset_buttons()
        self._layout_debug_log()
        self._layout_main_widget()

    def _connect_signals(self):
        """Connect signals and slots"""
        self.generate_btn.clicked.connect(self.generate_city)
        self.reset_btn.clicked.connect(self.delete_city)
      
    def log(self, message):
        """Log message to the debug log"""
        self.debug_log.append(message)
        self.main_layout.update()
        cmds.refresh(f=True)

    def clearLog(self):
        """Clear the debug log"""
        self.debug_log.clear()
        self.main_layout.update()

    def get_values_from_ui(self):
        """Get the values from the UI"""
        self.cityGridSize = [self.city_size_x.value(), self.city_size_y.value()]
        self.buildingNumber = self.building_number.value()
        self.buildingHeight = [self.building_height_min.value(), self.building_height_max.value()]
        self.buildingRotationLimits = [self.building_rotation_min.value(), self.building_rotation_max.value()]
        self.distBetweenBuildings = self.distance_between_buildings.value()
        self.customSeed = self.custom_seed.value()
        self.customObjectGroupName = self.custom_object_group.text()

    def get_building_group(self):
        """Get the building group"""
        if not cmds.objExists("BuildingGroup"):
            cmds.group(em=True, name="BuildingGroup")
            cmds.polyCube(name="BuildingTemplate", width=1, height=1, depth=1)
            cmds.parent("BuildingTemplate", "BuildingGroup")
        
        if cmds.objExists(self.customObjectGroupName):
            self.buildingGroup = self.customObjectGroupName
            cmds.delete("BuildingGroup")
        else:
            self.buildingGroup = "BuildingGroup"

    def make_plane(self):
        """Make a plane the size of city grid size and add it to the city group
        """
        cmds.polyPlane(name="CityPlane", width=self.cityGridSize[0], height=self.cityGridSize[1], sx=1, sy=1)
        cmds.parent("CityPlane", "CityGroup")
        
        if cmds.objExists(self.custom_ground_material_name.text()):
            cmds.select("CityPlane")
            cmds.hyperShade(assign=self.custom_ground_material_name.text())

    def set_random_seed(self):
        """Set the random seed
        """
        if (self.customSeed != 0):
            random.seed(self.customSeed)

    def get_pos(self):
        """Get the position of the building

        Returns:
            tuple: The position of the building
        """
        xPos = random.uniform(-self.cityGridSize[0]/2, self.cityGridSize[0]/2)
        xPos = round(xPos / self.distBetweenBuildings) * self.distBetweenBuildings
            
        yPos = random.uniform(-self.cityGridSize[1]/2, self.cityGridSize[1]/2)
        yPos = round(yPos / self.distBetweenBuildings) * self.distBetweenBuildings
        
        return (xPos, yPos)

    def get_building(self):
        """Get a random building from the building group

        Returns:
            building: The building
        """
        possibleBuildings = cmds.listRelatives(self.buildingGroup, children=True)
        return random.choice(possibleBuildings)

    def create_building_instance(self, building, i, pos):
        """ Create a building instance

        Args:
            building: The building
            i (int): The index of the building
            pos (tuple): The position of the building
        """
        if pos not in self.already_seen:
            self.already_seen.add(pos)
            cmds.instance(building, name="Building" + str(i))
            
            self.assign_building_material(i)
            self.move_building(i, pos)
    
    def assign_building_material(self, buildingIndex):
        """Assign the building material

        Args:
            buildingIndex (int): The index of the building
        """
        if cmds.objExists(self.custom_building_material_name.text()):
            cmds.select("Building" + str(buildingIndex))
            cmds.hyperShade(assign=self.custom_building_material_name.text())

    def move_building(self, buildingIndex, pos):
        """Move the building

        Args:
            buildingIndex (object reference): The index of the building
            pos (tuple): The position of the building
        """
        cmds.move(pos[0] + random.randrange(0, (self.distBetweenBuildings - 1)), 0, pos[1] + random.randrange(0, (self.distBetweenBuildings - 1)), "Building" + str(buildingIndex))
        randomScale = random.uniform(self.buildingHeight[0], self.buildingHeight[1])
        cmds.scale(1, randomScale, 1, "Building" + str(buildingIndex))
        cmds.move(0, randomScale/2, 0, "Building" + str(buildingIndex), r=True)
        cmds.rotate(0, random.uniform(self.buildingRotationLimits[0], self.buildingRotationLimits[1]), 0, "Building" + str(buildingIndex))
        cmds.parent("Building" + str(buildingIndex), "CityGroup")
        self.log(f"Building {buildingIndex} created at {pos}")
        self.generatedBuldingList.append("Building" + str(buildingIndex))

    @QtCore.Slot()
    def generate_city(self):
        self.log("Generating City")
        
        self.get_values_from_ui()
        
        self.get_building_group()
        
        # make a city group
        cmds.group(em=True, name="CityGroup")
        
        for i in range(self.buildingNumber):
            self.set_random_seed()
            pos = self.get_pos()
            building = self.get_building()
            self.create_building_instance(building, i, pos)
     
        self.make_plane()

    @QtCore.Slot()
    def delete_city(self):
        self.log("Deleting City")
        cmds.delete(self.generatedBuldingList)
        cmds.delete("CityGroup")
        cmds.delete("BuildingGroup")
        self.already_seen.clear()
        self.generatedBuldingList.clear()

        self.log("City deleted")

if __name__ == "__main__":
    win = CityGeneratorWin()
    win.show()