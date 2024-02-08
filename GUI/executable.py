from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main
from PySide6.QtGui import QImage
from BreedingPath import BreedingPath


class MainBox(QWidget):
    def __init__(self):
        class MainBox(QWidget):
            def __init__(self):
                super().__init__()

                # Create buttons
                breeding_path_button = QPushButton("BreedingPath")
                breeding_combo_button = QPushButton("BreedingCombo")
                possible_parents_button = QPushButton("PossibleParents")

                # Create layout
                layout = QVBoxLayout()
                layout.addWidget(breeding_path_button)
                layout.addWidget(breeding_combo_button)
                layout.addWidget(possible_parents_button)

                # Set layout for the main widget
                self.setLayout(layout)

                # Connect button click event to open BreedingPath window
                breeding_path_button.clicked.connect(self.open_breeding_path)

            def open_breeding_path(self):
                breeding_path = BreedingPath()
                breeding_path.show()


sys.exit(app.exec())
