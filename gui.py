from PyQt5.QtWidgets import QApplication, QLabel, QListWidgetItem, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QListWidget, QComboBox, QFrame
from PyQt5.QtGui import QFontDatabase, QFont, QColor, QPalette
from PyQt5.QtCore import Qt
from menu_app import FreshSeshApp
from recap_gui import RecapGUI
import os

class FreshSeshAI(QWidget):
    def __init__(self,fresh_sesh):
        super().__init__()
        self.fresh_sesh_app = fresh_sesh_app
        self.recap_instance = None 
        # Set window title
        self.setWindowTitle("FreshSesh AI")

        # Create main layout
        layout = QVBoxLayout()
        layout.setSpacing(10)

         # Add the font
        font_database = QFontDatabase()
        working_directory = os.getcwd()   # Get the absolute path of the current working directory
        font_path = os.path.join(working_directory, 'DOCALLISME ON STREET.ttf') 
        id = font_database.addApplicationFont(font_path)
        font_name = 'Arial'  # default font
        if id != -1:
            families = font_database.applicationFontFamilies(id)
            if families:
                font_name = families[0]
        else:
            print("Failed to load font at path: " + font_path)

        font = QFont(font_name)
        font.setPointSize(40)  # Adjust font size as needed
        logo = QLabel("FreshSesh AI")
        logo.setContentsMargins(10, 0, 0, 0) 
        logo.setFont(font)
        logo.setStyleSheet("color: blue") 

        logo_layout = QHBoxLayout()
        logo_layout.addStretch()
        logo_layout.addWidget(logo)
        logo_layout.addStretch()
        
        # For description
        description = QLabel("Start deep work faster with full context in mind.")

        desc_layout = QHBoxLayout()
        desc_layout.addStretch()
        desc_layout.addWidget(description)
        desc_layout.addStretch()

        # Add line after the description
        line = QFrame()
        line.setFrameShape(QFrame.HLine)  # Set the shape to a horizontal line
        line.setFrameShadow(QFrame.Sunken)  # Set the shadow to be sunken

        # Put items in the QVBoxLayout
        logo_desc_layout = QVBoxLayout()
        logo_desc_layout.addLayout(logo_layout)
        logo_desc_layout.addLayout(desc_layout)
        logo_desc_layout.addWidget(line)
        logo_desc_layout.setContentsMargins(0, 0, 0, 0)
        logo_desc_layout.setSpacing(0)

        layout.addLayout(logo_desc_layout)

        palette = QPalette()
        palette.setColor(QPalette.Text, QColor('blue'))
        # For QComboBoxes
        line_layout = QHBoxLayout()
        label1 = QLabel("Give me a recap of my")
        line_layout.addWidget(label1)
        self.comboBox1 = QComboBox()
        self.comboBox1.addItems(["","last commit","last 2 commits","last 3 commits"])
        self.comboBox1.setPalette(palette)
        line_layout.addWidget(self.comboBox1)

        label2 = QLabel("for repo")
        line_layout.addWidget(label2)
        self.comboBox2 = QComboBox()
        self.comboBox2.addItems(["","freshsesh","chess"])
        self.comboBox2.setPalette(palette)
        line_layout.addWidget(self.comboBox2)

        layout.addLayout(line_layout)

        # Buttons
        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run)

        self.list_widget = QListWidget()

        # Add button and list widget to the main layout
        layout.addWidget(self.run_button)

        self.setLayout(layout)


    def run(self):
        if self.comboBox1.currentText() and self.comboBox2.currentText():
            self.recap_instance = RecapGUI()
             # Pass a reference to self if you want to manipulate the parent from RecapGUI or for later use
            self.recap_instance.create_recap(self.comboBox1.currentText(), self.comboBox2.currentText())
            self.recap_instance.show()  # Make sure to show the recap_instance if it's not already visible

            

# Main loop
if __name__ == "__main__":
    app = QApplication([])
    fresh_sesh_app = FreshSeshApp()
    window = FreshSeshAI(fresh_sesh_app)  # pass it to FreshSeshAI
    window.resize(250, 150)  # You can adjust this size as needed
    window.show()
    app.exec_()
