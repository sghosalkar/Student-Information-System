from tkinter import *
from Views.AddView import createAddView
from Views.Update import createUpdate
from Views.View  import createView
from Views.Delete import createDelete
from Views.Graph import createGraph


root = Tk()
root.title('S.M.S')
root.geometry("300x600+10+20")
def addClickAction():
    createAddView(root)
def viewClickAction():
    createView(root)
def UpdateClickAction():
    createUpdate(root)
def DeleteClickAction():
    createDelete(root)
def GraphClickAction():
    createGraph(root)            
    

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