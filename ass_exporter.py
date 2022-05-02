import os
import datetime

import maya.cmds as cmds
import pymel.core as pm


def open_scene(maya_filepath):
    if maya_filepath:
        cmds.file(new=True, force=True) 
        cmds.file(maya_filepath, open=True)

def set_render_settings():
    if not cmds.getAttr("defaultArnoldDriver.halfPrecision"):
        cmds.setAttr("defaultArnoldDriver.halfPrecision", 1)

    if not cmds.getAttr("defaultArnoldDriver.mergeAOVs"):
        cmds.setAttr("defaultArnoldDriver.mergeAOVs", 1)
    
    """
    if not cmds.getAttr("defaultArnoldRenderOptions.renderType"):
        cmds.setAttr("defaultArnoldRenderOptions.renderType", 1)
    """

def export(folder_path):
    current_time = datetime.datetime.now()
    date = "{year}{month}{date}".format(year=current_time.year, month=current_time.month, date=current_time.day)

    #cmds.workspace(fileRule=['translatorData', folder_path])
    
    for frame in range(1, 10 + 1):
        frame_padded = str(frame).zfill(4)
        
        cmds.currentTime(frame)
        frame_path = "{folder}\\\\<Scene>_<RenderLayer>_{date}_{frame}".format(folder=folder_path, date=date, frame=frame_padded)
        print(frame_path)
        pm.other.arnoldExportAss(filename=frame_path)

def clean_ass_files(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        if not os.path.isdir(file) and ".ass" in file:
            os.remove(os.path.abspath(os.path.join(folder_path, file)))