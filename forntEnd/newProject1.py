#!/usr/bin/python
# newProject1.py is a python script to create a new project for verilog. It is developed for OSCAD software. It is written by Yogesh Dilip Save (yogessave@gmail.com).  
# Copyright (C) 2012 Yogesh Dilip Save, FOSS Project, IIT Bombay.
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.


from setPath import OSCAD_HOME
from Tkinter import *
import thread
import ttk
import sys
import subprocess, time
import template
import tkMessageBox
import os.path
import os
import toolTip
import selectOption
from string import maketrans
from PIL import Image, ImageTk



class ProjectInfo(template.MyTemplate):
  """ Class for accept model information from  user """
  def body(self, master):
  # Ask for project name  
    try:
        Label(master, text="Enter Project name:").grid(row=0)
        self.e1 = Entry(master)
        self.e1.grid(row=0, column=1,pady=10,columnspan=2)
    except:
        print "error"
# Collect project information
  def apply(self):
    """ a method for writing project information to the file"""
    self.text.insert(END, "Creating new project " + self.projectName+" ...... \n")
    self.text.yview(END)
  # Cerate directory for the project
    try:
        os.mkdir(self.projectName)
    except:
        tkMessageBox.showwarning("Error","Directory already exists")
    self.text.insert(END, "   The project directory "+self.projectName+"has been created.\n")
    self.text.yview(END)
    os.chdir(self.projectName)
    self.text.insert(END, "   Entered into the project directory "+self.projectName+"\n")
    self.text.yview(END)
  # Create model file for writing
    try:
      f = open(self.projectName+".proj","w")
    except :
      tkMessageBox.showwarning("Error","Project information file can not be wriiten. please check the file system permission")
      return 0 
    f.write("VHDLFile " + self.projectName+".vhdl\n")
    f.close()
    self.text.insert(END, "Successfully Created new project " + self.projectName+". \n")
    self.text.yview(END)
    return 1

# Validate the model information
  def validate(self):
  # Remove trailing and leading spaces from modelName
    self.projectName=self.e1.get().strip()
    if len(self.projectName):
      if os.path.exists(self.projectName+".proj"):
        tkMessageBox.showwarning("Bad input","Project already exists, please try again")
        return 0
      return 1
    else:
      tkMessageBox.showwarning("Bad input","Project Name is not specified, please try again")
      return 0

class ProjectParam(template.MyTemplate):
  """Class for specifying parameter of the model"""
  def __init__(self,parent,text,name):
  # Collect model information
    self.projectName=name
    try:
      self.OSCAD_HOME=OSCAD_HOME
    except NameError:
      try:
        self.OSCAD_HOME=os.environ["OSCAD_HOME"]
      except KeyError:
        tkMessageBox.showerror("Error OSCAD_HOME is not set","Please set OSCAD_HOME variable in .bashrc\n\nStep to set  OSCAD_HOME variable:\n  1) Open ~/.bashrc using text editor (vi ~/.bash).\n   2) Add the line \"Export OSCAD_HOME=<path_of_oscad>\" to it.\n  3) source ~/.bashrc")
        exit(0) 

  # Call base class MyTemplate
    template.MyTemplate.__init__(self,parent,text,name, buttonbox=False)

  def body(self, master):
    w, h = master.winfo_screenwidth(), master.winfo_screenheight()
    self.geometry("%dx%d" % (0.075*w, 0.6*h))
    self.resizable(0,0)
    self.attributes("-topmost",True)

  # Create and configure a menu
    """menu = Menu(self)
    self.config(menu=menu)
 
  # Create File menu
    toolmenu= Menu(menu)
    menu.add_cascade(label="Tool", menu=toolmenu)
    toolmenu.add_command(label="Text Editor  F1", command=self.openEmac)
    toolmenu.add_separator()
    toolmenu.add_command(label="GHDL Compiler  F2", command=self.openGHDL)
    toolmenu.add_separator()
    toolmenu.add_command(label="GTKwave Viewer  F12", command=self.openGTKwave)
    toolmenu.add_separator()
    toolmenu.add_command(label="Exit  F3", command=self.exitProject)
    
  # Create help menu
    helpmenu=Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Help  F1",command=self.helpProject)
    helpmenu.add_command(label="About...",command=self.aboutProjectManager)

   

    self.mainWindow = LabelFrame(self, bd=4, relief=SUNKEN,text="Tool Window",bg="lightblue")
    self.mainWindow.pack(side=TOP,fill="both", padx=5, pady=5, expand="Y")
    self.mainWindow.place(relheight=0.85, relwidth=0.99)"""
    
    # Set frame for command buttons
    buttonWindow = Frame(self, bd=4, relief=SUNKEN)
    buttonWindow.pack(side=LEFT,fill="both", padx=2, pady=2,expand="Y")
    buttonWindow.place(relheight=0.95, relwidth=0.87, rely=0.02, relx=0.07)
    
    """buttonWindow1 = Frame(self, bd=4, relief=SUNKEN)
    buttonWindow1.pack(side=TOP,fill="both", padx=2, pady=2,expand="Y")
    buttonWindow1.place(relheight=0.9, relwidth=0.25, rely=0.02, relx=0.37)
    
    buttonWindow2 = Frame(self, bd=4, relief=SUNKEN)
    buttonWindow2.pack(side=BOTTOM,fill="both", padx=2, pady=2,expand="Y")
    buttonWindow2.place(relheight=0.9, relwidth=0.25, rely=0.02, relx=0.67)"""
    
    def createToolbox():
        self.createButton(buttonWindow,self.openEmac,self.OSCAD_HOME+"/images/se.png","Schematic Editor")
        self.createButton(buttonWindow,self.openEmacTB,self.OSCAD_HOME+"/images/se.png","Schematic Editor")
        self.createButton(buttonWindow,self.openGHDL,self.OSCAD_HOME+"/images/an.png","Analysis Insertor")
        self.createButton(buttonWindow,self.openGTKwave,self.OSCAD_HOME+"/images/kn.png","NetList Converter")
    createToolbox()    
           
  # Protocol for deletion of main window
    self.protocol("WM_DELETE_WINDOW",self.exitProject)
    
  # Create shortcut keys
  """self.bind("<F2>", self.openSchematic)
    self.bind("<F3>", self.openFootprint)
    self.bind("<F4>", self.openLayout)
    self.bind("<F5>", self.openAnalysisInserter)
    self.bind("<F6>", self.openModelBuilder)
    self.bind("<F7>", self.openSubcircuitBuilder)
    self.bind("<F8>", self.openNetConverter)
    self.bind("<F9>", self.openNgspice)
    self.bind("<F10>",self.openSMCSim)
    self.bind("<F11>",self.exitProject)
    self.bind("<F1>", self.helpProject)
    self.focus_set()"""

  
  def createButton(self,frameName,commandName,imagePath,textlabel):
  # Open images
    im = Image.open(imagePath)
    photo = ImageTk.PhotoImage(im)
  
  # Create button and set label for tools
    w = Button(frameName, image=photo, width=45, height=35, command=commandName, default=ACTIVE)
    w.image=photo
    w.pack(side=TOP, padx=1, pady=1)
    toolTip.createToolTip(w,textlabel)
    
  def call_system(self,command):
      os.system(command)

  def openGHDL(self,e=None):
    self.text.insert(END, "  Opening footprint editor .........\n")
    self.text.yview(END)
  # Call all pending idle tasks, without processing any other events.
    self.update_idletasks()
    command="ghdl -a "+self.projectName+".vhdl; ghdl -a "+self.projectName+"_tb.vhdl; ghdl -e "+self.projectName+"_tb"; "ghdl -r "+self.projectName+"_tb --vcd="+self.projectName+".vcd "
    try:
        thread.start_new_thread(self.call_system,(command,))
    except Exception,err:
        print err
	
    

    '''command="ghdl -a "+self.projectName+"_tb.vhdl "
    try:
        thread.start_new_thread(self.call_system,(command,))
    except Exception,err:
        print err
    command="ghdl -e "+self.projectName+"_tb "
    try:
        thread.start_new_thread(self.call_system,(command,))
    except Exception,err:
        print err'''
    self.text.insert(END, "Select a tool from tool menu\n")
    self.text.yview(END)
  
  def openEmac(self,e=None):
    self.text.insert(END, "  Opening GHDL .........\n")
    self.text.yview(END)
  # Call all pending idle tasks, without processing any other events.
    self.update_idletasks()
    command="emacs "+self.projectName+".vhdl "
    try:
        thread.start_new_thread(self.call_system,(command,))
    except Exception,err:
        print err
    self.text.insert(END, "Select a tool from tool menu\n")
    self.text.yview(END) 
  
  def openEmacTB(self,e=None):
    self.text.insert(END, "  Opening GHDL .........\n")
    self.text.yview(END)
  # Call all pending idle tasks, without processing any other events.
    self.update_idletasks()
    command="emacs "+self.projectName+"_tb.vhdl "
    try:
        thread.start_new_thread(self.call_system,(command,))
    except Exception,err:
        print err
    self.text.insert(END, "Select a tool from tool menu\n")
    self.text.yview(END) 
  
  def openGTKwave(self,e=None):
    self.text.insert(END, "  Opening GHDL .........\n")
    self.text.yview(END)
  # Call all pending idle tasks, without processing any other events.
    self.update_idletasks()
    command="gtkwave "+self.projectName+".vcd "
    try:
        thread.start_new_thread(self.call_system,(command,))
    except Exception,err:
        print err
    self.text.insert(END, "Select a tool from tool menu\n")
    self.text.yview(END) 
  
 

  def helpProject(self,e=None):
    pass

# Display help content
  def aboutProjectManager(self,e=None):
    tkMessageBox.showinfo("About Project Manager","Created by Yogesh Dilip Save")

# Exit an Project Manager
  def exitProject(self):
    if tkMessageBox.askokcancel("QUIT","Do you really wish to quit?"):
      self.destroy()

  def apply(self):
    pass

if __name__=='__main__':
  root = Tk()
  project= ProjectInfo(root)
  projectParam = ProjectParam(root,project.modelName,project.modelType)
  mainloop()
