__author__ = "Benjamin Danneville"
__copyright__ = "Copyright 2022, Benjamin Danneville"
__version__ = "0.1.3"
__maintainer__ = "Benjamin Danneville"
__email__ = "benjamin.danneville@gmail.com"
__status__ = "Maintenance"


import subprocess


if __name__ == "__main__":
    cmd = "C:/Program Files/Autodesk/Maya2020/bin/mayapy.exe"
    try:
        subprocess.call([cmd, "ui.py"])
    except Exception as exception:
        print(exception)