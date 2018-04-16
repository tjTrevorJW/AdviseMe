# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schedule.ui'
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
        Dialog.resize(492, 300)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Schedule = QtGui.QTableWidget(Dialog)
        self.Schedule.setGeometry(QtCore.QRect(20, 20, 256, 192))
        self.Schedule.setStyleSheet(_fromUtf8(""))
        self.Schedule.setObjectName(_fromUtf8("Schedule"))
        self.Schedule.setColumnCount(0)
        self.Schedule.setRowCount(0)
        self.preferences_button = QtGui.QPushButton(Dialog)
        self.preferences_button.setGeometry(QtCore.QRect(300, 40, 85, 27))
        self.preferences_button.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);"))
        self.preferences_button.setObjectName(_fromUtf8("preferences_button"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.preferences_button.setText(_translate("Dialog", "Preferences", None))

