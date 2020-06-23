from tkinter import *
import cx_Oracle

class AddView():
    
    def __init__(self,root):
        self.addStudent = Toplevel(root)
        self.addStudent.title("Add St.")
        self.addStudent.geometry("500x400+200+200")
        self.loadView(self.addStudent)



    def loadView(self,root):
        lblAddRno = Label(root, text="enter rno", font=("arial", 18, 'bold'))
        self.entAddRno = Entry(root, bd=10, font=("arial", 18, 'bold'))
        lblAddName = Label(root, text="enter name", font=("arial", 18, 'bold'))
        self.entAddName = Entry(root, bd=10, font=("arial", 18, 'bold'))
        lblAddMarks = Label(root, text="enter marks", font=("arial", 18, 'bold'))
        self.entAddMarks = Entry(root, bd=10, font=("arial", 18, 'bold'))
        btnSave = Button(root, text = "Save", font=("arial", 18, 'bold'),width=10, command= self.clickSaveAction)
        btnBack = Button(root, text = "Back", font=("arial", 18, 'bold'),width=10, command= self.clickBackAction)
        lblAddRno.pack(pady=5)
        self.entAddRno.pack(pady=5)
        lblAddName.pack(pady=5)
        self.entAddName.pack(pady=5)
        lblAddMarks.pack(pady=5)
        self.entAddMarks.pack(pady=5)
        btnSave.pack(pady=5)
        btnBack.pack(pady=5)

    def clickBackAction(self):
        self.addStudent.destroy()

    def clickSaveAction(self):
        name = self.entAddName.get()
        print(name)
        rno = self.entAddRno.get()
        marks = self.entAddMarks.get()
        conn = cx_Oracle.connect("System/abc123@localhost")
        cursor = conn.cursor()
        cursor.execute("insert into STUDENTS values (" + rno +",'" + name + "',"  + marks+ ")")
        conn.commit()
        