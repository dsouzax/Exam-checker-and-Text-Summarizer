# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import test
import test1
import Neww


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setEnabled(True)
        Dialog.resize(597, 490)
        Dialog.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(32, 74, 135);"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 90, 211, 51))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(148, 186, 183);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(177, 219, 227);"))
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 370, 201, 41))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(177, 219, 227);"))
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 180, 161, 51))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(148, 186, 183);\n"
"background-color: rgb(177, 219, 227);"))
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 270, 201, 51))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(177, 219, 227);"))
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 370, 181, 41))
        self.lineEdit_3.setStyleSheet(_fromUtf8("background-color: rgb(177, 219, 227);"))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.OpenClick)
        self.pushButton_3.clicked.connect(self.OpenClick1)
        self.pushButton_4.clicked.connect(self.OpenClick2)
        self.pushButton_2.clicked.connect(self.OpenClick3)

    def OpenClick(self):
        test.FunctionAlgo()

    def OpenClick1(self):
        test1.FunctionAlgo()

    def OpenClick2(self):
        Neww.FunctionAlgo()

    def OpenClick3(self):
        result=Neww.FunctionAlgo()
        self.lineEdit_3.setText(result)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "SUBMISSION APP", None))
        self.pushButton.setText(_translate("Dialog", "ANSWER KEY", None))
        self.pushButton_2.setText(_translate("Dialog", "RESULT :", None))
        self.pushButton_3.setText(_translate("Dialog", "UPLOAD", None))
        self.pushButton_4.setText(_translate("Dialog", "EVALUATE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
