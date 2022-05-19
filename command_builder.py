import os


KICK_PATH = "C:/Program Files/Autodesk/Arnold/maya2020/bin/kick.exe"

def render(folder_path):
    file_format = ".exr"

    ass_folders = []
    ass_folders.append(folder_path.replace("\\\\", "/"))

    for ass_folder in ass_folders:
        for file in os.listdir(ass_folder):
            if ".ass" in file:
                pre = (os.path.splitext(file))[0]
                output_file = "{0}{1}".format(pre, file_format)
                os.system('"{0}" -dp -dw -v 1 -i {1} -o {2}'.format(KICK_PATH, folder_path + "/" + file, folder_path + "/" + output_file))