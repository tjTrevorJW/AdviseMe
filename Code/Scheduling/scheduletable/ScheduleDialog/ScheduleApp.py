import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox,QTimeEdit
from ScheduleDialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from operator import sub

class Dialog(QDialog):
    def __init__(self):
        super(Dialog,self).__init__()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        tbl = self.ui.schedule_tbl
        
<<<<<<< HEAD
        self.in_file = open('workfile.txt')
=======
        self.in_file = open('/Users/howard/PreferencesDialog/workfile')
>>>>>>> c0c06d8965c00e4b02b96807836139f09a23e4bb
        self.preference_string = self.in_file.read()

 #       self.preference_string = self.preference_string.strip('(')
#        self.preference_string = self.preference_string.strip(')')
        self.preference_string = self.preference_string.split(sep=';')

        self.preference_string = list(filter(None, self.preference_string)) # fastest

        self.emp = []
        for x in self.preference_string:
            y = x.split(sep=',')
            z = list(filter(None,y))
            self.emp.append(z)
<<<<<<< HEAD
           
        
        
=======
>>>>>>> c0c06d8965c00e4b02b96807836139f09a23e4bb
            
        
                
            
        
 #       self.preferences = (self.preference_string,)
        
        pref_btn = self.ui.preferences_btn
        rec_btn = self.ui.recommendations_btn
        make_btn = self.ui.create_schedule_btn
        lkahd_btn = self.ui.look_ahead_btn
        
        pref_btn.clicked.connect(self.gt_prefs)
        rec_btn.clicked.connect(self.gt_rec)
        make_btn.clicked.connect(self.mk_sched)
        lkahd_btn.clicked.connect(self.lkahd)
        
        
        
        

    @pyqtSlot()
    def gt_prefs(self):
        pass
        
   
    @pyqtSlot()
    def gt_rec(self):
        pass
        
    @pyqtSlot()
    def mk_sched(self):
        pass
        
        
    @pyqtSlot()
    def lkahd(self):
        pass





def main():
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    print(dialog.preference_string)
    print('\n')
    print(dialog.emp)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
