from tkinter import *
from PIL import Image,ImageTk
tk=Tk()
canvas = Canvas(tk, width=1080, height=620,bg='firebrick1',relief=SUNKEN)
canvas.pack()
load1 = Image.open('C:\\Users\\DELL\\Desktop\\Data_structure\\fit4.PNG')
img1 = ImageTk.PhotoImage(load1)
root_posn2=(590,195)
class Queue:
    
    def __init__(self):
        self.Queue=list()
        
    def pos2(self, i):
        self.img=canvas.create_image(root_posn2[0]-100*i, root_posn2[1],image=img1,anchor=NW)
    
    def add(self,data):
        if data not in self.Queue:
            self.Queue.insert(0,data)
            self.pos2(len(self.Queue))
            return True
        else:
            return False
    def size(self):
        return(len(self.Queue))

    def remove(self):
        if len(self.Queue)>=0:
            return self.Queue.pop()
        return ("No element in Queue")

if __name__=='__main__':   
     Myqueue=Queue()
     Myqueue.add('87')
     Myqueue.add('23')
     Myqueue.add('44')
     Myqueue.add('36')
     print(Myqueue.remove())

label=Label(tk,bg='firebrick1',fg='white',text='Queue Pictorial Representation',font=('arial',25,'bold'))
label.pack()
tk.mainloop()