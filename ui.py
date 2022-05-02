__author__ = "Benjamin Danneville"
__copyright__ = "Copyright 2022, One of Us"
__version__ = "0.1.3"
__maintainer__ = "Benjamin Danneville"
__email__ = "benjamin-d@weacceptyou.com"
__status__ = "Maintenance"
 
 
import sys
 
from PyQt5 import QtCore
from PyQt5 import QtWidgets

import execute
 
 
class BDRenderer(QtWidgets.QDialog):
    def __init__(self):
        super(BDRenderer, self).__init__()
        
        # Variable
        self.maya_files = []
        self.selected_maya_files = None

        # Window title and minimum width
        self.setWindowTitle("BD Renderer")
        self.setMinimumHeight(280)
        self.setMinimumWidth(400)
    
        # Remove Question Mark
        #self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
    
        # UI
        self.create_widget()
        self.create_layout()
        self.widget_connection()
  
    def create_widget(self):
        self.pb_render = QtWidgets.QPushButton("RENDER FILES")

        self.pb_add = QtWidgets.QPushButton("ADD")
        self.pb_remove = QtWidgets.QPushButton("REMOVE")

        self.le_output = QtWidgets.QLineEdit()
        #self.le_output.setReadOnly(True)
        self.le_output.setPlaceholderText("output folder path")
        self.pb_output = QtWidgets.QPushButton("OUTPUT")

    def create_layout(self):
        self.vbl_main = QtWidgets.QVBoxLayout(self)

        self.tw_maya_files = QtWidgets.QTableWidget()
        self.tw_maya_files.setColumnCount(1)

        self.tw_maya_files.verticalHeader().setVisible(False)
        self.tw_maya_files.horizontalHeader().setVisible(False)

        self.tw_maya_files.horizontalHeader().setStretchLastSection(True)

        self.tw_maya_files.setRowCount(10)
        for i in range(10):
            name = "PATH {0}".format(i)
            self.maya_files.append(name)
            item = QtWidgets.QTableWidgetItem(name)
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
            self.tw_maya_files.setItem(i, 0, item)

        self.hbl_lw_button = QtWidgets.QHBoxLayout()
        self.hbl_lw_button.addWidget(self.pb_add)
        self.hbl_lw_button.addWidget(self.pb_remove)

        self.hbl_output_button = QtWidgets.QHBoxLayout()
        self.hbl_output_button.addWidget(self.le_output)
        self.hbl_output_button.addWidget(self.pb_output)

        self.vbl_main.addWidget(self.tw_maya_files)
        self.vbl_main.addLayout(self.hbl_lw_button)
        self.vbl_main.addLayout(self.hbl_output_button)
        self.vbl_main.addWidget(self.pb_render)

    def output_clicked(self):
        folder_filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "Select the output renders folder")
        self.le_output.setText(folder_filepath)

    def remove_clicked(self):
        for selected_maya_file in self.selected_maya_files:
            if selected_maya_file.text() in self.maya_files:
                self.maya_files.remove(selected_maya_file.text())
            """
            self.tw_maya_files.takeItem(selected_maya_file.row(), 0)
            self.tw_maya_files.removeRow(selected_maya_file.row())
            """
        
        self.update_maya_files()

    def add_clicked(self):
        maya_filepaths, check = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open a maya file', '', 'Maya Ascii Files (*.ma);;All files (*.*)')
        if check:
            for maya_filepath in maya_filepaths:
                if not maya_filepath in self.maya_files:
                    self.maya_files.append(maya_filepath)
        
        self.update_maya_files()

    def maya_file_selected(self):
        self.selected_maya_files = self.tw_maya_files.selectedItems()

    def update_maya_files(self):
        self.tw_maya_files.clear()
        self.tw_maya_files.setRowCount(len(self.maya_files))

        for i in range(len(self.maya_files)):
            item = QtWidgets.QTableWidgetItem(self.maya_files[i])
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
            self.tw_maya_files.setItem(i, 0, item)

    def render(self):
        execute.render(self.le_output.text(), self.maya_files)

    def widget_connection(self):
        self.pb_output.clicked.connect(self.output_clicked)
        self.pb_add.clicked.connect(self.add_clicked)
        self.tw_maya_files.itemSelectionChanged.connect(self.maya_file_selected)
        self.pb_remove.clicked.connect(self.remove_clicked)
        self.pb_render.clicked.connect(self.render)
 

if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)

    window = BDRenderer()
    window.show()

    sys.exit(application.exec_())