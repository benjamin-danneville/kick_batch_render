# This Python file uses the following encoding: utf-8

import sys

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui

 
class BDRenderer(QtWidgets.QDialog):
    def __init__(self):
        super(BDRenderer, self).__init__()
        
        # Variable
        self.maya_files = []
        self.selected_maya_files = None

        # Window title and minimum width
        self.setWindowTitle("BD Renderer")
        self.setMinimumHeight(395)
        self.setMinimumWidth(400)

        # Background
        palette_window = QtGui.QPalette()
        palette_window.setColor(QtGui.QPalette.Window, QtGui.QColor(33, 35, 41, 255))

        self.setPalette(palette_window)
    
        # Remove Question Mark
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
    
        # UI
        self.create_widget()
        self.create_layout()
        self.widget_connection()
        self.create_shortcuts()
  
    def create_widget(self):
        self.pb_up = QtWidgets.QPushButton("▲")
        self.pb_up.setFixedWidth(30)
        self.pb_up.setMinimumHeight(100)
        self.pb_up.setMaximumHeight(500)
        self.pb_down = QtWidgets.QPushButton("▼")
        self.pb_down.setFixedWidth(30)
        self.pb_down.setMinimumHeight(100)
        self.pb_down.setMaximumHeight(500)

        self.pb_render = QtWidgets.QPushButton("RENDER FILES")

        self.pb_add = QtWidgets.QPushButton("ADD")
        self.pb_remove = QtWidgets.QPushButton("REMOVE")

        self.cb_step = QtWidgets.QCheckBox("Step")
        self.cb_stylesheet = "QCheckBox {border: none; color: white;}"
        self.cb_step.setStyleSheet(self.cb_stylesheet)

        self.le_step = QtWidgets.QLineEdit()
        self.le_step.setValidator(QtGui.QIntValidator())
        self.le_step.setFixedWidth(50)
        self.le_step.setEnabled(False)
        self.le_step.setStyleSheet("color: white;  background-color: black")

        self.le_output = QtWidgets.QLineEdit()
        #self.le_output.setReadOnly(True)

        self.le_output.setPlaceholderText("Choose an output folder path")

        self.pb_output = QtWidgets.QPushButton("...")
        self.pb_output.setFixedWidth(35)

        # Palette
        self.palette_le_output = self.le_output.palette()
        self.palette_le_output.setColor(QtGui.QPalette.Base, QtGui.QColor(63, 66, 76, 255))
        self.le_output.setPalette(self.palette_le_output)
        
        self.palette_le_output_place_holder = self.le_output.palette()
        self.palette_le_output_place_holder.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(255, 255, 255, 255))
        self.le_output.setPalette(self.palette_le_output_place_holder)

    def create_layout(self):
        self.vbl_main = QtWidgets.QVBoxLayout(self)

        self.hbl_maya_files = QtWidgets.QHBoxLayout()

        self.tw_maya_files = QtWidgets.QTableWidget()
        #self.tw_maya_files.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        self.tw_maya_files.setColumnCount(1)

        self.vbl_maya_files_button = QtWidgets.QVBoxLayout()

        palette_tw_maya_files = self.tw_maya_files.palette()
        palette_tw_maya_files.setColor(QtGui.QPalette.Base, QtGui.QColor(63, 66, 76, 255))
        self.tw_maya_files.setPalette(palette_tw_maya_files)

        self.tw_maya_files.verticalHeader().setVisible(False)
        self.tw_maya_files.horizontalHeader().setVisible(False)

        self.tw_maya_files.horizontalHeader().setStretchLastSection(True)

        self.hbl_lw_button = QtWidgets.QHBoxLayout()
        self.hbl_lw_button.addWidget(self.pb_add)
        self.hbl_lw_button.addWidget(self.pb_remove)

        self.hbl_output_button = QtWidgets.QHBoxLayout()
        self.hbl_output_button.addWidget(self.le_output)
        self.hbl_output_button.addWidget(self.pb_output)

        self.hbl_settings = QtWidgets.QHBoxLayout()

        self.vbl_maya_files_button.addWidget(self.pb_up)
        self.vbl_maya_files_button.addWidget(self.pb_down)

        self.hbl_maya_files.addWidget(self.tw_maya_files)
        self.hbl_maya_files.addLayout(self.vbl_maya_files_button)

        self.vbl_step = QtWidgets.QVBoxLayout()
        self.vbl_step.addWidget(self.cb_step)
        self.vbl_step.addWidget(self.le_step)

        self.hbl_settings.addLayout(self.vbl_step)
        self.hbl_settings.setAlignment(QtCore.Qt.AlignLeft)

        self.vbl_main.addLayout(self.hbl_maya_files)
        self.vbl_main.addLayout(self.hbl_lw_button)
        self.vbl_main.addLayout(self.hbl_settings)
        self.vbl_main.addLayout(self.hbl_output_button)
        self.vbl_main.addWidget(self.pb_render)

    def output_clicked(self):
        folder_filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "Select the output renders folder")
        if folder_filepath:
            self.le_output.setText(folder_filepath)
            self.palette_le_output.setColor(QtGui.QPalette.Base, QtGui.QColor(105, 115, 130, 255))
            self.le_output.setPalette(self.palette_le_output)

    def remove_clicked(self):
        try:
            for selected_maya_file in self.selected_maya_files:
                if selected_maya_file.text() in self.maya_files:
                    self.maya_files.remove(selected_maya_file.text())
        
            self.update_maya_files()
        
        except TypeError:
            print("No items has been selected")

    def add_clicked(self):
        maya_filepaths, check = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open a maya file', '', 'Maya Ascii Files (*.ma);;All files (*.*)')
        if check:
            for maya_filepath in maya_filepaths:
                if not maya_filepath in self.maya_files:
                    self.maya_files.append(maya_filepath)
        
        self.update_maya_files()

    def maya_file_selected(self):
        self.selected_maya_files = self.tw_maya_files.selectedItems()

    def text_changed(self):
        if self.le_output.text():
            self.palette_le_output.setColor(QtGui.QPalette.Base, QtGui.QColor(105, 115, 130, 255))
            self.le_output.setPalette(self.palette_le_output)
        else:
            self.palette_le_output.setColor(QtGui.QPalette.Base, QtGui.QColor(63, 66, 76, 255))
            self.le_output.setPalette(self.palette_le_output)
            self.palette_le_output_place_holder.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor(255, 255, 255, 255))
            self.le_output.setPalette(self.palette_le_output_place_holder)

    def update_maya_files(self):
        self.tw_maya_files.clear()
        self.tw_maya_files.setRowCount(len(self.maya_files))

        for i in range(len(self.maya_files)):
            item = QtWidgets.QTableWidgetItem(self.maya_files[i])
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
            item.setBackground(QtGui.QColor(105, 115, 130, 255))
            self.tw_maya_files.setItem(i, 0, item)
    
    def step_state_changed(self, state):
        if state:
            self.le_step.setStyleSheet("color: white;  background-color: rgb(105,115,130)")
            self.le_step.setEnabled(True)
        else:
            self.le_step.setStyleSheet("color: white;  background-color: black")
            self.le_step.setEnabled(False)  
    
    def move_maya_file(self, move_number):
        try:
            if not len(self.selected_maya_files) > 1:
                new_index = None
                for selected_maya_file in self.selected_maya_files:
                    if selected_maya_file.text() in self.maya_files:
                        old_index = self.maya_files.index(selected_maya_file.text())
                        if old_index == 0 and move_number < 0:
                            new_index = old_index
                        elif old_index == len(self.maya_files) - 1 and move_number > 0:
                            new_index = old_index
                        else:
                            new_index = old_index + move_number

                        self.maya_files.remove(selected_maya_file.text())
                        self.maya_files.insert(new_index, selected_maya_file.text())
            
                self.update_maya_files()
                self.tw_maya_files.selectRow(new_index)

            else:
                print("You must select only one item to move it up or down")
        except TypeError:
            print("No items has been selected")

    def move_maya_file_up(self):
        self.move_maya_file(-1)

    def move_maya_file_down(self):
        self.move_maya_file(1)

    def render(self):
        import render
        render.render(self.le_output.text(), self.maya_files, self.le_step)

    def widget_connection(self):
        self.pb_output.clicked.connect(self.output_clicked)
        self.pb_add.clicked.connect(self.add_clicked)
        self.tw_maya_files.itemSelectionChanged.connect(self.maya_file_selected)
        self.pb_remove.clicked.connect(self.remove_clicked)
        self.pb_render.clicked.connect(self.render)
        self.le_output.textChanged.connect(self.text_changed)
        self.cb_step.stateChanged.connect(self.step_state_changed)
        self.pb_up.clicked.connect(self.move_maya_file_up)
        self.pb_down.clicked.connect(self.move_maya_file_down)

    def create_shortcuts(self):
        self.sc_up = QtWidgets.QShortcut(QtGui.QKeySequence('Up'), self)
        self.sc_up.activated.connect(self.move_maya_file_up)
        self.sc_down = QtWidgets.QShortcut(QtGui.QKeySequence('Down'), self)
        self.sc_down.activated.connect(self.move_maya_file_down)
        self.sc_remove = QtWidgets.QShortcut(QtGui.QKeySequence('Del'), self)
        self.sc_remove.activated.connect(self.remove_clicked)
 

if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)

    window = BDRenderer()
    window.show()

    sys.exit(application.exec_())