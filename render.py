import os

import maya.standalone
maya.standalone.initialize("Python")

import ass_exporter
import command_builder

import maya.cmds as cmds


def render(output_folder_basepath, maya_filepaths, le_step):
    for maya_filepath in maya_filepaths:
        maya_filepath_name = (os.path.splitext(maya_filepath))[0]
        maya_filename = os.path.basename(maya_filepath_name)
        output_folder_path = os.path.join(output_folder_basepath, maya_filename)
        output_folder_path = output_folder_path.replace("/", "\\\\")
        ass_exporter.open_scene(maya_filepath)
        ass_exporter.set_render_settings(le_step)
        for layer in cmds.ls(type='renderLayer'):
            if not ":" in layer:
                if cmds.getAttr("{0}.renderable".format(layer)):
                    cmds.editRenderLayerGlobals(currentRenderLayer=layer)
                    ass_exporter.export(output_folder_path)
                    command_builder.render(output_folder_path)
                    ass_exporter.clean_ass_files(output_folder_path)

        print("{0} has been rendered".format(maya_filepath))
    
    print("All maya files has been rendered")