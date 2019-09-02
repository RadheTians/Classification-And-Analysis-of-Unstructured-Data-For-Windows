
from PyQt5 import QtCore, QtWidgets
import sys
import Fileimformation as info

class Ui_Dialog(object):
    def __init__(self):
        self.taker_Data_Set=[]

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 600)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(220, 20, 361, 41))
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setPlaceholderText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(670, 20, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.GetterALL)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 160, 1100, 431))
        self.tableWidget.setIconSize(QtCore.QSize(10, 10))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.scrollToBottom()
        self.tableWidget.scrollToTop()
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 100, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.GetterType)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 100, 151, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.GetterCreate)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 100, 161, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.GetterModify)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(920, 100, 151, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.GetterAccess)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 161, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(True)
        self.label.setStyleSheet("bold")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(10)
        self.label.setMidLineWidth(10)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "META-DATA EXTRACTOR"))
        self.pushButton.setText(_translate("Dialog", "GET METADATA"))
        self.pushButton_2.setText(_translate("Dialog", "File Type"))
        self.pushButton_3.setText(_translate("Dialog", "File Creation Date/Time"))
        self.pushButton_4.setText(_translate("Dialog", "File Modification Date/Time"))
        self.pushButton_5.setText(_translate("Dialog", "File Access Date/Time"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Enter File Full Path </span></p></body></html>"))

    def GetterALL(self):
        r = 0
        input_set = self.plainTextEdit.toPlainText()
        self.taker_Data_Set = info.Main(input_set)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['FILE NAME','CREATION DATE/TIME',' ACCESS DATE/TIME',' MODIFICATION DATE/TIME','FILE TYPE'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

        for one_set in self.taker_Data_Set:

            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(one_set[0]))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(one_set[1]))
            self.tableWidget.setItem(r, 2, QtWidgets.QTableWidgetItem(one_set[2]))
            self.tableWidget.setItem(r, 3, QtWidgets.QTableWidgetItem(one_set[3]))
            self.tableWidget.setItem(r, 4, QtWidgets.QTableWidgetItem(one_set[4]))
            r += 1

        self.tableWidget.setVisible(True)

    def GetterType(self):
        r = 0
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['FILE NAME','FILE TYPE'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for one_set in self.taker_Data_Set:
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(one_set[0]))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(one_set[4]))
            r += 1

        self.tableWidget.setVisible(True)

    def GetterModify(self):
        r = 0
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['FILE NAME','MODIFICATION DATE/TIME'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for one_set in self.taker_Data_Set:
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(one_set[0]))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(one_set[3]))
            r += 1

        self.tableWidget.setVisible(True)

    def GetterAccess(self):
        r = 0
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['FILE NAME', 'ACCESS DATE/TIME'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for one_set in self.taker_Data_Set:
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(one_set[0]))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(one_set[2]))
            r += 1

        self.tableWidget.setVisible(True)

    def GetterCreate(self):
        r = 0
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['FILE NAME','CREATION DATE/TIME'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        for one_set in self.taker_Data_Set:
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(one_set[0]))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(one_set[1]))
            r += 1

        self.tableWidget.setVisible(True)


def Caller():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
	Caller()
