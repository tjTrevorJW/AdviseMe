# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
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
        self.label.setGeometry(QtCore.QRect(100, 20, 71, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 71, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 80, 71, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 110, 56, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Username_edit = QtGui.QLineEdit(Dialog)
        self.Username_edit.setGeometry(QtCore.QRect(180, 20, 113, 27))
        self.Username_edit.setObjectName(_fromUtf8("Username_edit"))
        self.password_edit = QtGui.QLineEdit(Dialog)
        self.password_edit.setGeometry(QtCore.QRect(180, 50, 113, 27))
        self.password_edit.setObjectName(_fromUtf8("password_edit"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 170, 151, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(40, 190, 141, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.Course_edit = QtGui.QLineEdit(Dialog)
        self.Course_edit.setGeometry(QtCore.QRect(50, 210, 113, 27))
        self.Course_edit.setObjectName(_fromUtf8("Course_edit"))
        self.course_list = QtGui.QListWidget(Dialog)
        self.course_list.setGeometry(QtCore.QRect(80, 240, 256, 61))
        self.course_list.setObjectName(_fromUtf8("course_list"))
        self.Add_button = QtGui.QPushButton(Dialog)
        self.Add_button.setGeometry(QtCore.QRect(210, 210, 85, 27))
        self.Add_button.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);"))
        self.Add_button.setObjectName(_fromUtf8("Add_button"))
        self.Institution_cmbbx = QtGui.QComboBox(Dialog)
        self.Institution_cmbbx.setGeometry(QtCore.QRect(180, 80, 111, 21))
        self.Institution_cmbbx.setObjectName(_fromUtf8("Institution_cmbbx"))
        self.major_cmbbx = QtGui.QComboBox(Dialog)
        self.major_cmbbx.setGeometry(QtCore.QRect(180, 110, 111, 21))
        self.major_cmbbx.setObjectName(_fromUtf8("major_cmbbx"))
        self.Register_button = QtGui.QPushButton(Dialog)
        self.Register_button.setGeometry(QtCore.QRect(290, 160, 85, 27))
        self.Register_button.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);"))
        self.Register_button.setObjectName(_fromUtf8("Register_button"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Username:", None))
        self.label_2.setText(_translate("Dialog", "Password:", None))
        self.label_3.setText(_translate("Dialog", "Institution:", None))
        self.label_4.setText(_translate("Dialog", "Major:", None))
        self.label_5.setText(_translate("Dialog", "Enter completed courses:", None))
        self.Add_button.setText(_translate("Dialog", "Add", None))
        self.Register_button.setText(_translate("Dialog", "Register", None))

