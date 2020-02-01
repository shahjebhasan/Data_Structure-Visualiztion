from tkinter import *
from PIL import Image, ImageTk
import os
tk=Tk()
tk.config(bg='gray')
label=Label(tk,text='Data Structure Visualization',font=('arial',30,'bold'),fg='white',bg='gray',padx=40,pady=40)
label.pack()
frame1=Frame(tk,width=1080,height=620,relief=SUNKEN,bg='ivory3')
frame1.pack()
label2=Label(frame1,font=('arial',25,'bold'),text='To Observe the Tree Representation click on the TREE butoon :-',bg='ivory3')
label2.grid(row=0,column=0)
btn1=Button(frame1,text='TREE',font=('arial',20,'bold'),padx=100,pady=10,bg='thistle3',fg='black',justify='right',bd=5,command=lambda:os.system('python Tree.py'))
btn1.grid(row=1,column=0)

label3=Label(frame1,font=('arial',25,'bold'),text='To Observe the Stack Representation click on the STACK butoon :-',bg='ivory3')
label3.grid(row=3,column=0)
btn2=Button(frame1,text='STACK',font=('arial',20,'bold'),padx=100,pady=10,bg='thistle3',fg='black',justify='right',bd=5,command=lambda:os.system('python stack.py'))
btn2.grid(row=4,column=0)

label4=Label(frame1,font=('arial',25,'bold'),text='To Observe the Queue Representation click on the QUEUE butoon :-',bg='ivory3')
label4.grid(row=6,column=0)
btn3=Button(frame1,text='QUEUE',font=('arial',20,'bold'),padx=100,pady=10,bg='thistle3',fg='black',justify='right',bd=5,command=lambda:os.system('python queue.py'))
btn3.grid(row=7,column=0)


tk.mainloop()