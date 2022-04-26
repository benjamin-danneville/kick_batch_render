import os

KICK_PATH = "C:/Program Files/Autodesk/Arnold/maya2020/bin/kick.exe"

def render(folder_path):
    file_format = ".exr"

    ass_folders = []
    ass_folders.append(folder_path.replace("\\\\", "/"))

    for ass_folder in ass_folders:
        for ass_file in os.listdir(ass_folder):
            pre, ext = os.path.splitext(ass_file)
            output_file = "{0}{1}".format(pre, file_format)
            os.system('"{0}" -dp -dw -v 6 -i {1} -o {2}'.format(KICK_PATH, ass_file, output_file))