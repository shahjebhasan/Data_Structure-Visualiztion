from tkinter import *
from PIL import Image,ImageTk
tk=Tk()
canvas = Canvas(tk, width=1080, height=620,bg='firebrick1',relief=RIDGE)
canvas.pack()
root_posn1=(400,520)
load = Image.open('C:\\Users\\DELL\\Desktop\\Data_structure\\Plate1.PNG')
img = ImageTk.PhotoImage(load)

class stack:
    
    def __init__(self):
        self.stack=[]
        
    def pos1(self, i):
        self.img=canvas.create_image(root_posn1[0], root_posn1[1]-100*i,image=img,anchor=NW)
        
    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            self.pos1(len(self.stack))
            return True
        else:
            return False
        tk.update()
        
    def remove(self):
        if len(self.stack)>=0:
            return(self.stack.pop())
        else:
            return ("No element in the stack")
        
    def peek(self):
        return self.stack[-1]

if __name__=='__main__':
      List=stack()
      List.add('Mon')
      List.add('Tue')
      List.add('wed')
      #print(List.peek())
      List.add(24)
      #print(List.peek())
      #print(List.remove())
label=Label(tk,bg='firebrick1',fg='white',text='Stack Pictorial Representation',font=('arial',20,'bold'))
label.pack()

tk.mainloop()
    