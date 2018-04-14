import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox,QTimeEdit
from dialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from operator import sub

class Dialog(QDialog):
    def __init__(self):
        super(Dialog,self).__init__()
        #list that will store all info from preferences
        #to be written to file
        #must use set() function after apply
        
        info = []

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.buttons = self.ui.buttonBox.buttons()
        self.apply_button = self.buttons[2]
        self.cancel_button = self.buttons[1]
        self.ok_button = self.buttons[0]
        
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.apply_button.clicked.connect(self.apply_changes)

        self.all_chk = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"all_days_chk")
        self.all_chk.clicked.connect(self.check_all_days)
    
        self.time_from_edit =  self.get_child_widget(self.ui.time_available_grpbox,QTimeEdit,"available_from_time_edit")
        self.time_to_edit =  self.get_child_widget(self.ui.time_available_grpbox,QTimeEdit,"available_to_time_edit")

        
    
    

        
    @pyqtSlot()
    def apply_changes(self):
        
        print(self.get_all_options())
   
    def get_all_options(self):
        loc = self.get_location()
        cat = self.get_category()
        prof = self.get_professor()
        days = self.get_days()
        time_to = self.get_time_to()
        time_from = self.get_time_from()
        time_interval = self.get_time_available()
        info_pre = (loc,cat,prof,days,time_to,time_from,time_interval)
        return info_pre
        
    def get_time_available(self):
        return tuple(map(sub,self.get_time_to(), self.get_time_from()))
    def get_time_from(self):
        time_from =  self.get_child_widget(self.ui.time_available_grpbox,QTimeEdit,"available_from_time_edit")
        return (time_from.time().hour(),time_from.time().minute())
        #print(time_from.time().hour())
        #print(str(time_to.time().hour()))
    def get_time_to(self):
        time_to =  self.get_child_widget(self.ui.time_available_grpbox,QTimeEdit,"available_to_time_edit")
        return (time_to.time().hour(),time_to.time().minute())

    
    def get_category(self):
       # category = self.ui.category_grpbox.findChild(QComboBox,"category_comb")
       # category_text = str(category.currentText())
        return (self.get_cwtext(self.ui.category_grpbox,QComboBox,"category_comb"),)

    def get_location(self):
        return (self.get_cwtext(self.ui.location_grpbox,QComboBox,"location_comb"),)
        
    
    def get_days(self):
        
        return (self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"all_days_chk"),
        self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"monday_chk") ,
        self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"tues_chk"),
        self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"wed_chk"),
        self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"thurs_chk"),
        self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"fri_chk"))
    
    @pyqtSlot()
    def check_all_days(self):
        all_is_checked = self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"all_days_chk")
        if all_is_checked:
            self.check_rest()
        
    def check_rest(self):
        monday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"monday_chk")
        tuesday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"tues_chk")
        wednesday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"wed_chk")
        thursday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"thurs_chk")
        friday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"fri_chk")
        
        monday.setChecked(True)
        tuesday.setChecked(True)
        wednesday.setChecked(True)
        thursday.setChecked(True)
        friday.setChecked(True)
        
        #immediately update gui to reflect changes
        #note: choice of monday is arbitrary
        monday.repaint()
        
            

    def get_child_widget(self,parent,child_widget_type,child_name):
        child = parent.findChild(child_widget_type,child_name)
        return child

        

    def get_checkbox_helper(self,parent,child_widget_type,child_name):
        child = parent.findChild(child_widget_type,child_name)
        child_is_checked = child.isChecked()
        return child_is_checked

    def get_professor(self):
        #comma after makes it a tuple
        return (self.get_cwtext(self.ui.professor_grpbox,QComboBox,"professor_comb"),)

    def get_cwtext(self,parent,child_widget_type,child_name):
        child = parent.findChild(child_widget_type,child_name)
        child_text = str(child.currentText())
        return child_text


def main():
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
