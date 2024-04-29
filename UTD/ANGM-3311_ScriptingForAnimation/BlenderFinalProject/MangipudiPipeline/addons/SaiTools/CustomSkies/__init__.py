import bpy
from bpy.types import Panel

class SaiToolsPanel(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "SaiTools"
    bl_idname = "DEV_PT_saitools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Sai's Tools"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("saitools.customskiesgui")
