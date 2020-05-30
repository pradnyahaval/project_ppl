
''' STUD INFO APP FOR HOSTEL WARDENS '''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

import sys

from os import path

from PyQt5.uic import loadUiType

FROM_CLASS,_=loadUiType(path.join(path.dirname('__file__'), "main.ui"))


import sqlite3


class Main(QMainWindow, FROM_CLASS):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()

    def Handel_Buttons(self):
        self.search_button.clicked.connect(self.GET_DATA)
        self.add_button.clicked.connect(self.ADD_DATA)
        self.find_record_button.clicked.connect(self.FIND_DATA)
        self.delete_button.clicked.connect(self.DELETE_DATA)
        
    #by clicking search button
    def GET_DATA(self):
        db=sqlite3.connect("student.db")
        cursor1=db.cursor()
        cursor2=db.cursor()
        cursor3=db.cursor()
        cursor4=db.cursor()
        cursor5=db.cursor()
        
        stud_mis=int(self.mis_input.text())

        try:  #command for collecting info from database
            stud_name="SELECT Name from stud_table WHERE MIS = ?"
            stud_branch="SELECT Branch from stud_table WHERE MIS= ? "
            stud_cgpa="SELECT CGPA from stud_table WHERE MIS = ?"
            stud_hostel_block="SELECT HostelBlock from stud_table WHERE MIS = ?"
            stud_room_no="SELECT RoomNo from stud_table WHERE MIS = ?"
        
            result_n=cursor1.execute(stud_name, [stud_mis])
            result_b=cursor2.execute(stud_branch, [stud_mis])
            result_c=cursor3.execute(stud_cgpa, [stud_mis])
            result_h=cursor4.execute(stud_hostel_block, [stud_mis])
            result_r=cursor5.execute(stud_room_no, [stud_mis])

            # if [0] is not used, result will print as tuple
            #printing name, branch, cgpa, hostel block, room no 
            self.lbl_name.setText(str(result_n.fetchone()[0]))
            self.lbl_branch.setText(str(result_b.fetchone()[0]))
            self.lbl_cgpa.setText(str(result_c.fetchone()[0]))
            self.lbl_hostel_block.setText(str(result_h.fetchone()[0]))
            self.lbl_room_no.setText(str(result_r.fetchone()[0]))

        except:
            msg=QMessageBox()
            msg.setWindowTitle("Invalid Input")
            msg.setInformativeText("Entered MIS is not valid\nPlease try again")
            msg.setIcon(QMessageBox.Information)
            
            #we can set Icon as Information, Question, Warning, Error
            msg.setStandardButtons(QMessageBox.Ok)

            x=msg.exec_()
        
        #we don't required refresh button, bcuz we have used signal and slots in qt designers
    
    def ADD_DATA(self):
        db=sqlite3.connect("student.db")
        cursor=db.cursor()

        try:
            self.mis=self.line_mis.text()
            self.name=self.line_name.text()
            self.branch=self.line_branch.text()
            self.cgpa=self.line_cgpa.text()
            self.hostel_block=self.line_hostel_block.text()
            self.room_no=self.line_room_no.text()

            row=(self.mis, self.name, self.branch, self.cgpa, self.hostel_block, self.room_no)
            command="INSERT INTO stud_table(MIS, Name, Branch, CGPA, HostelBlock, RoomNo)VALUES(?, ?, ?, ?, ?, ?)"

            cursor.execute(command, row)
            db.commit()

            msg=QMessageBox()
            msg.setWindowTitle("Record updation")
            msg.setText("Record saved successfully")
            msg.setIcon(QMessageBox.Information)

            x=msg.exec_()

        except:
            print("No")


    def FIND_DATA(self):
        db=sqlite3.connect("student.db")
        cursor=db.cursor()
        

        stud_mis=int(self.mis_input_1.text())
        try:
            stud_name="SELECT Name from stud_table WHERE MIS = ?"
            result_n=cursor.execute(stud_name, [stud_mis])
            self.lbl_name_1.setText(str(result_n.fetchone()[0]))
            
        except:
            msg=QMessageBox()
            msg.setWindowTitle("Invalid Input")
            msg.setInformativeText("Entered MIS is not valid")
            msg.setIcon(QMessageBox.Information)
            
            #we can set Icon as Information, Question, Warning, Error
            msg.setStandardButtons(QMessageBox.Ok)

            x=msg.exec_()


    def DELETE_DATA(self):
        db=sqlite3.connect("student.db")
        cursor1=db.cursor()
        try:
            name=self.FIND_DATA()
            command="DELETE FROM stud_table WHERE Name=?"

            cursor1.execute(command, name)

            db.commit()
            msg=QMessageBox()
            msg.setWindowTitle("Record deletion")
            msg.setText("Record deleted successfully")
            msg.setIcon(QMessageBox.Information)

        except:
            msg=QMessageBox()
            msg.setWindowTitle("Invalid Input")
            msg.setInformativeText("Entered MIS is not valid")
            msg.setIcon(QMessageBox.Information)
            
            #we can set Icon as Information, Question, Warning, Error
            msg.setStandardButtons(QMessageBox.Ok)

            x=msg.exec_()
            
            
        
def main():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__=='__main__':
    main()





    
