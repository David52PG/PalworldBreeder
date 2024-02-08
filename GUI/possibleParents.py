from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os
import main
from PySide6.QtGui import QImage

class ImageProcessor:
    @staticmethod
    def process_images(name1, name2):
        images = main.mainloop(name1, name2)

        return images

class BreedingPath(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PalworldBreeding")
        self.windowIcon = QIcon(os.path.join(os.path.dirname(os.path.dirname(__file__)), "Pal_Sphere_icon.ico"))

        self.name1_text = QLineEdit()
        self.name2_text = QLineEdit()
        self.button = QPushButton("Show Images")
        self.next_button = QPushButton("Next Image")
        self.save_button = QPushButton("Save Image")
        self.image_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("children:"))
        layout.addWidget(self.name1_text)
        layout.addWidget(QLabel("Destination:"))
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
        name1 = main.buscar_pal(self.name1_text.text())
        name2 = main.buscar_pal(self.name2_text.text())

        if name1 == None:
            QMessageBox.critical(self, "Error", "Origin name not found")
        elif name2 == None:
            QMessageBox.critical(self, "Error", "Destination name not found")
        else:
            self.images = ImageProcessor.process_images(name1, name2)
            if self.images == False:
                QMessageBox.critical(self, "No path", "No path found between the two pals")
                self.images = []
                self.current_image_index = 0
            else: 
                self.current_image_index = 0
                self.show_current_image()

    def show_current_image(self):
        if self.images and len(self.images) <= self.current_image_index:
            QMessageBox.critical(self, "End of image gallery", "There are not more trees")
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
            QMessageBox.critical(self, "Error", "There are no image")
        elif self.images:
            image = self.images[self.current_image_index]
            qimage = QImage.fromData(image)
            file_dialog = QFileDialog()
            file_dialog.setDefaultSuffix("png")
            file_path, _ = file_dialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png)")

            if file_path:
                qimage.save(file_path, "PNG")