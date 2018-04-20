import pandas as pd
import numpy as np
import math
import os
import sys
from PyQt4 import QtCore, QtGui
import Main, Login, transfer, Register, data, template, schedule, preferences

fullDF = pd.read_csv('../../Data/Course_Data/tempSmall.csv')
majorDF = pd.read_csv('../../Data/Major_Data/MajorData.csv')
import ScheduleApp, PreferencesApp, ScheduleDialog, PreferencesDialog
import ScheduleApp.Dialog as SAD
import PreferencesApp.Dialog as PAD
 

xrange = range
student = None
vals = data.ret_vals()

def recommend(student):
    majorDF.set_value(0, 'Core', majorDF.loc[0].Core.split(","))
    majorDF.set_value(0, 'GFL', majorDF.loc[0].GFL.split(","))
    majorDF.set_value(0, 'MAT', majorDF.loc[0].MAT.split(","))
    fullDF['Prerequisites'].fillna("none", inplace=True)
    for i, row in fullDF.iterrows():
        if "," in row.Prerequisites:
            fullDF.set_value(i, 'Prerequisites', fullDF.loc[i].Prerequisites.split(","))
            
    classList = student.courses_taken
    classList[-1] = classList[-1][0:6]
    recDF = fullDF
    majDF = majorDF
    y = "none"
    recDF.to_csv('../../Data/Recommended_Data/recommendedData.csv', index=False)
    
    for x in range(len(classList)):
        recDF = recDF[recDF.Course.str.contains(classList[x]) == False]
        if classList[x] in majDF.loc[0].Core:
            majDF.loc[0].Core.remove(classList[x])
        elif classList[x] in majDF.loc[0].MAT:
            del majDF.loc[0].MAT[:]
        elif classList[x] in majDF.loc[0].GFL:
            majDF.loc[0].GFL.remove(classList[x])
        else:
            for i, row in fullDF.iterrows():
                if classList[x] in row.Course:
                    #print(row.Course)
                    if row.Course[0:6] in y:
                        break
                    if ".GLT" in row.Categories:
                        majDF.set_value(0, 'GLT', majDF.loc[0].GLT - 1)
                        if majDF.loc[0].GLT == 0:
                             for i, row in recDF.iterrows():
                                    if ".GLT" in row.Categories:
                                        recDF.set_value(i, 'Score', row.Score - 1)
                    if ".GPR" in row.Categories:
                        majDF.set_value(0, 'GPR', majDF.loc[0].GPR - 1)
                        if majDF.loc[0].GPR == 0:
                             for i, row in recDF.iterrows():
                                    if ".GRP" in row.Categories:
                                        recDF.set_value(i, 'Score', row.Score - 1)
                    if ".GHP" in row.Categories:
                        majDF.set_value(0, 'GHP', majDF.loc[0].GHP - 1)
                        if majDF.loc[0].GHP == 0:
                             for i, row in recDF.iterrows():
                                    if ".GHP" in row.Categories:
                                        recDF.set_value(i, 'Score', row.Score - 1)
                    if ".GRD" in row.Categories:
                        majDF.set_value(0, 'GRD', majDF.loc[0].GRD - 1)
                        if majDF.loc[0].GRD == 0:
                             for i, row in recDF.iterrows():
                                    if ".GRD" in row.Categories:
                                        recDF.set_value(i, 'Score', row.Score - 1)
                    if ".GL" in row.Categories or ".GN" in row.Categories:
                        majDF.set_value(0, 'GLGN', majDF.loc[0].GLGN - 1)
                        if majDF.loc[0].GLGN == 0:
                             for i, row in recDF.iterrows():
                                    if ".GL" in row.Categories or ".GN" in row.Categories:
                                        recDF.set_value(i, 'Score', row.Score - 1)
                    if ".SI" in row.Categories:
                        majDF.set_value(0, 'SI', majDF.loc[0].SI - 1)
                        if majDF.loc[0].SI == 0:
                             for i, row in recDF.iterrows():
                                    if ".SI" in row.Categories:
                                        recDF.set_value(i, 'Score', row.Score - 1)
                    if ".WI" in row.Categories:
                        majDF.set_value(0, 'WI', majDF.loc[0].WI - 1)
                        if majDF.loc[0].WI == 0:
                             for i, row in recDF.iterrows():
                                    if ".WI" in row.Categories:
                                        recDF.set_value(i, 'Score', row.Score - 1)
                    if ".CSC" in row.Categories:
                        majDF.set_value(0, 'CSC', majDF.loc[0].CSC - 1)
                        if majDF.loc[0].CSC == 0:
                             for i, row in recDF.iterrows():
                                    if ".CSC" in row.Categories:
                                        recDF.set_value(i, 'Score', row.Score - 1)
                    y = row.Course
        
    for i, row in recDF.iterrows():
        if row.Prerequisites == "none":
            continue
        if not row.Prerequisites in classList:
            recDF.drop(i, inplace=True)
            
    recDF = recDF[recDF.Score != 0]            
<<<<<<< HEAD
    #recDF.sort_values('Score', inplace=True, ascending=False)
=======
    recDF.sort_values('Score', inplace=True, ascending=False)
>>>>>>> c0c06d8965c00e4b02b96807836139f09a23e4bb
    os.remove('../../Data/Recommended_Data/recommendedData.csv')
    recDF.to_csv('../../Data/Recommended_Data/recommendedData.csv', index=False)
    return recDF
"""
class scheduleDialog(QtGui.QDialog):
    def __init__(self, parent=None, days = ['Monday','Tuesday','Wednesday','Thursday','Friday'],time=0,course_marker=0):
        QtGui.QWidget.__init__(self, parent)
        self.days = days
        self.time = time
        self.course_marker = course_marker
        self.ui = schedule.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.preferences_button.clicked.connect(self.goto_preferences)
        sched = self.get_recs()
        if len(self.days) == 0:
            self.days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
        self.ui.Schedule.setColumnCount(len(self.days))
        st = 8
        ed = 5
        if self.time == 0:
            times = 10
        else:
            st = self.time[0].split(':')
            st = int(st[0])
            ed = self.time[1].split(':')
            ed = int(ed[0])
            if ed < st:
                times = (12-st)+(12-ed)
            else:
                times = ed-st
        self.ui.Schedule.setRowCount(times)
        self.ui.Schedule.setHorizontalHeaderLabels(self.days)
        v_headers = []
        if self.time == 0:
            v_headers = ['8','9','10','11','12','1','2','3','4','5']
        else:
            if ed < st:
                for char in range(st,13):
                    v_headers.append(str(char))
                for char in range(ed+1):
                    v_headers.append(str(char))
            else:
                for char in range(st, ed):
                    v_headers.append(str(char))
        self.ui.Schedule.setVerticalHeaderLabels(v_headers)
        h = 0
        v = 0
        for itm in range(6):
            if itm >= len(sched):
                break
            self.ui.Schedule.setItem(h,v,QtGui.QTableWidgetItem(sched[itm]))
            h = (h+7) % (len(self.days)-1)
            v = (v+7) % (len(v_headers)-1)

    def goto_preferences(self):
        self.pref = preferencesDialog(self)
        self.pref.show()
        self.done(0)
    
    def get_recs(self):
        recs = []
        for course in student.university.course_list:
            if course in student.major.requirements:
                recs.append(course)
        return recs
"""
"""
class preferencesDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = preferences.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.create_schedule.clicked.connect(self.create_schedule)
        self.ui.Course_marker_cmbbx.clear()
        course_marker_adds = []
        for itm in vals[2]:
            course_marker_adds.append(itm)
        self.ui.Course_marker_cmbbx.addItems(course_marker_adds)

    def create_schedule(self):
        days = []
        if self.ui.all_days_checkbox.isChecked():
            days.append("Monday")
            days.append("Tuesday")
            days.append("Wednesday")
            days.append("Thursday")
            days.append("Friday")
        else:
            if self.ui.Monday_checkbox.isChecked():
                days.append("Monday")
            if self.ui.Tuesday_checkbox.isChecked():
                days.append("Tuesday")
            if self.ui.Wednesday_checkbox.isChecked():
                days.append("Wednesday")
            if self.ui.Thursday_checkbox.isChecked():
                days.append("Thursday")
            if self.ui.Friday_checkbox.isChecked():
                days.append("Friday")
        start = self.ui.Start_time.text()
        end = self.ui.end_time.text()
        if start == end:
            time = 0
        else:
            time = [start, end]
        course_mark = self.ui.Course_marker_cmbbx.currentText()
        sched = scheduleDialog(self, days, time, course_mark)
        sched.show()
        self.done(0)
"""
class transferDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = transfer.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Lookup_button.clicked.connect(self.lookup)
        self.ui.University_1_cmbbx.clear()
        self.ui.University_2_cmbbx.clear()
        uni_adds = []
        for itm in vals[1]:
            uni_adds.append(itm.name)
        self.ui.University_1_cmbbx.addItems(uni_adds)
        self.ui.University_2_cmbbx.addItems(uni_adds)

    def lookup(self):
        for index in xrange(self.ui.transfer_course_list.count()):
            self.ui.transfer_course_list.takeItem(index)
        uni_1 = self.ui.University_1_cmbbx.currentText()
        uni_2 = self.ui.University_2_cmbbx.currentText()
        for itm in vals[1]:
            if uni_1 == itm.name:
                uni_1 = itm
            if uni_2 == itm.name:
                uni_2 = itm
        transfer_creds = data.find_transfer(student, uni_1, uni_2)
        if not transfer_creds:
            self.ui.transfer_course_list.addItem("None")
        else:
            self.ui.transfer_course_list.addItems(transfer_creds)

class MainDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.ui = Main.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.AdviseMe.clicked.connect(self.advise_me)
        self.ui.Lookup.clicked.connect(self.lookup)
        self.ui.Email.clicked.connect(self.email)

    def advise_me(self):
        print ("Advising")
        recommendDF = recommend(student)
        self.pref = preferencesDialog(self)
        self.pref.show()

    def lookup(self):
        print ("Lookup Transfer Credit")
        self.transfer = transferDialog(self)
        self.transfer.show()

    def email(self):
        print ("Why though")
        sys.exit()

class RegisterDialog(QtGui.QDialog):
    def __init__(self, parent = None):
        super(RegisterDialog, self).__init__(parent)
        self.ui = Register.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Register_button.clicked.connect(self.register)
        self.ui.Add_button.clicked.connect(self.add)
        self.ui.major_cmbbx.clear()
        major_adds = []
        for itm in vals[0]:
            major_adds.append(itm.name)
        self.ui.major_cmbbx.addItems(major_adds)
        self.ui.Institution_cmbbx.clear()
        uni_adds = []
        for itm in vals[1]:
            uni_adds.append(itm.name)
        self.ui.Institution_cmbbx.addItems(uni_adds)

    def register(self):
        courses_taken_list = []
        for index in xrange(self.ui.course_list.count()):
            courses_taken_list.append(self.ui.course_list.item(index))
        labels = [i.text() for i in courses_taken_list]
        if labels == []:
            courses_taken = "[]"
        else:
            courses_taken = "["
            for itm in range(len(labels)-1):
                courses_taken += labels[itm] + ','
            courses_taken += labels[len(labels)-1] + ']'
        with open("Users.txt", "a+") as f:
            f.write(self.ui.Username_edit.text() + ';' + self.ui.password_edit.text() + ';' + self.ui.Institution_cmbbx.currentText() + ';' + self.ui.major_cmbbx.currentText() + ';' + courses_taken + ';\n')
            f.close()
        self.done(0)

    def add(self):
        self.ui.course_list.addItem(self.ui.Course_edit.text())

class LoginDialog(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Login.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Signin_button.clicked.connect(self.signin)
        self.ui.Register_button.clicked.connect(self.register)
        self.register = RegisterDialog(self)
        self.main = MainDialog(self)
        self.ui.Password_edit.setEchoMode(QtGui.QLineEdit.Password)

    def signin(self):
        username = self.ui.Username_edit.text()
        password = self.ui.Password_edit.text()
        with open("Users.txt", 'r+') as f:
            line = f.readline()
            while line:
                stu = line.split(';')
                if stu[0] == username and stu[1] == password:
                    stu_uni = None
                    stu_major = None
                    for itm in vals[0]:
                        if stu[3] == itm.name:
                            stu_major = itm
                    for itm in vals[1]:
                        if stu[2] == itm.name:
                            stu_uni = itm
                    stu_courses = stu[4].split(',')
                    stu_courses[0] = stu_courses[0][1:]
                    stu_courses[len(stu_courses)-1] = stu_courses[len(stu_courses)-1][:len(stu_courses[len(stu_courses)-1])]
                    global student
                    student = data.Student(stu_uni,stu_courses,stu_major,stu[0],stu[1])
                    f.close()
                    self.goto_main()
                    return
                line = f.readline()
            f.close()
            print ("No such user")

    def register(self):
        print ("Registering new user")
        self.register.show()

    def goto_main(self):
        print ("Going to main")
        self.main.show()
        self.done(0)

class am(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = template.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.login = LoginDialog()
        self.login.show()
        self.schedule = SAD()
        self.schedule.show()
        self.preferences = PAD()
        self.preferences.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    AdviseMe = am()
    sys.exit(app.exec_())
