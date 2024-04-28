# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Sai's Custom Tools",
    "author" : "Sai Mangipudi",
    "description" : "Take control of blender with the help of Sai's custom tools",
    "blender" : (4, 0, 2),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Development"
}

import bpy
from . import CustomSkies
from . import CustomSkiesGUI
from importlib import reload

tools = [
    CustomSkies.CustomSkiesOperator,
    CustomSkiesGUI.CustomSkiesGUIOperator
]

def register():
    reload(CustomSkies)
    reload(CustomSkiesGUI)
    
    for cls in tools:
        bpy.utils.register_class(cls)
        print(f"Registered {cls}")

def unregister():
    for cls in tools:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()