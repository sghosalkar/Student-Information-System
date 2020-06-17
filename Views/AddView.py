from tkinter import *


addStudent = None


def createAddView(root):
    addStudent = Toplevel(root)
    addStudent.title("Add St.")
    addStudent.geometry("500x400+200+200")
    loadView(addStudent)



def loadView(root):
    lblAddRno = Label(root, text="enter rno", font=("arial", 18, 'bold'))
    entAddRno = Entry(root, bd=10, font=("arial", 18, 'bold'))
    lblAddName = Label(root, text="enter name", font=("arial", 18, 'bold'))
    entAddName = Entry(root, bd=10, font=("arial", 18, 'bold'))
    lblAddMarks = Label(root, text="enter marks", font=("arial", 18, 'bold'))
    entAddMarks = Entry(root, bd=10, font=("arial", 18, 'bold'))
    btnSave = Button(root, text = "Save", font=("arial", 18, 'bold'),width=10)
    btnBack = Button(root, text = "Back", font=("arial", 18, 'bold'),width=10,command= clickBackAction)
    lblAddRno.pack(pady=5)
    entAddRno.pack(pady=5)
    lblAddName.pack(pady=5)
    entAddName.pack(pady=5)
    lblAddMarks.pack(pady=5)
    entAddMarks.pack(pady=5)
    btnSave.pack(pady=5)
    btnBack.pack(pady=5)

def clickBackAction():
    addStudent.withdraw()
