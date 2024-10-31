
import tkinter as tk
from tkinter import *
import csv
import tkinter.font as tkFont
import tkinter.messagebox as messageBox
from PIL import ImageTk,Image
import time

root= tk.Tk()
root.geometry("840x990")
def clear(): 
      
    # clear the content of text entry box 
    name_field.delete(0, END) 
    email_field.delete(0, END) 
    phoneno_field.delete(0, END) 
    q1_field.delete(0, END) 
    q2_field.delete(0, END) 
    q3_field.delete(0, END) 
    q4_field.delete(0, END) 
    q5_field.delete(0, END) 

def insert(): 
    namefield=name_field.get()
    emailfield=email_field.get()
    phonenumber=phoneno_field.get()
    q1field=q1_field.get()
    q2field=q2_field.get()
    q3field=q3_field.get()
    q4field=q4_field.get()
    q5field=q5_field.get() 

    with open('feedback.csv', 'a', newline="" ) as file:  
       #fieldnames = ['Name', 'Email', 'Phone number','Q1','Q2','Q3','Q4','Q5']  
       #writer = csv.DictWriter(file,fieldnames=fieldnames)  
       writer = csv.writer(file) 
       #writer.writeheader()
       writer.writerow([namefield,emailfield,phonenumber,q1field,q2field,q3field,q4field,q5field])
        
        #writer.writerow({'Name': namefield, 'Email': emailfield, 'Phone number': phonenumber,'Q1':q1field, 'Q2': q2field,'Q3': q3field,'Q4': q4field,'Q5': q5field})
        
    name_field.focus_set()
    clear()
    clearFrame()

def clearFrame():    
    bottomframe.grid_remove()           
    canvas = tk.Canvas(root, width=700, height=400) 
    canvas.grid(row=3)
    img = ImageTk.PhotoImage(Image.open("image.jpg").resize((680, 350)))
    canvas.img=img
    bg = canvas.create_image(0,0, image=img,anchor=tk.NW)
    canvas.after(5000,canvas.destroy)
    bottomframe.grid(row=3)
'''   
def recover():
   
    text2.pack()
    text3.pack()
    q1.pack()
    q1_field.pack()
    q2.pack()
    q2_field.pack()
    q3.pack()
    q3_field.pack()
    q4.pack()
    q4_field.pack()
    q5.pack()
    q5_field.pack()
 '''   
    



     
  
    
topframe=LabelFrame(root,bd=10,background='black',relief=RAISED)
middleframe=LabelFrame(root,bd=10,padx=30,pady=10)
bottomframe=LabelFrame(root, padx=55,pady=15)



label_font_heading= tkFont.Font(topframe,family='Helvetica',size=30, weight='bold')
heading =tk.Label(topframe, text="         WELCOME TO FAB’S CLOTHING       ",font=label_font_heading,background='black',fg='white') 


label_font_rootline= tkFont.Font(topframe,family='Helvetica',size=15,slant='italic')
rootline= tk.Label(topframe, text="                                                           Best service Best business\n ",font = label_font_rootline,background='black',fg='white') 


label_font_text1= tkFont.Font(middleframe,family='Helvetica',size=19)
text1= tk.Label(middleframe, text="\n\nPraise makes you feel good, critics make u better.\nYour opinion matters. Let us know what u feel by giving the survey.\n\n ",font = label_font_text1,justify='left')


label_font_text1= tkFont.Font(middleframe,family='Helvetica',size=15)
name=tk.Label(middleframe, text="Name:",font = label_font_rootline)
email=tk.Label(middleframe, text="E-mail:",font = label_font_rootline)
phoneno=tk.Label(middleframe, text="Phone No:",font = label_font_rootline)

name_field = Entry(middleframe) 
email_field = Entry(middleframe) 
phoneno_field = Entry(middleframe) 

label_font_text2= tkFont.Font(bottomframe,family='Helvetica',size=15)
text2=tk.Label(bottomframe, text="\n\nWe do respect your valuable time pleace take time to rate us on the following.\nIt will take less that 2 minutes.\n",font = label_font_text2,justify= 'left')


label_font_text3= tkFont.Font(bottomframe,family='Helvetica',size=15,slant='italic')
text3=tk.Label(bottomframe, text="Rate out of 5!\n",font = label_font_text3,justify= 'left')
q1_field=Entry(bottomframe)
q2_field=Entry(bottomframe)
q3_field=Entry(bottomframe)
q4_field=Entry(bottomframe)
q5_field=Entry(bottomframe)
q1=tk.Label(bottomframe, text="Did you find the product you were looking for? ",font = label_font_rootline)
q2=tk.Label(bottomframe, text=" Was our staff help full?",font = label_font_rootline)
q3=tk.Label(bottomframe, text=" Did the quality of the product reach your expectations?",font = label_font_rootline)
q4=tk.Label(bottomframe, text="Is the product worth the price? ",font = label_font_rootline)
q5=tk.Label(bottomframe, text="How likely are you to recommend this store to others?",font = label_font_rootline)


topframe.grid(row=0)
middleframe.grid(row=2)
bottomframe.grid(row=3)
heading.grid(row=0) 
rootline.grid(row=1) 
text1.grid(row=2)
name.grid(row=3, column=0, sticky = 'W',padx=(50,0)) 
email.grid(row=4, column=0, sticky = 'W',ipadx=50) 
phoneno.grid(row=5, column=0, sticky = 'W',ipadx=50)
name_field.grid(row=3, column=0,ipadx=100) 
email_field.grid(row=4, column=0,ipadx=100) 
phoneno_field.grid(row=5, column=0,ipadx=100) 
text2.grid(row=6)
text3.grid(row=7)
q1.grid(row=8, column=0,ipadx=100) 
q1_field.grid(row=9,column=0,ipadx=50)
q2.grid(row=10, column=0,ipadx=100) 
q2_field.grid(row=11,column=0,ipadx=50)
q3.grid(row=12, column=0,ipadx=100) 
q3_field.grid(row=13,column=0,ipadx=50)
q4.grid(row=14, column=0,ipadx=100) 
q4_field.grid(row=15,column=0,ipadx=50)
q5.grid(row=16, column=0,ipadx=100) 
q5_field.grid(row=17,column=0,ipadx=50)
 
submit = Button(root, text="SUBMIT", fg="Black", bg="Dark grey",command=insert,width=10,height=2)
 
submit.place(relx=0.5,rely=.95,anchor= CENTER)

root.mainloop()
