import bpy
import sys
from PySide2 import QtWidgets
from bpy.types import Operator

from . import CustomSkiesGUI

class CustomSkiesGUIOperator(bpy.types.Operator):
    bl_idname = "saitools.customskiesgui"
    bl_label = "Custom Skies"
    

    def execute(self, context):
        app = QtWidgets.QApplication.instance()
        
        if app is None:
            app = QtWidgets.QApplication(sys.argv)
            
        self.widget = CustomSkiesGUI.SkiesGUI()
        return {'RUNNING_MODAL'}
    