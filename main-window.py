from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtCore import pyqtSlot, pyqtSignal, Qt
from PyQt6.QtWidgets import QMainWindow
import json, os, subprocess, time



class Save_Form(QtCore.QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 184)
        Form.setMinimumSize(QtCore.QSize(100, 100))
        Form.setStyleSheet("background-color: gray;")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(240, 140, 158, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.noButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.noButton.setObjectName("noButton")
        self.horizontalLayout.addWidget(self.noButton)
        self.commitMessage = QtWidgets.QTextEdit(parent=Form)
        self.commitMessage.setGeometry(QtCore.QRect(30, 30, 361, 101))
        self.commitMessage.setStyleSheet("background-color: white")
        self.commitMessage.setObjectName("commitMessage")
        self.saveButton.clicked.connect(lambda: self.save(self.commitMessage.toPlainText()))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("B-icon.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        Form.setWindowIcon(icon)

        self.retranslateUi(Form)
        self.noButton.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def save(self, commitMessage):
        print(commitMessage)
        directoryPath = r'.\Bulaloi-App-Production/next-app'
        fullPath = os.path.join(directoryPath)
        print(fullPath)
        command = subprocess.run(['cd', fullPath , '&&', 'git', 'add', '.', '&&', 'git', 'commit', '-m', f'"{commitMessage}"', '&&', 'git', 'push', 'origin', 'main'], shell=True, capture_output=True, text=True)
        print(command.stdout)
        print(command.returncode)
        print(command.stderr)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bulaloi Manager"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.noButton.setText(_translate("Form", "No"))
        self.commitMessage.setPlaceholderText(_translate("Form", "Commit message..."))




class Search_Form(QtCore.QObject):
    searchSignal = pyqtSignal(str)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(377, 88)
        Form.setStyleSheet("background: gray;")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 341, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchInput = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.searchInput.setObjectName("searchInput")
        self.horizontalLayout.addWidget(self.searchInput)
        self.searchButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.searchButton.clicked.connect(self.search)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("B-icon.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        Form.setWindowIcon(icon)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def search(self):
        # Gives the search input text to the Main Window, 
        # then Main Window will use it to filter the apps that has the text that Search Window gaved
        self.searchSignal.emit(self.searchInput.text()) 

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Search"))
        self.searchInput.setPlaceholderText(_translate("Form", "......"))
        self.searchButton.setText(_translate("Form", "Search"))





class Delete_Form(QtCore.QObject):
    deleteSignal = pyqtSignal(bool)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 201)
        Form.setMinimumSize(QtCore.QSize(100, 100))
        Form.setStyleSheet("background: gray;")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 401, 111))
        self.label.setMinimumSize(QtCore.QSize(131, 0))
        self.label.setStyleSheet("/*background-color: black;*/\n"
"font-size: 50px;\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 130, 158, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton.clicked.connect(self.deleteApps) # type: ignore
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("B-icon.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        Form.setWindowIcon(icon)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def deleteApps(self):
        self.deleteSignal.emit(True)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:26pt;\">Are you sure you want to</span></p><p><span style=\" font-size:26pt;\"> delete all this apps?</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Yes"))
        self.pushButton_2.setText(_translate("Form", "No"))
        QtCore.QMetaObject.connectSlotsByName(Form)





# Class to represent the app/game details
class CreateNewApp:
    def __init__(self, appOrGame, appPicture, appName, appRating, appDownloadLink, appDescription, appCategory, appVersion=None, appRequirement=None, appSize=None, appDownloads=None):
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
        self.appDownloads = appDownloads

# Class to setup and handle the UI form
class Add_Edit_Form(QtCore.QObject):
    refreshSignal = pyqtSignal(bool)
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
        self.appCategory = self.addComboBox(layout, ["Game Category", "Role-playing", "FPS", "Adventure", "Action", "Casual", "Arcade", "Addons and mods", "App Category", "Phone editor", "Task-app Management", "Video player & Editor", "Music", "Productivity"])
        self.appVersion = self.addLineEdit(layout, "App Version")
        self.appRequirement = self.addLineEdit(layout, "App Requirement")
        self.appSize = self.addLineEdit(layout, "App Size")
        self.appDownloads = self.addLineEdit(layout, "App Downloads")

        # Add the "Add" button
        self.addOrEditButton = QtWidgets.QPushButton(Form)
        self.addOrEditButton.setGeometry(QtCore.QRect(290, 360, 75, 24))
        self.addOrEditButton.setText("Add")
        self.addOrEditButton.clicked.connect(self.add)

        # Retranslate the UI
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Declare oldAppName attribute. its used to delete the old app after edit is saved, so there will be no duplicate apps
        self.oldAppName = None
        # set the addOrEdit attribute to "add" so the add button will be displayed instead of edit
        self.addOrEdit = "add"

    def updateInputs(self, app):
        # Update the input fields with the provided app data
        self.appOrGame.setCurrentText(app["appOrGame"])
        self.appPicture.setText(app["appPicture"])
        self.appName.setText(app["appName"])
        self.appRating.setText(app["appRating"])
        self.appDownloadLink.setText(app["appDownloadLink"])
        self.appDescription.setText(app["appDescription"])
        self.appCategory.setCurrentText(app["appCategory"])
        self.appVersion.setText(app["appVersion"])
        self.appRequirement.setText(app["appRequirement"])
        self.appSize.setText(app["appSize"])
        self.appDownloads.setText(app["appDownloads"])
        self.addOrEditButton.setText("Edit")
        
        # Once your app data is updated, save the oldAppName attribute so you can delete it later
        self.oldAppName = app["appName"]
        # set the addOrEdit attribute to "edit" so the edit button will be displayed instead of add
        self.addOrEdit = "edit"
        print("Signal worked")

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
        directory = r'.\Bulaloi-App-Production\next-app\public\apps-games-data'
        directory += r'\games' if app.appOrGame == "Game" else r'\apps'
        print(self.oldAppName)
        subprocess.run(['cd', directory, '&&', 'del', f'{self.oldAppName}.json'], shell=True, capture_output=True,) if self.addOrEdit == "edit" else print("No oldAppName found")
        full_path = os.path.join(directory, f"{app.appName}.json")

        with open(full_path, 'w') as file:
            json.dump(app.__dict__, file, indent=4)
        
        # Update the oldAppName attribute for future edits
        self.oldAppName = app.appName

        self.sendRefreshSignal()

    def sendRefreshSignal(self):
        self.refreshSignal.emit(True)
        
    # Method to set up the translations for the UI components
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCore.QCoreApplication.translate("Form", "Add"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("B-icon.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        Form.setWindowIcon(icon)





class Ui_MainWindow(QMainWindow):
    editSignal = pyqtSignal(dict)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 495)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("B-icon.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: gray;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea_2.setEnabled(True)
        self.scrollArea_2.setGeometry(QtCore.QRect(50, 10, 641, 411))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setBold(False)
        self.scrollArea_2.setFont(font)
        self.scrollArea_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.scrollArea_2.setMouseTracking(False)
        self.scrollArea_2.setAutoFillBackground(False)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 622, 409))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 430, 641, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addOrEditButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.addOrEditButton.setObjectName("addOrEditButton")
        self.horizontalLayout.addWidget(self.addOrEditButton)
        self.addOrEditButton.clicked.connect(self.addApp)
        self.deleteButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.deleteButton.clicked.connect(self.showDeleteWindow)
        self.searchButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.searchButton.clicked.connect(self.showSearchWindow)
        self.refreshButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout.addWidget(self.refreshButton)
        self.refreshButton.clicked.connect(self.refreshApps)
        self.saveButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.saveButton.clicked.connect(self.showSaveWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Initialize empty list to store dictionaries of the apps that will be rendered on the list
        # This is used in setupUI & search methods
        self.listOfAppDicsToIterate = []

        # Initialize empty lists to store references to dynamically created push buttons and check boxes
        self.buttons = []
        self.checkboxs = []

        self.toDeleteApps = []

        self.iterateApps(self.listOfAppDicsToIterate)
        self.retranslateUi(MainWindow)
    
    def showSaveWindow(self):
        print("Save Window opened")
        self.SaveWindow = QtWidgets.QWidget()
        self.ui = Save_Form()
        self.ui.setupUi(self.SaveWindow)
        self._translate = QtCore.QCoreApplication.translate
        self.SaveWindow.setWindowTitle(self._translate("MainWindow", "Bulaloi Manager"))
        self.SaveWindow.show()

    def showSearchWindow(self):
        print("Search Window opened")
        self.SearchWindow = QtWidgets.QWidget()
        self.ui = Search_Form()
        self.ui.setupUi(self.SearchWindow)
        self._translate = QtCore.QCoreApplication.translate
        self.SearchWindow.setWindowTitle(self._translate("MainWindow", "Bulaloi Manager"))
        self.SearchWindow.show()
        
        self.ui.searchSignal.connect(self.searchApps) 

    def searchApps(self, data):
        print(f"Searching for: {data}")

        filteredAppDicsToIterate = []

        for app in self.listOfAppDicsToIterate:
            if data in app['appName']:
                filteredAppDicsToIterate.append(app)

        print(filteredAppDicsToIterate)

        self.resetAppsList()
        self.iterateApps(filteredAppDicsToIterate, displayNoneFilteredApps=False)

    def resetAppsList(self):
        for button in self.buttons[:]:  # Iterate over a copy of the buttons list
            if button in self.scrollAreaWidgetContents_2.findChildren(QtWidgets.QPushButton):
                button.deleteLater()
                self.buttons.remove(button)
        for checkbox in self.checkboxs[:]:  # Iterate over a copy of the buttons list
            if checkbox in self.scrollAreaWidgetContents_2.findChildren(QtWidgets.QCheckBox):
                checkbox.deleteLater()
                self.checkboxs.remove(checkbox)

    def refreshApps(self):
        print("Refresh button clicked")
        self.resetAppsList()
        self.listOfAppDicsToIterate.clear()
        self.iterateApps(self.listOfAppDicsToIterate, displayNoneFilteredApps=True)
    
    def addApp(self):
        print("Add button clicked")
        self.EditWindow = QtWidgets.QWidget()
        self.ui = Add_Edit_Form()
        self.ui.setupUi(self.EditWindow)
        self._translate = QtCore.QCoreApplication.translate
        self.EditWindow.setWindowTitle(self._translate("MainWindow", "Bulaloi Manager"))
        self.EditWindow.show()

        self.ui.refreshSignal.connect(self.refreshApps)  # Connect the signal to the saveApp method of the Add_Edit_Form

    def createForSlotEdit(self, dict):
        return lambda: self.editApp(dict)

    @pyqtSlot()
    def editApp(self, dict):
        print(f"Clicked: {dict}")
        print("EditWindow opened")
        self.EditWindow = QtWidgets.QWidget()
        self.ui = Add_Edit_Form()
        self.ui.setupUi(self.EditWindow)
        self._translate = QtCore.QCoreApplication.translate
        self.EditWindow.setWindowTitle(self._translate("MainWindow", "Bulaloi Manager"))
        self.EditWindow.show()
        
        self.editSignal.connect(self.ui.updateInputs)  # Connect the signal to the updateInputs method of the EditWindow's UI
        time.sleep(1)
        self.sendDataToEditWindow(dict)
        self.ui.refreshSignal.connect(self.refreshApps)

    def sendDataToEditWindow(self, dict):
        data = dict
        self.editSignal.emit(data)

    def showDeleteWindow(self):
        print("DeleteWindow opened")
        self.DeleteWindow = QtWidgets.QWidget()
        self.ui = Delete_Form()
        self.ui.setupUi(self.DeleteWindow)
        self._translate = QtCore.QCoreApplication.translate
        self.DeleteWindow.setWindowTitle(self._translate("MainWindow", "Bulaloi Manager"))
        self.DeleteWindow.show()
        
        self.ui.deleteSignal.connect(self.deleteApps)
    
    def deleteApps(self):
        print("Delete button clicked")
        # print(f"Selected apps to delete: {self.toDeleteApps}")

        appsDir = r'./Bulaloi-App-Production/next-app/public/apps-games-data/apps/'
        gamesDir = r'./Bulaloi-App-Production/next-app/public/apps-games-data/games/'

        for app in self.toDeleteApps:
            if app["appOrGame"] == "Game":
                os.remove(gamesDir + app["appName"] + ".json")
            elif app["appOrGame"] == "App":
                os.remove(appsDir + app["appName"] + ".json")
        self.toDeleteApps = []
        self.refreshApps()

        self.DeleteWindow.close()

    def create_checkbox_slot(self, dic):
        return lambda state: self.on_checkbox_state_changed(dic, state)

    
    def on_checkbox_state_changed(self, dic, state):
        # print(f"the state is: {state}")
        print(state == Qt.CheckState.Checked)
        if Qt.CheckState(state) == Qt.CheckState.Checked:
            # print("if is working")
            if dic not in self.toDeleteApps:
                self.toDeleteApps.append(dic)
                # print("if is working but not its nested  if")
        else:
            # print("else is working")
            if dic in self.toDeleteApps:
                self.toDeleteApps.remove(dic)
                # print("else is working but not its if")
        # print(f"Selected apps to delete: {self.toDeleteApps}")

    def iterateApps(self, listToIterate, displayNoneFilteredApps=bool):
            listOfAppNames = os.listdir(r'./Bulaloi-App-Production\next-app\public\apps-games-data\apps')
            listOfGameNames = os.listdir(r'./Bulaloi-App-Production\next-app\public\apps-games-data\games')
            appsDir = r'./Bulaloi-App-Production\next-app\public\apps-games-data\apps/'
            gamesDir = r'./Bulaloi-App-Production\next-app\public\apps-games-data\games/'

            if displayNoneFilteredApps: # If displayNoneFilteredApps is `true` we will display the all the apps, if its `false` we will display the filtered apps
                for Name in listOfAppNames:
                    with open(appsDir + Name, 'r') as file:
                        data = json.load(file)
                        listToIterate.append(data)
                
                for Name in listOfGameNames:
                    with open(gamesDir + Name, 'r') as file:
                        data = json.load(file)
                        listToIterate.append(data)
            
            for index, dic in enumerate(listToIterate):
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.horizontalLayout = QtWidgets.QHBoxLayout()
                self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
                self.horizontalLayout.setSpacing(2)
                self.horizontalLayout.setObjectName(f"horizontalLayout_{index}")
                self.checkBox = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
                self.checkBox.setSizePolicy(sizePolicy)
                self.checkBox.setMinimumSize(QtCore.QSize(13, 0))
                self.checkBox.setText("")
                self.checkBox.setObjectName(f"checkBox_{index}")
                self.checkBox.stateChanged.connect(self.create_checkbox_slot(dic))
                self.horizontalLayout.addWidget(self.checkBox)
                self.pushButton = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
                self.pushButton.setSizePolicy(sizePolicy)
                self.pushButton.setMinimumSize(QtCore.QSize(150, 0))
                self.pushButton.setObjectName(f"pushButton_{index}")
                self.horizontalLayout.addWidget(self.pushButton)
                self.verticalLayout.addLayout(self.horizontalLayout)
                self.pushButton.clicked.connect(self.createForSlotEdit(dic))

                # Append the newly created pushButton to the buttons list
                self.buttons.append(self.pushButton)

                # Append the newly created checkBox to the checkboxs list
                self.checkboxs.append(self.checkBox)

                _translate = QtCore.QCoreApplication.translate
                self.pushButton.setText(_translate("MainWindow", dic['appName']))
                self.addOrEditButton.setText(_translate("MainWindow", "Add"))
                
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Bulaloi Manager"))

def showMainWindow():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())

if os.path.exists('./Bulaloi-App-Production'):
    print("Repo already cloned, skipping clone step")
    showMainWindow()
else:
    print("Cloning repo...")
    subprocess.run(['git', 'clone', 'https://github.com/Boboe16/Bulaloi-App-Production', '&&', 'cd', 'Bulaloi-App-Production/next-app'], shell=True, capture_output=True, text=True)
    showMainWindow()