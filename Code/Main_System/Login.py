# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 111, 51))
        self.label.setStyleSheet(_fromUtf8("font: 75 italic 9pt \"Noto Sans\";\n"
"font: 63 italic 9pt \"URW Chancery L\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(130, 60, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 71, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 56, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Username_edit = QtGui.QLineEdit(Dialog)
        self.Username_edit.setGeometry(QtCore.QRect(180, 100, 113, 27))
        self.Username_edit.setStyleSheet(_fromUtf8("border-color: rgb(130, 186, 228);"))
        self.Username_edit.setObjectName(_fromUtf8("Username_edit"))
        self.Password_edit = QtGui.QLineEdit(Dialog)
        self.Password_edit.setGeometry(QtCore.QRect(180, 130, 113, 27))
        self.Password_edit.setStyleSheet(_fromUtf8("border-color: rgb(130, 186, 228);"))
        self.Password_edit.setObjectName(_fromUtf8("Password_edit"))
        self.Signin_button = QtGui.QPushButton(Dialog)
        self.Signin_button.setGeometry(QtCore.QRect(210, 170, 85, 27))
        self.Signin_button.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);"))
        self.Signin_button.setObjectName(_fromUtf8("Signin_button"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(60, 230, 118, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 220, 21, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(220, 230, 118, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.Register_button = QtGui.QPushButton(Dialog)
        self.Register_button.setGeometry(QtCore.QRect(160, 250, 85, 27))
        self.Register_button.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);"))
        self.Register_button.setObjectName(_fromUtf8("Register_button"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:16pt; color:#0000ff;\">Advise</span><span style=\" font-family:\'URW Chancery L\'; font-size:24pt; color:#82bae4;\">Me</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "Username:", None))
        self.label_3.setText(_translate("Dialog", "Password:", None))
        self.Signin_button.setText(_translate("Dialog", "Sign In", None))
        self.label_4.setText(_translate("Dialog", "OR", None))
        self.Register_button.setText(_translate("Dialog", "Register", None))

