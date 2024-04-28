import bpy
from bpy.types import Operator

class CustomSkiesOperator(bpy.types.Operator):
    bl_idname = "saitools.customskies"
    bl_label = "Sai Tools - Custom Skies"
    

    def execute(self, context):
        print("Custom Skies Operator")
        return {'RUNNING_MODAL'}