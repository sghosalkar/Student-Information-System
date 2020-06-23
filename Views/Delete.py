from tkinter import *
import cx_Oracle


class DeleteView():
    
    def __init__(self,root):
        self.delStudent = Toplevel(root)
        self.delStudent.title("Delete St.")
        self.delStudent.geometry("500x400+200+200")
        self.loadView(self.delStudent)
    
    def loadView(self,root):
        lblAddRno = Label(root, text="enter rno", font=("arial", 18, 'bold'))
        self.entAddRno = Entry(root, bd=10, font=("arial", 18, 'bold'))
        btnDelete = Button(root, text = "Delete", font=("arial", 18, 'bold'),width=10, command= self.clickDeleteAction)
        btnBack = Button(root, text = "Back", font=("arial", 18, 'bold'),width=10, command= self.clickBackAction)
        lblAddRno.pack(pady=5)
        self.entAddRno.pack(pady=5)
        btnDelete.pack(pady=5)
        btnBack.pack(pady=5)

    def clickBackAction(self):
        self.deleteStudent.destroy()

    def clickDeleteAction(self):
        rno = self.entAddRno.get()
        conn = cx_Oracle.connect("System/abc123@localhost")
        cursor = conn.cursor()
        cursor.execute("delete from STUDENTS where rno = " + rno)
        conn.commit()
        print("delete successful")