import sys
from PySide6.QtWidgets import QApplication, QMessageBox

class MessageBox(QMessageBox):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setStyle()
            
    def setStyle(self):
        self.setStyleSheet("QMessageBox { background-color: black; } QLabel { color: white; }")
