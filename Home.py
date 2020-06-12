from tkinter import *
from Views.AddView import createAddView


root = Tk()
root.title('S.M.S')
root.geometry("300x600+10+20")
def addClickAction():
    createAddView(root)
def viewClickAction():
    root.withdraw()
def UpdateClickAction():
    root.withdraw()
def DeleteClickAction():
    root.withdraw()
def GraphClickAction():
    root.withdraw()            
    

btnAdd = Button(root, text = "Add", font=("arial", 18, 'bold'),width=10, command=addClickAction)
btnView = Button(root, text = "View", font=("arial", 18, 'bold'),width=10, command=viewClickAction)
btnUpdate = Button(root, text = "Update", font=("arial", 18, 'bold'),width=10, command=UpdateClickAction)
btnDelete = Button(root, text = "Delete", font=("arial", 18, 'bold'),width=10, command=DeleteClickAction)
btnGraph = Button(root, text = "Graph", font=("arial", 18, 'bold'),width=10, command=GraphClickAction)

btnAdd.pack(padx=2, pady=10)
btnView.pack(padx=2, pady=10)
btnUpdate.pack(padx=2, pady=10)
btnDelete.pack(padx=2, pady=10)
btnGraph.pack(padx=2, pady=10)



root.mainloop()