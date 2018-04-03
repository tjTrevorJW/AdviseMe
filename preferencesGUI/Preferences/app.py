import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow,QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
def main():
    #initial stuff                                                                                                                                                                   
    app = QApplication(sys.argv)
    main_window = MainWindow()


   #middle logic                                                                                                                                                                     




   #last stuff                                                                                                                                                                       
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


