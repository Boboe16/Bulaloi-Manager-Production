# Form implementation generated from reading ui file 'search-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class Search_Form(QtCore.QObject):
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Search"))
        self.searchInput.setPlaceholderText(_translate("Form", "......"))
        self.searchButton.setText(_translate("Form", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Search_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
