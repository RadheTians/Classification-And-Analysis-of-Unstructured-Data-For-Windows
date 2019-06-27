# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metadata.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import file_data as meta 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(" META INFORMATION OF DOCUMENT ")
        Dialog.resize(795, 531)
        self.plainTextEdit = QtWidgets.QLineEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(220, 20, 361, 41))
        self.plainTextEdit.setObjectName("input_set")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(330, 90, 141, 23))
        self.pushButton.setObjectName("btn_heat")
        self.pushButton.clicked.connect(self.Getter)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 150, 721, 311))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setFont(QtGui.QFont('SansSerif', 10))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        #self.tableWidget.resizeColumnsToContents(0)
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setVisible(False)
        self.tableWidget.resizeColumnToContents(200)
        #self.tableWidget.setFixedWidth(self.tableWidget.columnWidth(5))
        self.tableWidget.setObjectName("show_table")

        self.retranslateUi(Dialog)
        #self.Getter(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "\t\t\t\tMETA INFORMATION OF DOCUMENT "))
        self.pushButton.setText(_translate("Dialog", "GET METADATA"))

    def Getter(self):
        r=0
        input_set=self.plainTextEdit.text()
        taker=meta.MetaData(input_set)
        for one_set in taker:
            
            '''for k, v in one_set.items():
                self.tableWidget.insertRow(r)
                self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(k))
                self.tableWidget.setItem(r,1,QtWidgets.QTableWidgetItem(v))
                r+=1
                print(k,"===>>\t\t",v)'''
            self.tableWidget.insertRow(r)
            self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(one_set))
            r+=1
        self.tableWidget.setVisible(True)
            
                

        

def Caller():
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

def main():
	Caller()

main()







