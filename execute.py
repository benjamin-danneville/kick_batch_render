import sys
sys.path.append("C:\\Program Files\\Autodesk\\Maya2020\\Python\\Lib\\site-packages")

import maya.standalone
maya.standalone.initialize("Python")

import ass_exporter
import command_builder

folder_path= r'C:\\Users\\benja\\Desktop\TMP\\'

ass_exporter.open_scene()
ass_exporter.set_render_settings()
ass_exporter.export(folder_path)

command_builder.render(folder_path)
