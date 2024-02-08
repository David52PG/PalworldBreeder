from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os
from PySide6.QtGui import QImage
import sys
import os
from main import *
from button import Button
from MessageBox import MessageBox

class WelcomeBox(QWidget):
    def __init__(self):
        super().__init__()

        description1 = QLabel(
            "Welcome to Palworld Breeding\n"
            "This app helps find breeding combos for Palworld.\n"
            "Press one of the buttons to choose the type of search")

        layout = QVBoxLayout()

        description1.setStyleSheet("color: white; font-size: 25px;")
        description1.setAlignment(Qt.AlignCenter)

        layout.addWidget(description1)

        self.setLayout(layout)
