import maya.cmds
import datetime
import pymel.core as pm
import os


def set_render_settings():
    if not cmds.getAttr("defaultArnoldDriver.halfPrecision"):
        cmds.setAttr("defaultArnoldDriver.halfPrecision", 1)

    if not cmds.getAttr("defaultArnoldDriver.mergeAOVs"):
        cmds.setAttr("defaultArnoldDriver.mergeAOVs", 1)
    
    """
    if not cmds.getAttr("defaultArnoldRenderOptions.renderType"):
        cmds.setAttr("defaultArnoldRenderOptions.renderType", 1)
    """

def render():
    current_time = datetime.datetime.now()
    date = "{year}{month}{date}".format(year=current_time.year, month=current_time.month, date=current_time.day)

    render_dir= r'C:\Users\benja\Desktop\TMP\\'
    #cmds.workspace(fileRule=['translatorData', render_dir])

    for frame in range(1, 10 + 1):
        frame_padded = str(frame).zfill(4)
        
        cmds.currentTime(frame)
        frame_path = "{folder}<Scene>_<RenderLayer>_{date}_{frame}".format(folder=render_dir, date=date, frame=frame_padded)
        pm.other.arnoldExportAss(filename=frame_path)

render()
    
    
    