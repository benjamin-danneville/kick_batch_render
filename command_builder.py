import os
from pathlib import Path

KICK_PATH = Path("C:/Program Files/Autodesk/Arnold/maya2020/bin/kick.exe")

file_format = ".exr"

ass_folders = []
ass_folders.append(Path("D:/Documents/Perso/Projets/Kick_Batch_Render/Render/ass_files/ass_files_v001/"))

for ass_folder in ass_folders:
    for ass_file in ass_folder.iterdir():
        output_file = "{0}{1}".format(ass_file.with_suffix("".format(file_format)), file_format)
        os.system('"{0}" -dp -dw -v 6 -i {1} -o {2}'.format(KICK_PATH, ass_file, output_file))