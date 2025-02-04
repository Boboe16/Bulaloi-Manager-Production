from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6.QtCore import pyqtSignal, QObject

# Define a class for your object with dictionary properties
class DataObject(QObject):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict

# Define the main window class
class MainWindow(QMainWindow):
    # Create a signal that can carry a dictionary
    data_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.button = QPushButton('Send Data', self)
        self.button.clicked.connect(self.send_data)
        self.show()

    def send_data(self):
        # Create a dictionary with the data you want to pass
        data_dict = {"key1": "value1", "key2": "value2"}
        # Emit the signal with the dictionary
        self.data_signal.emit(data_dict)

# Define the second window class
class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()

    # Define a slot to receive the dictionary
    def receive_data(self, data_dict):
        # Access the data from the dictionary
        print("Data received: " + data_dict)

# Set up the application and the windows
app = QApplication([])
main_window = MainWindow()
second_window = SecondWindow()

# Connect the main window's signal to the second window's slot
main_window.data_signal.connect(second_window.receive_data)

app.exec()
