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

class ImageProcessor:
    @staticmethod
    def process_images(name1, name2):
        images = mainloop(name1, name2)

        return images

class BreedingPath(QWidget):
    def __init__(self):
        super().__init__()

        self.name1_text = QLineEdit()
        self.name1_text.setStyleSheet("color: white; font-size: 16px;")
        self.name1_text.setFixedHeight(40)
        self.name2_text = QLineEdit()
        self.name2_text.setStyleSheet("color: white; font-size: 16px;")
        self.name2_text.setFixedHeight(40)
        self.button = Button("Show Images")
        self.next_button = Button("Next Image")
        self.save_button = Button("Save Image")
        self.image_label = QLabel()
        destination_label = QLabel("Destination:")
        destination_description = QLabel("Enter the name of the destination pal")
        destination_label.setStyleSheet("color: white; font-size: 20px;")
        destination_description.setStyleSheet("color: white; font-size: 16px;")
        origin_label = QLabel("Origin:")
        origin_description = QLabel("Enter the name of the origin pal")
        origin_label.setStyleSheet("color: white; font-size: 20px;")
        origin_description.setStyleSheet("color: white; font-size: 16px;")

        layout = QVBoxLayout()

        layout.addWidget(origin_label)
        layout.addWidget(origin_description)
        layout.addWidget(self.name1_text)
        layout.addWidget(destination_label)
        layout.addWidget(destination_description)
        layout.addWidget(self.name2_text)
        layout.addWidget(self.button)
        layout.addWidget(self.next_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

        self.button.clicked.connect(self.show_images)
        self.next_button.clicked.connect(self.show_next_image)
        self.save_button.clicked.connect(self.save_image)

        self.images = []
        self.current_image_index = 0

    def show_images(self):
        name1 = buscar_pal(self.name1_text.text())
        name2 = buscar_pal(self.name2_text.text())

        if name1 == None:
            MessageBox("Origin name not found").exec_()
        elif name2 == None:
            MessageBox("Destination name not found").exec_()
        else:
            self.images = ImageProcessor.process_images(name1, name2)
            if self.images == False:
                MessageBox("No path found between the two pals").exec_()
                self.images = []
                self.current_image_index = 0
            else: 
                self.current_image_index = 0
                self.show_current_image()

    def show_current_image(self):
        if self.images and len(self.images) <= self.current_image_index:
            MessageBox("There are not more trees").exec_()
        elif self.images:
            image = self.images[self.current_image_index]
            byte_array = QByteArray(image)
            pixmap = QPixmap()
            pixmap.loadFromData(byte_array)
            self.image_label.setPixmap(pixmap)

    def show_next_image(self):
        if self.images:
            self.current_image_index += 1
            self.show_current_image()

    def save_image(self):
        if not self.images:
            MessageBox.critical(self, "Error", "There are no image")
        elif self.images:
            image = self.images[self.current_image_index]
            qimage = QImage.fromData(image)
            file_dialog = QFileDialog()
            file_dialog.setDefaultSuffix("png")
            file_path, _ = file_dialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png)")

            if file_path:
                qimage.save(file_path, "PNG")