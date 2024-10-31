import tkinter as tk
from tkinter import *
import csv
import tkinter.font as tkFont
import tkinter.messagebox as messageBox
from PIL import ImageTk,Image
import time,sys
import threading
import numpy as np
import pandas as pd
import matplotlib as plt


def check():
    idfield=id_field.get()
    passwordf=password_field.get()
    font= tkFont.Font(root,family='Helvetica',size=12, weight='bold')
    if idfield=='admin' and passwordf=='123':
        newWindow = tk.Toplevel(root,width=200, height =200)
        labelExample = tk.Label(newWindow, text = "login success full",font=font)
        labelExample.pack(pady=(50,50))
        newWindow.after(3000,newWindow.destroy)
        datav()
    else:         
        newWindow = tk.Toplevel(root)
        newWindow.geometry("200x200")
        labelExample = tk.Label(newWindow, text = "Wrong id or password", font=font)
        labelExample.pack(pady=(50,50))
        newWindow.after(3000,newWindow.destroy)
        id_field.delete(0,END)
        password_field.delete(0,END)

def datav():
    for widget in root.winfo_children():
       widget.destroy()
    root.geometry("700x400")
    font= tkFont.Font(root,family='Helvetica',size=25, weight='bold')
    title= tk.Label(root, text = "          Performance analysis of the store",font=font)
    font1= tkFont.Font(root,family='Helvetica',size=12,slant='italic')
    variety = tk.Label(root,text="Variety available",font=font1)
    friendly= tk.Label(root,text="Staff cordiality",font=font1)
    quality= tk.Label(root,text="Quality of product",font=font1)
    price= tk.Label(root,text="Price of the prduct",font=font1)
    sharing=tk.Label(root,text="Recommending to others", font=font1)
    title.grid(row=1)
    variety.grid(row=3,column=0,padx=(0,200))
    friendly.grid(row=4,column=0, padx=(0,200))
    quality.grid(row=5,column=0,padx=(0,200))
    price.grid(row=6,column=0,padx=(0,200))
    sharing.grid(row=7,column=0,padx=(0,200))
    button1=Button(root, text="Analysis", fg="Black", bg="Dark grey",command=check,width=9,height=3)
    button2=Button(root, text="Analysis", fg="Black", bg="Dark grey",command=check,width=9,height=3)
    button3=Button(root, text="Analysis", fg="Black", bg="Dark grey",command=check,width=9,height=3)
    button4=Button(root, text="Analysis", fg="Black", bg="Dark grey",command=check,width=9,height=3)
    button5=Button(root, text="Analysis", fg="Black", bg="Dark grey",command=check,width=9,height=3,padx=(10,0))
    button1.grid(row=3,column=1,padx=(0,450))
    button2.grid(row=4,column=1,padx=(0,450))
    button3.grid(row=5,column=1,padx=(0,450))
    button4.grid(row=6,column=1,padx=(0,450))
    button5.grid(row=7,column=1,padx=(0,450))




root= tk.Tk()
root.title("Performance analysis")
root.geometry("490x200")
global label,label_font,label_texts,id,password,password_field 
label_font= tkFont.Font(root,family='Helvetica',size=20, weight='bold')
label=tk.Label(root, text="              Enter details to log in ",font=label_font)
label_texts= tkFont.Font(root,family='Helvetica',size=12, weight='bold')
id=tk.Label(root, text="ID ",font= label_texts)
password=tk.Label(root, text="Password ", font=label_texts)
id_field=Entry(root)
password_field=Entry(root)
label.grid(row=1)
id.grid(row=2, column=0, sticky = 'W',padx=(30,0)) 
password.grid(row=3, column=0, sticky = 'W',ipadx=30) 
id_field.grid(row=2, column=0,ipadx=30) 
password_field.grid(row=3, column=0,ipadx=30) 

button=Button(root, text="OK", fg="Black", bg="Dark grey",command=check,width=5,height=1)
button.grid(row=4)
root.mainloop()
