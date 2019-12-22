#import module from tkinter for UI
from tkinter import *

import os

#creating instance of TK
root=Tk()

root.configure(background="#80D8FF")

#root.geometry("600x600")

def function1():
    
    os.system("python D:/testProject/final_project/dataSetCreator.py")
    os.system("python D:/testProject/final_project/train.py")
    
def function2():
    
    os.system("python D:/testProject/final_project/testImageCreater.py")

def function3():

    os.system("python D:/testProject/final_project/face_recognition_knn.py")

#stting title for the window
root.title("AUTOMATIC ATTENDANCE SYSTEM USING FACE RECOGNITION")

#creating a text label
Label(root, text="SELECT YOUR OPTION",font=("helvatica",40),fg="white",bg="#00BFA5",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating a button
Button(root,text="Update Database",font=("times new roman",30),bg="#3F51B5",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Take Test Images",font=("times new roman",30),bg="#3F51B5",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)




#third button
Button(root,text="Recognizer",font=("times new roman",30),bg="#3F51B5",fg='white',command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)





Button(root,text="CLEAR",font=("times new roman",30), fg="white",bg="#3F51B5",command=root.quit).grid(row=6,columnspan=2, pady=5,padx=5,sticky=E+W+N+S)
#creating third button
#Button(root,text="COMPARE",font=('times new roman',30),bg="#3F51B5",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
