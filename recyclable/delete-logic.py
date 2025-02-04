from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QScrollArea, QCheckBox
from PyQt6.QtCore import Qt, pyqtSlot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic Checkboxes in PyQt6")

        # Initialize the array to store selected app names
        self.selected_apps = []

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

        # Add multiple checkboxes inside the scroll container
        app_names = [f"App {i}" for i in range(5)]  # Example app names
        for app_name in app_names:
            checkbox = QCheckBox(app_name)
            checkbox.setObjectName(f"checkbox_{app_name}")
            scroll_layout.addWidget(checkbox)

            # Connect the checkbox's stateChanged signal to the slot with the correct argument
            checkbox.stateChanged.connect(self.create_checkbox_slot(app_name))

    def create_checkbox_slot(self, app_name):
        return lambda state: self.on_checkbox_state_changed(app_name, state)

    @pyqtSlot()
    def on_checkbox_state_changed(self, app_name, state):
        print(f"the state is: {state}")
        print(state == Qt.CheckState.Checked)
        if Qt.CheckState(state) == Qt.CheckState.Checked:
            print("if is working")
            if app_name not in self.selected_apps:
                self.selected_apps.append(app_name)
                print("if is working but not its nested  if")
        else:
            print("else is working")
            if app_name in self.selected_apps:
                self.selected_apps.remove(app_name)
                print("else is working but not its if")
        print(f"Selected apps: {self.selected_apps}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
