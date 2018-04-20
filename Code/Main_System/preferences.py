# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
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
        Dialog.resize(678, 361)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 651, 251))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.all_days_checkbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.all_days_checkbox.setObjectName(_fromUtf8("all_days_checkbox"))
        self.horizontalLayout.addWidget(self.all_days_checkbox)
        self.Monday_checkbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.Monday_checkbox.setObjectName(_fromUtf8("Monday_checkbox"))
        self.horizontalLayout.addWidget(self.Monday_checkbox)
        self.Tuesday_checkbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.Tuesday_checkbox.setObjectName(_fromUtf8("Tuesday_checkbox"))
        self.horizontalLayout.addWidget(self.Tuesday_checkbox)
        self.Wednesday_checkbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.Wednesday_checkbox.setObjectName(_fromUtf8("Wednesday_checkbox"))
        self.horizontalLayout.addWidget(self.Wednesday_checkbox)
        self.Thursday_checkbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.Thursday_checkbox.setObjectName(_fromUtf8("Thursday_checkbox"))
        self.horizontalLayout.addWidget(self.Thursday_checkbox)
        self.Friday_checkbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.Friday_checkbox.setObjectName(_fromUtf8("Friday_checkbox"))
        self.horizontalLayout.addWidget(self.Friday_checkbox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Start_time = QtGui.QTimeEdit(self.verticalLayoutWidget)
        self.Start_time.setObjectName(_fromUtf8("Start_time"))
        self.horizontalLayout_2.addWidget(self.Start_time)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.end_time = QtGui.QTimeEdit(self.verticalLayoutWidget)
        self.end_time.setObjectName(_fromUtf8("end_time"))
        self.horizontalLayout_2.addWidget(self.end_time)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.Course_marker_cmbbx = QtGui.QComboBox(self.verticalLayoutWidget)
        self.Course_marker_cmbbx.setObjectName(_fromUtf8("Course_marker_cmbbx"))
        self.verticalLayout.addWidget(self.Course_marker_cmbbx)
        self.create_schedule = QtGui.QPushButton(Dialog)
        self.create_schedule.setGeometry(QtCore.QRect(260, 300, 101, 27))
        self.create_schedule.setStyleSheet(_fromUtf8("background-color: rgb(130, 186, 228);"))
        self.create_schedule.setObjectName(_fromUtf8("create_schedule"))
        self.verticalLayoutWidget.raise_()
        self.label.raise_()
        self.label.raise_()
        self.create_schedule.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Days Available", None))
        self.all_days_checkbox.setText(_translate("Dialog", "All Days", None))
        self.Monday_checkbox.setText(_translate("Dialog", "Monday", None))
        self.Tuesday_checkbox.setText(_translate("Dialog", "Tuesday", None))
        self.Wednesday_checkbox.setText(_translate("Dialog", "Wednesday", None))
        self.Thursday_checkbox.setText(_translate("Dialog", "Thursday", None))
        self.Friday_checkbox.setText(_translate("Dialog", "Friday", None))
        self.label_2.setText(_translate("Dialog", "Time Available", None))
        self.label_3.setText(_translate("Dialog", "to", None))
        self.label_4.setText(_translate("Dialog", "Course Marker", None))
        self.create_schedule.setText(_translate("Dialog", "Create Schedule", None))

