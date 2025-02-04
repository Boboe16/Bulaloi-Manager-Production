from PyQt6 import QtCore, QtWidgets
import json
import os

# Class to represent the app/game details
class CreateNewApp:
    def __init__(self, appOrGame, appPicture, appName, appRating, appDownloadLink, appDescription, appCategory, appVersion=None, appRequirement=None, appSize=None):
        self.appOrGame = appOrGame
        self.appPicture = appPicture
        self.appName = appName
        self.appRating = appRating
        self.appDownloadLink = appDownloadLink
        self.appDescription = appDescription
        self.appCategory = appCategory
        self.appVersion = appVersion
        self.appRequirement = appRequirement
        self.appSize = appSize

# Class to setup and handle the UI form
class EditForm:
    def setupUi(self, Form):
        # Set up the main form
        Form.setObjectName("Form")
        Form.resize(375, 390)
        Form.setStyleSheet("background: gray;")

        # Create a layout widget
        layoutWidget = QtWidgets.QWidget(Form)
        layoutWidget.setGeometry(QtCore.QRect(20, 10, 341, 351))
        layout = QtWidgets.QVBoxLayout(layoutWidget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Add widgets to the layout
        self.appOrGame = self.addComboBox(layout, ["App or Game", "Game", "App"])
        self.appPicture = self.addLineEdit(layout, "App Image URL")
        self.appName = self.addLineEdit(layout, "App Name")
        self.appRating = self.addLineEdit(layout, "App Rating 1 to 5")
        self.appDownloadLink = self.addLineEdit(layout, "App Download Link")
        self.appDescription = self.addLineEdit(layout, "App Description")
        self.appCategory = self.addComboBox(layout, ["Game Category", "Role-playing", "FPS", "Adventure", "Action", "Casual", "Arcade", "App Category", "Phone editor", "Task-app Management", "Video player & Editor", "Music", "Productivity"])
        self.appVersion = self.addLineEdit(layout, "App Version")
        self.appRequirement = self.addLineEdit(layout, "App Requirement")
        self.appSize = self.addLineEdit(layout, "App Size")

        # Add the "Add" button
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(290, 360, 75, 24))
        self.addButton.setText("Add")
        self.addButton.clicked.connect(self.add)

        # Retranslate the UI
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # Utility method to add a QLineEdit with a placeholder
    def addLineEdit(self, layout, placeholder):
        lineEdit = QtWidgets.QLineEdit()
        lineEdit.setPlaceholderText(placeholder)
        layout.addWidget(lineEdit)
        return lineEdit

    # Utility method to add a QComboBox with a list of items
    def addComboBox(self, layout, items):
        comboBox = QtWidgets.QComboBox()
        comboBox.addItems(items)
        layout.addWidget(comboBox)
        return comboBox

    # Method to handle the addition of a new app
    def add(self):
        # Gather data from the input fields
        newApp = CreateNewApp(
            appOrGame=self.appOrGame.currentText(),
            appPicture=self.appPicture.text(),
            appName=self.appName.text(),
            appRating=self.appRating.text(),
            appDownloadLink=self.appDownloadLink.text(),
            appDescription=self.appDescription.text(),
            appCategory=self.appCategory.currentText(),
            appVersion=self.appVersion.text(),
            appRequirement=self.appRequirement.text(),
            appSize=self.appSize.text()
        )
        
        # Save the new app data to a JSON file
        self.saveAppToFile(newApp)

    # Method to save the app data to a JSON file
    def saveAppToFile(self, app):
        directory = r'.\Bulaloi-App-Development-Experiment\next-app\public\apps-games-data'
        directory += r'\games' if app.appOrGame == "Game" else r'\apps'
        full_path = os.path.join(directory, f"{app.appName}.json")

        with open(full_path, 'w') as file:
            json.dump(app.__dict__, file, indent=4)

    # Method to set up the translations for the UI components
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCore.QCoreApplication.translate("Form", "Add"))

# Main section to run the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
