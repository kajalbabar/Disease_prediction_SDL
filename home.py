#import library
from tkinter import *
import tkinter
from tkinter import messagebox
import os


root = Tk()     #root object
root.title("Diseases Prediction and analysis")
title=tkinter.Label(root,text="Disease Analysis",bg="#F44336",fg="white",font=("arrial",32,"bold"))
title.pack(fill=BOTH,pady=2,padx=1)

title1=tkinter.Label(root,text="",bg="white",fg="royalblue",font=("arrial",32,"bold"))
title1.pack(fill=BOTH,pady=2,padx=0)

photo = PhotoImage(file = "bg.jpg")
root.geometry("900x600+200+10")
w = Label(root, image=photo)
w.pack()

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def fun1():
    #os.system('Code1.py')
    import Code1
def fun2():
    #os.system('graph.py')
    import graph

def callInfo():
    msg = "Algorithm Used: Decision Tree Classification\nAccuracy for prediction: 95 % \n"
    messagebox.showinfo("Information", msg)

B1=tkinter.Button(root,text="About Project",command= callInfo,fg='white',bg='#F44336',font=("arrial",16,"bold"),height=3,width=10)
B1.place(x=40,y=200)
B2=tkinter.Button(root,text="Disease\nPrediction",command= fun1,fg='white',bg='#F44336',font=("arrial",16,"bold"),height=3,width=10)
B4=tkinter.Button(root,text="Analysis \nof Hepatitis",command= fun2,fg='white',bg='#F44336',font=("arrial",16,"bold"),height=3,width=10)
B2.place(x=40,y=500)
B4.place(x=1200,y=370)

root.mainloop()


