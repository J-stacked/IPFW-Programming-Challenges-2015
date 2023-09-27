import os
import tkinter as Tkinter
from tkinter import * 
from tkinter.scrolledtext import *
import tkinter.filedialog as tkFileDialog
import tkinter.messagebox as tkMessageBox
import tkinter.simpledialog as tkSimpleDialog
import shutil as shutil


root = Tkinter.Tk(className=" HTML Editor")
textPad = ScrolledText(root, width=100, height=80)
file=None
filename=None
filecontent=None
matched=False
reported=False
newProjectName=" "
tagArray=[]
brackets=0
linenumber=0

def open_command():
    global file
    global filename
    filename = tkFileDialog.askopenfilename(parent=root,title='Select a file')
    file = open(filename,mode='r+')
    if file != None:
        textPad.delete("1.0",END)
        contents = file.read()
        textPad.insert('1.0',contents)
 

def save_command():
    global file
    global filename
    if file != None:
        data = textPad.get('1.0', END+'-1c')
        file=open(filename,mode="r+")
        file.seek(0)
        file.truncate()
        file.write(data)
        file.close()

def newproject_command():
    global file
    global filename
    newProjectName=tkSimpleDialog.askstring("New Project","Enter project name:")
    newProjectName=newProjectName+".html"
    file = os.getcwd()
    filename = file+"\\"+newProjectName
    file = open(filename, mode="a")  # using mode a (append) to create the file, if it is not already there.
    file = open(filename, mode='r+')  #using mode r+ to successfully edit the file.

def check_command():
    global reported
    global brackets
    global linenumber
    global tagArray
    global matched
    linenumber=1
    filecontent=textPad.get("1.0", END+"-1c")
    temporarystring=""
    tagArray=[]
    reported=False
    for f in filecontent:
        if(f=="<"):  #the begining of a tag
            brackets+=1
        if(f==">"):  #the end of a tag
            if(temporarystring=="" and reported==False):
                print("Tag empty on line "+str(linenumber))
                reported=True
            elif(len(temporarystring)>9  and reported==False):
                print("Tag name too long on line "+str(linenumber))
                reported=True
            elif(temporarystring!=""):
                tagArray.append(temporarystring)
            brackets-=1
            temporarystring=""

            
        if(brackets==1):
            if(f.isupper() and reported==False):  #checking if letter inside tag is upper case
                print("Invalid Character (uppercase) in tag on line "+str(linenumber))
                reported=True
            elif(f.isalpha()==False and f!="<" and f!="/" and f!=">" and reported==False):
                print("Invalid Character in tag on line "+str(linenumber))
                reported=True
            else:
                if(f!="<"):  #slowly adding a new tag to the tag database!
                    temporarystring=temporarystring+f

                
        if(f=="\n"):  #new line
            linenumber+=1
            if(brackets>0 and reported==False):
                print("Tag not closed on line "+str(linenumber-1))
                reported=True
                brackets=0

    for x in range(0,len(tagArray)):
        matched=False
        for y in range(0,len(tagArray)):
            if("/"+str(tagArray[y])==tagArray[x]):
                matched=True
        if(matched==False and reported==False and tagArray[x][0]=="/"):
            print("Tag "+str(tagArray[x])+" missing beggining tag.")
            reported=True

    for x in range(0,round(len(tagArray)/2)):
        matched=False
        for y in range(0,len(tagArray)):
            if("/"+str(tagArray[x])==tagArray[y]):
                matched=True
        if(matched==False and reported==False and tagArray[x][0]!="/"):
            print("Tag "+str(tagArray[x])+" missing </"+str(tagArray[x])+">")
            reported=True
                    
        
def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()
    
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New File",command=newproject_command)
filemenu.add_command(label="Open File", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_command(label="Check Syntax", command=check_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
textPad.pack()
root.mainloop()
