import json
import os

listOfFileNames = os.listdir(r'./Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\apps')
dir = r'./Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\apps/'
listOfDics = []

for fileName in listOfFileNames:
    with open(dir + fileName, 'r') as file:
        data = json.load(file)
        listOfDics.append(data)

print(listOfDics)

for dic in listOfDics:
    print(dic['appName'])
    
    # self.iterateAppsAndSetWindowTitle()

    # def iterateAppsAndSetWindowTitle(self):
    #         listOfAppNames = os.listdir(r'./Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\apps')
    #         listOfGameNames = os.listdir(r'./Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\games')
    #         appsDir = r'./Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\apps/'
    #         gamesDir = r'./Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\games/'
    #         listOfDics = []

    #         for Name in listOfAppNames:
    #             with open(appsDir + Name, 'r') as file:
    #                 data = json.load(file)
    #                 listOfDics.append(data)
            
    #         for Name in listOfGameNames:
    #             with open(gamesDir + Name, 'r') as file:
    #                 data = json.load(file)
    #                 listOfDics.append(data)
            
    #         for index, dic in enumerate(listOfDics):
    #             self.scrollAreaWidgetContents = QtWidgets.QWidget()
    #             self.horizontalLayout = QtWidgets.QHBoxLayout()
    #             self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
    #             self.horizontalLayout.setSpacing(2)
    #             self.horizontalLayout.setObjectName(f"horizontalLayout_{index}")
    #             self.checkBox = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents)
    #             sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
    #             sizePolicy.setHorizontalStretch(0)
    #             sizePolicy.setVerticalStretch(0)
    #             sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
    #             self.checkBox.setSizePolicy(sizePolicy)
    #             self.checkBox.setMinimumSize(QtCore.QSize(13, 0))
    #             self.checkBox.setText("")
    #             self.checkBox.setObjectName(f"checkBox_{index}")
    #             self.horizontalLayout.addWidget(self.checkBox)
    #             self.pushButton = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
    #             sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
    #             sizePolicy.setHorizontalStretch(0)
    #             sizePolicy.setVerticalStretch(0)
    #             sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
    #             self.pushButton.setSizePolicy(sizePolicy)
    #             self.pushButton.setMinimumSize(QtCore.QSize(150, 0))
    #             self.pushButton.setObjectName(f"pushButton_{index}")
    #             self.horizontalLayout.addWidget(self.pushButton)
    #             self.verticalLayout.addLayout(self.horizontalLayout)
                
    #             _translate = QtCore.QCoreApplication.translate
    #             self.pushButton.setText(_translate("MainWindow", dic['appName']))
    #             MainWindow.setWindowTitle(_translate("MainWindow", "Bulaloi Manager"))
    #             self.addButton.setText(_translate("MainWindow", "Add"))
    #             self.deleteButton.setText(_translate("MainWindow", "Delete"))
    #             self.searchButton.setText(_translate("MainWindow", "Search"))
    #             self.refreshButton.setText(_translate("MainWindow", "Refresh"))
    #             self.saveButton.setText(_translate("MainWindow", "Save"))
