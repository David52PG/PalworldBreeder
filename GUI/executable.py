from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main

class ImageProcessor:
    @staticmethod
    def process_images(name1, name2):
        images = main.mainloop(name1, name2)

        return images

class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")

        self.name1_text = QLineEdit()
        self.name2_text = QLineEdit()
        self.button = QPushButton("Show Images")
        self.next_button = QPushButton("Next Image")
        self.save_button = QPushButton("Save Image")
        self.image_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Origin:"))
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
            self.current_image_index = 0

            self.show_current_image()

    def show_current_image(self):
        if self.images:
            image = self.images[self.current_image_index]
            pixmap = QPixmap(image)
            self.image_label.setPixmap(pixmap)
            self.current_image_index = (self.current_image_index + 1) % len(self.images)

    def show_next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.show_current_image()

    def save_image(self):
        if self.images:
            image = self.images[self.current_image_index]
            # Lógica para guardar la imagen en el ordenador

app = QApplication(sys.argv)
window = ImageWindow()
window.show()
sys.exit(app.exec())
