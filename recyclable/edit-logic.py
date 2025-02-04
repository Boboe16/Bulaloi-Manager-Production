from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QScrollArea, QVBoxLayout
from PyQt6.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic Buttons in PyQt6")

        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        # Create a widget and layout for the scroll area
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_area.setWidget(scroll_widget)

        # Add multiple buttons inside the scroll container
        for i in range(5):  # Adjust the range as needed
            button = QPushButton(f"Button {i}")
            button.setObjectName(f"button_{i}")
            scroll_layout.addWidget(button)

            # Connect the button's signal to the slot with the correct argument
            button.clicked.connect(self.create_slot(f"Button {i}"))

    def create_slot(self, text):
        return lambda: self.on_button_clicked(text)

    @pyqtSlot()
    def on_button_clicked(self, text):
        print(f"Clicked: {text}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()