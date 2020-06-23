from tkinter import *
from tkinter import scrolledtext
from cx_Oracle import *

class RecordsView():
    
    def __init__(self,root):
        self.viewStudent = Toplevel(root)
        self.viewStudent.title("View St.")
        self.viewStudent.geometry("500x400+200+200")
        self.loadView(self.viewStudent)

    def loadView(self,root):
        scrollView= scrolledtext.ScrolledText(root,width=60,height=10)
        scrollView.pack()
        conn=None
        try:
            conn = connect("System/abc123@localhost")
            cursor = conn.cursor()
            cursor.execute("select rno, name, marks from STUDENTS")
            data = cursor.fetchall()
            uidata = ""
            for e in data:
                uidata = uidata + "rno = " + str(e[0]) + ", name = " + str(e[1]) + ", marks= " + str(e[2]) + "\n"
            scrollView.insert(INSERT,uidata)
        except Exception as e:
            print(e)
        finally:
            conn.close()
        