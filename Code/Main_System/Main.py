# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
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
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(130, 60, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 111, 51))
        self.label.setStyleSheet(_fromUtf8("font: 75 italic 9pt \"Noto Sans\";\n"
"font: 63 italic 9pt \"URW Chancery L\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(130, 60, 118, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.AdviseMe = QtGui.QPushButton(Dialog)
        self.AdviseMe.setGeometry(QtCore.QRect(150, 110, 85, 27))
        self.AdviseMe.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);"))
        self.AdviseMe.setObjectName(_fromUtf8("AdviseMe"))
        self.Lookup = QtGui.QPushButton(Dialog)
        self.Lookup.setGeometry(QtCore.QRect(120, 150, 141, 27))
        self.Lookup.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);"))
        self.Lookup.setObjectName(_fromUtf8("Lookup"))
        self.Email = QtGui.QPushButton(Dialog)
        self.Email.setGeometry(QtCore.QRect(150, 190, 85, 27))
        self.Email.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);"))
        self.Email.setObjectName(_fromUtf8("Email"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 110, 61, 21))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);\n"
"border-color: rgb(0, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.raise_()
        self.AdviseMe.raise_()
        self.line.raise_()
        self.label.raise_()
        self.line_2.raise_()
        self.Lookup.raise_()
        self.Email.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:16pt; color:#0000ff;\">Advise</span><span style=\" font-family:\'URW Chancery L\'; font-size:24pt; color:#82bae4;\">Me</span></p></body></html>", None))
        self.AdviseMe.setText(_translate("Dialog", "AdviseMe", None))
        self.Lookup.setText(_translate("Dialog", "Lookup Transfer Credit", None))
        self.Email.setText(_translate("Dialog", "Email Advisor", None))
        self.label_2.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:8pt; color:#000000;\">Advise</span><span style=\" font-family:\'URW Chancery L\'; font-size:10pt; color:#000000;\">Me</span></p></body></html>", None))

