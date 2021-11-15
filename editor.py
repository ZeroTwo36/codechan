import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox,filedialog
import os

def createWidgets():

    global textArea
    textArea = Text(root)
    textArea.grid(sticky= N+E+S+W)
    
    menubar = Menu(root)
    root.config(menu=menubar)
    fileMenu = Menu(menubar,tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_command(label="Save as...", command=saveFileAs)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=kill)
    menubar.add_cascade(label="File",menu=fileMenu)
    
    editMenu = Menu(menubar,tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit",menu=editMenu)
    
    helpMenu = Menu(menubar,tearoff=0)
    helpMenu.add_command(label="About", command=about)
    menubar.add_cascade(label="Help",menu=helpMenu)

def about():
    messagebox.showinfo("About CodeChan","CodeChan is an Open Source Project By @ZeroTwo36\nwhich is publicly available at https://github.com/ZeroTwo36/codechan/")

def newFile():
    global textArea
    global file
    root.title("Untitled - CodeChan IDE")
    file = None
    textArea.delete(1.0,END)

def openFile():
    global textArea
    global file
    file_ = filedialog.askopenfilename(defaultextension=".txt",
    filetypes=[("text/plain","*.txt"),
    ("text/plain","*.txt"),
    ("application/python","*.py"),
    ("application/javascript","*.js"),
    ("application/c","*.c"),
    ("application/c#","*.cs"),
    ("application/c++","*.cpp"),
    ("application/php","*.php"),
    ("windows/bat","*.bat"),
    ("windows/ps1","*.ps1"),
    ("text/markdown","*.md"),
    ("text/css","*.css"),
    ("text/html","*.html"),
    ("text/json","*.json"),
    ("text/sql","*.sql"),
    ("text/cc-extension","*.cc.ext"),
    ("text/all","*.*"),
    ])
    file = file_
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - CodeChan IDE")
        textArea.delete(1.0,END)
        tmp = open(file,"rb")
        textArea.insert(1.0,tmp.read())
        tmp.close()

def saveFileAs():
    global textArea,file
    file_ = filedialog.asksaveasfilename(defaultextension=".txt",
    filetypes=[("text/plain","*.txt"),
    ("text/plain","*.txt"),
    ("application/python","*.py"),
    ("application/javascript","*.js"),
    ("application/c","*.c"),
    ("application/c#","*.cs"),
    ("application/c++","*.cpp"),
    ("application/php","*.php"),
    ("windows/bat","*.bat"),
    ("windows/ps1","*.ps1"),
    ("text/markdown","*.md"),
    ("text/css","*.css"),
    ("text/html","*.html"),
    ("text/json","*.json"),
    ("text/sql","*.sql"),
    ("text/cc-extension","*.cc.ext"),
    ("text/all","*.*"),
    ])
    file = file_
    root.title(os.path.basename(file)+" - CodeChan IDE")

def saveFile():
    global textArea,file
    print(file)
    if file == None:
        saveFileAs()

        if file == None:
            f = None
        else:
            f = open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - CodeChan IDE")
    else:
            f = open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - CodeChan IDE")

def kill():
    root.destroy()

def cut():
    global textArea
    textArea.event_generate("<<Cut>>")

def copy():
    global textArea
    textArea.event_generate("<<Copy>>")

def paste():
    global textArea
    textArea.event_generate("<<Paste>>")

root = Tk()
root.iconbitmap('favicon.ico')
root.title("Untitled - CodeChan IDE")
file = None

createWidgets()

root.mainloop()
