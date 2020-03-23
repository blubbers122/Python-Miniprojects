from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import asksaveasfile

def doNothing():
    print("nothing")

def newFile():
    answer = tkinter.messagebox.askquestion("New File", "Create a new file?")
    if answer == "yes":
        textarea.delete(1.0, END)

def save():
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes=files, defaultextension=files)

def undo():
    print("undo")



root = Tk()
root.title("New Document")

# Main Menu
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New", command=newFile)
subMenu.add_separator()
subMenu.add_command(label="Save", command=save)
subMenu.add_command(label="Save As", command=doNothing)
subMenu.add_command(label="Exit", command=root.destroy)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=undo)



# Toolbar
toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# Text Area
textarea = Text(root, height=20, undo=TRUE)
textarea.pack(side=TOP, fill=X)

# Status Bar
status = Label(root, text="Preparing for nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)



root.mainloop()
