import maya.standalone
maya.standalone.initialize("Python")

import ass_exporter
import command_builder

import maya.cmds as cmds


def render(output_folder_path, maya_filepaths):
    output_folder_path = output_folder_path.replace("/", "\\\\")

    for maya_filepath in maya_filepaths:
        ass_exporter.open_scene(maya_filepath)
        ass_exporter.set_render_settings()
        for layer in cmds.ls(type='renderLayer'):
            if cmds.getAttr("{0}.renderable".format(layer)):
                cmds.editRenderLayerGlobals(currentRenderLayer=layer)
                ass_exporter.export(output_folder_path)
                command_builder.render(output_folder_path)
                ass_exporter.clean_ass_files(output_folder_path)