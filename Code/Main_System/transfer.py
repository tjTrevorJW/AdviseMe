# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transfer.ui'
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
        Dialog.resize(398, 352)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.University_1_cmbbx = QtGui.QComboBox(Dialog)
        self.University_1_cmbbx.setGeometry(QtCore.QRect(30, 50, 141, 33))
        self.University_1_cmbbx.setObjectName(_fromUtf8("University_1_cmbbx"))
        self.University_2_cmbbx = QtGui.QComboBox(Dialog)
        self.University_2_cmbbx.setGeometry(QtCore.QRect(210, 50, 151, 33))
        self.University_2_cmbbx.setObjectName(_fromUtf8("University_2_cmbbx"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 71, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 71, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Lookup_button = QtGui.QPushButton(Dialog)
        self.Lookup_button.setGeometry(QtCore.QRect(140, 100, 85, 27))
        self.Lookup_button.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);"))
        self.Lookup_button.setObjectName(_fromUtf8("Lookup_button"))
        self.transfer_course_list = QtGui.QListWidget(Dialog)
        self.transfer_course_list.setGeometry(QtCore.QRect(60, 140, 256, 151))
        self.transfer_course_list.setObjectName(_fromUtf8("transfer_course_list"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "University 1", None))
        self.label_2.setText(_translate("Dialog", "University 2", None))
        self.Lookup_button.setText(_translate("Dialog", "Look up", None))

