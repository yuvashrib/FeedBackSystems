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
import matplotlib.pyplot as plt


global dataset
dataset=pd.read_csv("feedback.csv")
dataset["Q1"].fillna(0,inplace=True)
dataset["Q2"].fillna(0,inplace=True)
dataset["Q3"].fillna(0,inplace=True)
dataset["Q4"].fillna(0,inplace=True)
dataset["Q5"].fillna(0,inplace=True)



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
        #img = ImageTk.PhotoImage(Image.open("cross.png"))
        #wrong = tk.Label(newWindow, image = img)
        labelExample = tk.Label(newWindow, text = "Incorrect ID or Password", font=font)
        #wrong.grid(row=0)
        #labelExample.grid(row=2)
        #newWindow.after(3000,newWindow.destroy)
        canvas = tk.Canvas(newWindow, width=60, height=60) 
        canvas.grid(row=0,padx=(15,0))
        img = ImageTk.PhotoImage(Image.open("cross.jpg"))
        canvas.img=img
        bg = canvas.create_image(0,0, image=img,anchor=tk.NW)
        labelExample.grid(row=1)
        id_field.delete(0,END)
        password_field.delete(0,END)
      

def datav():
    for widget in root.winfo_children():
       widget.destroy()
    root.geometry("700x400")
    font= tkFont.Font(root,family='Helvetica',size=25, weight='bold')
    title= tk.Label(root, text = "          Performance analysis of the store",font=font)
    font1= tkFont.Font(root,family='Helvetica',size=17,slant='italic')
    variety = tk.Label(root,text="Variety available",font=font1)
    friendly= tk.Label(root,text="Staff cordiality",font=font1)
    quality= tk.Label(root,text="Quality of product",font=font1)
    price= tk.Label(root,text="Price of the prduct",font=font1)
    sharing=tk.Label(root,text="Recommending to others", font=font1)
    title.grid(row=1)
    variety.grid(row=3,column=0,padx=(0,200))
    friendly.grid(row=4,column=0,padx=(0,200))
    quality.grid(row=5,column=0,padx=(0,200))
    price.grid(row=6,column=0,padx=(0,200))
    sharing.grid(row=7,column=0,padx=(0,200))
    button1=Button(root, text="Analysis", fg="Black", bg="Dark grey",command=variety_func,width=9,height=2)
    button2=Button(root, text="Analysis", fg="Black", bg="Dark grey",command=staff,width=9,height=2)
    button3=Button(root, text="Analysis", fg="Black", bg="Dark grey",command=quality_func,width=9,height=2)
    button4=Button(root, text="Analysis", fg="Black", bg="Dark grey",command=price_fuc,width=9,height=2)
    button5=Button(root, text="Analysis", fg="Black", bg="Dark grey",command=recommend,width=9,height=2)
    button6=Button(root, text="OverAll Analysis", fg="Black", bg="Dark grey",command=overall,width=15,height=3)
    button1.grid(row=3,column=1,padx=(0,450),pady=5)
    button2.grid(row=4,column=1,padx=(0,450),pady=5)
    button3.grid(row=5,column=1,padx=(0,450),pady=5)
    button4.grid(row=6,column=1,padx=(0,450),pady=5)
    button5.grid(row=7,column=1,padx=(0,450),pady=5)
    button6.place(relx=.83,rely=.8)
def variety_func():
    font2= {'family': 'Franklin Gothic Medium',
            'color':'darkred',
            'weight':'bold',
            'size': 30
         }
  
    
    c1= dataset[dataset['Q1'] == 1].shape[0]
    c2 = dataset[dataset['Q1'] == 2].shape[0]
    c3= dataset[dataset['Q1'] == 3].shape[0]
    c4= dataset[dataset['Q1'] == 4].shape[0]
    c5= dataset[dataset['Q1'] == 5].shape[0]
    
    noof=[]
    noof.append(c1)
    noof.append(c2)
    noof.append(c3)
    noof.append(c4)
    noof.append(c5)
    pos=np.arange(5)    
    columns=[1,2,3,4,5]
    colors=['lightcoral','firebrick','crimson','maroon','indianred']
    plt.figure(figsize=(20,10))
    plt.bar(pos,noof,color=colors,width=0.6)
    plt.xticks(pos,columns)
    plt.xticks(size=13,color='darkred')
    plt.yticks(size=13,color='darkred')
    plt.xlabel('Rating',color='darkred',size=20)
    plt.ylabel('Number of customers', color='darkred',size=20)
    plt.title("Number of people who found good variety of clothes",fontdict=font2)
    plt.show()
    

      

def staff():
    font2= {'family': 'Franklin Gothic Medium',
            'color':'darkblue',
            'weight':'bold',
            'size': 30
         }
   
    
    c1= dataset[dataset['Q2'] == 1].shape[0]
    c2 = dataset[dataset['Q2'] == 2].shape[0]
    c3= dataset[dataset['Q2'] == 3].shape[0]
    c4= dataset[dataset['Q2'] == 4].shape[0]
    c5= dataset[dataset['Q2'] == 5].shape[0]
    
    noof=[]
    noof.append(c1)
    noof.append(c2)
    noof.append(c3)
    noof.append(c4)
    noof.append(c5)
    pos=np.arange(5)    
    columns=[1,2,3,4,5]
    colors=['deepskyblue','teal','cornflowerblue','steelblue','paleturquoise']
    plt.figure(figsize=(15,10))
    plt.bar(pos,noof,color=colors,width=0.6)
    plt.xticks(pos,columns)
    plt.xticks(size=13,color='darkblue')
    plt.yticks(size=13,color='darkblue')
    plt.xlabel('Rating',color='darkblue',size=20)
    plt.ylabel('Number of customers', color='darkblue',size=20)
    plt.title("Number of people who found staff friendly",fontdict=font2)
    plt.show()
    


def quality_func():
    font2= {'family': 'Franklin Gothic Medium',
            'color':'black',
            'weight':'bold',
            'size': 30
        }
    
    c1= dataset[dataset['Q3'] == 1].shape[0]
    c2 = dataset[dataset['Q3'] == 2].shape[0]
    c3= dataset[dataset['Q3'] == 3].shape[0]
    c4= dataset[dataset['Q3'] == 4].shape[0]
    c5= dataset[dataset['Q3'] == 5].shape[0]
    
    noof=[]
    noof.append(c1)
    noof.append(c2)
    noof.append(c3)
    noof.append(c4)
    noof.append(c5)
    pos=np.arange(5)    
    columns=[1,2,3,4,5]
    colors=['lightslategray','dimgray','silver','gainsboro','lightgrey']
    plt.figure(figsize=(15,10))
    plt.bar(pos,noof,color=colors,width=0.6)
    plt.xticks(pos,columns)
    plt.xlabel('Rating',color='black',size=20)
    plt.xticks(size=13,color='saddlebrown')
    plt.yticks(size=13,color='black')
    plt.ylabel('Number of customers', color='black',size=20)
    plt.title("Quality of the products",fontdict=font2)
    plt.show()


def price_fuc():
    font2= {'family': 'Franklin Gothic Medium',
            'color':'saddlebrown',
            'weight':'bold',
            'size': 30
         }
  
    
    c1= dataset[dataset['Q4'] == 1].shape[0]
    c2 = dataset[dataset['Q4'] == 2].shape[0]
    c3= dataset[dataset['Q4'] == 3].shape[0]
    c4= dataset[dataset['Q4'] == 4].shape[0]
    c5= dataset[dataset['Q4'] == 5].shape[0]
    
    noof=[]
    noof.append(c1)
    noof.append(c2)
    noof.append(c3)
    noof.append(c4)
    noof.append(c5)
    pos=np.arange(5)    
    columns=[1,2,3,4,5]
    colors=['gold','khaki','goldenrod','y','darkgoldenrod']
    plt.figure(figsize=(15,10))
    plt.bar(pos,noof,color=colors,width=0.6)
    plt.xticks(pos,columns)
    plt.xlabel('Rating',color='saddlebrown',size=20)
    plt.xticks(size=13,color='saddlebrown')
    plt.yticks(size=13,color='saddlebrown')
    plt.ylabel('Number of customers', color='saddlebrown',size=20)
    plt.title("Number of customer who found price of products reasonable",fontdict=font2)
    plt.show()

def recommend():
    font2= {'family': 'Franklin Gothic Medium',
            'color':'darkgreen',
            'weight':'bold',
            'size': 30
        }
    
    c1= dataset[dataset['Q5'] == 1].shape[0]
    c2 = dataset[dataset['Q5'] == 2].shape[0]
    c3= dataset[dataset['Q5'] == 3].shape[0]
    c4= dataset[dataset['Q5'] == 4].shape[0]
    c5= dataset[dataset['Q5'] == 5].shape[0]
    
    noof=[]
    noof.append(c1)
    noof.append(c2)
    noof.append(c3)
    noof.append(c4)
    noof.append(c5)
    pos=np.arange(5)    
    columns=[1,2,3,4,5]
    colors=['forestgreen','seagreen','green','limegreen','darkolivegreen']
    plt.figure(figsize=(15,10))
    plt.bar(pos,noof,color=colors,width=0.6)
    plt.xticks(pos,columns)
    plt.xticks(size=13,color='darkgreen')
    plt.yticks(size=13,color='darkgreen')
    plt.xlabel('Rating',color='darkgreen',size=20)
    plt.ylabel('Number of customers', color='darkgreen',size=20)
    plt.title("Number of customer who are likely to recommend this store to others",fontdict=font2)
    plt.show()

def overall():
    font2= {'family': 'Franklin Gothic Medium',
            'color':'black',
            'weight':'bold',
            'size': 30
        }
    c1=dataset["Q1"].mean()
    c2=dataset["Q2"].mean()
    c3=dataset["Q3"].mean()
    c4=dataset["Q4"].mean()
    c5=dataset["Q5"].mean()
    
    noof=[]
    noof.append(c1)
    noof.append(c2)
    noof.append(c3)
    noof.append(c4)
    noof.append(c5)
    pos=np.arange(5) 
    
    columns=[1,2,3,4,5]
    colors=['lightcoral','lightblue','lightslategrey','yellow','lightgreen']
    plt.figure(figsize=(15,10))
    plt.pie(noof,labels=columns,autopct='%1.1f%%',colors=colors,explode=[0,0,.1,0,0])
    plt.title("Overall Analysis",fontdict=font2)
    plt.show()


root= tk.Tk()
root.title("Performance analysis")
root.geometry("490x200")
global label,label_font,label_texts,id,password,password_field 
label_font= tkFont.Font(root,family='Helvetica',size=25, weight='bold')
entry_font= tkFont.Font(root,family='Helvetica',size=15)

label=tk.Label(root, text="         Enter details to log in ",font=label_font)
label_texts= tkFont.Font(root,family='Helvetica',size=15, weight='bold')

id=tk.Label(root, text="ID ",font= label_texts)
password=tk.Label(root, text="Password ", font=label_texts)

id_field=Entry(root,font=entry_font)
password_field=Entry(root,show="*",font=entry_font)

label.grid(row=1,pady=10)

id.grid(row=2, column=0, sticky = 'W',padx=(50,0)) 
password.grid(row=3, column=0, sticky = 'W',ipadx=20)

id_field.grid(row=2, column=0,pady=(3,3),padx=(125,0),ipadx=50) 
password_field.grid(row=3, column=0,pady=(3,3),padx=(125,0),ipadx=50) 


photo = PhotoImage(file ="okbutton1.png") 


button=Button(root, image = photo,command=check,width=100,height=50)
button.grid(row=5,pady=5)
root.mainloop()
