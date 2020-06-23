from tkinter import *
import cx_Oracle

class UpdateView():
    
    def __init__(self,root):
        self.updateStudent = Toplevel(root)
        self.updateStudent.title("update St.")
        self.updateStudent.geometry("500x400+200+200")
        self.loadView(self.updateStudent)



    def loadView(self,root):
        lblAddRno = Label(root, text="enter rno", font=("arial", 18, 'bold'))
        self.entAddRno = Entry(root, bd=10, font=("arial", 18, 'bold'))
        lblAddName = Label(root, text="enter name", font=("arial", 18, 'bold'))
        self.entAddName = Entry(root, bd=10, font=("arial", 18, 'bold'))
        lblAddMarks = Label(root, text="enter marks", font=("arial", 18, 'bold'))
        self.entAddMarks = Entry(root, bd=10, font=("arial", 18, 'bold'))
        btnUpdate = Button(root, text = "Update", font=("arial", 18, 'bold'),width=10, command= self.clickUpdateAction)
        btnBack = Button(root, text = "Back", font=("arial", 18, 'bold'),width=10, command= self.clickBackAction)
        lblAddRno.pack(pady=5)
        self.entAddRno.pack(pady=5)
        lblAddName.pack(pady=5)
        self.entAddName.pack(pady=5)
        lblAddMarks.pack(pady=5)
        self.entAddMarks.pack(pady=5)
        btnUpdate.pack(pady=5)
        btnBack.pack(pady=5)

    def clickBackAction(self):
        self.updateStudent.destroy()

    def clickUpdateAction(self):
        name = self.entAddName.get()
        rno = self.entAddRno.get()
        marks = self.entAddMarks.get()
        conn = cx_Oracle.connect("System/abc123@localhost")
        cursor = conn.cursor()
        cursor.execute("update STUDENTS set name='" + name +"', marks= "  + marks +"  where rno = " + rno)
        conn.commit()
        print("update successful")