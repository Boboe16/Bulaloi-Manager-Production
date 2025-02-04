import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import pyqtSignal

class SecondaryWindow(QWidget):
    sendData = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.button = QPushButton("Send Data to Main Window", self)
        self.button.clicked.connect(self.send_data)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def send_data(self):
        data = "Data from Secondary Window"
        self.sendData.emit(data)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Waiting for Data", self)
        self.button = QPushButton("Open Secondary Window", self)
        self.button.clicked.connect(self.open_secondary_window)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.secondary_window = SecondaryWindow()
        self.secondary_window.sendData.connect(self.update_label)

    def open_secondary_window(self):
        self.secondary_window.show()

    def update_label(self, data):
        self.label.setText(data)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
