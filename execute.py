import sys
sys.path.append("C:\\Program Files\\Autodesk\\Maya2020\\Python\\Lib\\site-packages")

import maya.standalone
maya.standalone.initialize("Python")

import ass_exporter
import command_builder


output_folder_path= r'C:\\Users\\benja\\Desktop\TMP\\'
#, "C:/Users/benja/Desktop/CYLINDRE.ma"
maya_filepaths = ["C:/Users/benja/Desktop/test.ma"]

for maya_filepath in maya_filepaths:
    ass_exporter.open_scene(maya_filepath)
    ass_exporter.set_render_settings()
    for layer in cmds.ls(type='renderLayer'):
        if cmds.getAttr("{0}.renderable".format(layer)):
            cmds.editRenderLayerGlobals(currentRenderLayer=layer)
            #print(cmds.getAttr(layer + ".renderable"))
            ass_exporter.export(output_folder_path)
            command_builder.render(output_folder_path)
            ass_exporter.clean_ass_files(output_folder_path)
