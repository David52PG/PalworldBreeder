from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os
from PySide6.QtGui import QImage
import sys
import os
import main
from button import Button
from MessageBox import MessageBox

class BreedingCombo(QWidget):
    def __init__(self):
        super().__init__()

        self.name1_text = QLineEdit()
        self.name1_text.setStyleSheet("color: white; font-size: 16px;")
        self.name1_text.setFixedHeight(40)

        self.name2_text = QLineEdit()
        self.name2_text.setStyleSheet("color: white; font-size: 16px;")
        self.name2_text.setFixedHeight(40)

        destination_label = QLabel("Parent2:")
        destination_label.setStyleSheet("color: white; font-size: 20px;")

        destination_description = QLabel("Enter the name of the other parent")
        destination_description.setStyleSheet("color: white; font-size: 16px;")

        origin_label = QLabel("Parent1:")
        origin_label.setStyleSheet("color: white; font-size: 20px;")

        origin_description = QLabel("Enter the name of one parent")
        origin_description.setStyleSheet("color: white; font-size: 16px;")

        self.showChildren = Button("Show Children")
        self.showChildren.clicked.connect(self.show_Children)

        self.Children = QLabel()
        self.Children.setStyleSheet("color: white; font-size: 20px;")
        
        layout = QVBoxLayout()

        layout.addWidget(origin_label)
        layout.addWidget(origin_description)
        layout.addWidget(self.name1_text)
        layout.addWidget(destination_label)
        layout.addWidget(destination_description)
        layout.addWidget(self.name2_text)
        layout.addWidget(self.showChildren)
        layout.addWidget(self.Children)

        self.setLayout(layout)

    def show_Children(self):
        name1 = main.buscar_pal(self.name1_text.text())
        name2 = main.buscar_pal(self.name2_text.text())
        if self.name1_text.text() == None or self.name2_text.text() == None:
            message_box = MessageBox("Parents name error").exec_()
            return
        self.Children.setText(main.buscar_apareamiento(name1, name2)[0])