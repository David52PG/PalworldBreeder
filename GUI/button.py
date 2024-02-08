import sys
from PySide6.QtWidgets import QPushButton
class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyle()
            
    def setStyle(self):
        self.setStyleSheet("color: white; background-color: #474747; border: 2px solid white; padding: 5px; margin: 5px;")
