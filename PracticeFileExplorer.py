"""
Created on Tue Feb 11 15:30:02 2020

@author: jacob
"""


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, askdirectory
import Browse as Br
import os.path

    
j = tk.Tk()

j.title('File Explorer')

canvas = tk.Canvas(j, width = 300, height= 350)
canvas.pack()


filepathod = StringVar()
filepathfl = StringVar()
save_od = StringVar()
save_fl = StringVar()
save_err = StringVar()


def OD_Explorer():
   filename = askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.csv*"), 
                                                       ("all files", 
                                                        "*.*")))

   filepathod.set(os.path.normpath(filename))
   
   return(filepathod)

def FL_Explorer():
   filename = askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.csv*"), 
                                                       ("all files", 
                                                        "*.*"))) 
  
   filepathfl.set( os.path.normpath(filename))
   
   return(filepathfl)

def OD_Save():
   filename = askdirectory()
    
   save_od.set(os.path.normpath(filename))
   
   return(save_od)

def FL_Save():
   filename = askdirectory()
   
   save_fl.set(os.path.normpath(filename))
   
   return(save_fl)

def Err_Save():
   filename = askdirectory()
   
   save_err.set(os.path.normpath(filename))
   
   return(save_err)

def Go_ON():
  (filepathod.get())
  (filepathfl.get())
  (save_od.get())
  (save_fl.get())
  (save_err.get())


ODBT = tk.Button(j, text = 'Select OD File', width = 25, command = OD_Explorer)
canvas.create_window(150,50, window = ODBT)

FLBT = tk.Button(j, text = 'Select FL File', width = 25, command = FL_Explorer)
canvas.create_window(150,100, window = FLBT)

OD_SV_BT = tk.Button(j, text = 'Select OD Graph Savepath', width = 25, command = OD_Save)
canvas.create_window(150,150, window = OD_SV_BT)

FL_SV_BT = tk.Button(j, text = 'Select FL Graph Savepath', width = 25, command = FL_Save)
canvas.create_window(150,200, window = FL_SV_BT)

ERR_SV_BT = tk.Button(j, text = 'Select Error Bar Graph Savepath', width = 25, command = Err_Save)
canvas.create_window(150,250, window = ERR_SV_BT)

QUIT = tk.Button(j, text = 'Quit', width = 10, command = j.destroy)
canvas.create_window(200,300, window = QUIT)

NEXT = tk.Button(j, text = 'Next', width = 10, command = Go_ON)
canvas.create_window(100,300, window = NEXT)

j.mainloop()
