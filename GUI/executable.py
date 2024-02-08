from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os
from button import Button
from BreedingPath import BreedingPath
from BreedingCombo import BreedingCombo
from possibleParents import PossibleParents
from PySide6.QtGui import QImage


class MainBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")

        self.resize(800, 600)
        self.setWindowTitle("PalworldBreeding")
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.dirname(__file__)), "Pal_Sphere_icon.ico")))
        # Create buttons
        breeding_path_button = Button("BreedingPath")
        breeding_combo_button = Button("BreedingCombo")
        possible_parents_button = Button("PossibleParents")

        # Create layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(breeding_path_button)
        button_layout.addWidget(breeding_combo_button)
        button_layout.addWidget(possible_parents_button)
        # Create stacked widget to hold the windows
        self.stacked_widget = QStackedWidget()

        # Create layout for the main widget
        layout = QVBoxLayout()
        layout.addLayout(button_layout)
        layout.addWidget(self.stacked_widget)

        # Set layout for the main widget
        self.setLayout(layout)

        # Connect button click events to show respective windows
        breeding_path_button.clicked.connect(self.show_breeding_path)
        breeding_combo_button.clicked.connect(self.show_breeding_combo)
        possible_parents_button.clicked.connect(self.show_possible_parents)

    def show_breeding_path(self):
        breeding_path = BreedingPath()
        self.stacked_widget.addWidget(breeding_path)
        self.stacked_widget.setCurrentWidget(breeding_path)

    def show_breeding_combo(self):
        breeding_combo = BreedingCombo()
        self.stacked_widget.addWidget(breeding_combo)
        self.stacked_widget.setCurrentWidget(breeding_combo)

    def show_possible_parents(self):
        possible_parents = PossibleParents()
        self.stacked_widget.addWidget(possible_parents)
        self.stacked_widget.setCurrentWidget(possible_parents)


app = QApplication(sys.argv)
window = MainBox()
window.show()
sys.exit(app.exec())