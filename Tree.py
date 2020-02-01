from tkinter import *
from PIL import Image,ImageTk
tk=Tk()
canvas = Canvas(tk, width=1080, height=620,bg='firebrick1',relief=RIDGE)
canvas.pack()
root_pos=(510, 5, 540, 40)
class NewNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.posn=root_pos
    def pos(self, root_posn, lr):
        if lr=='l':
            self.posn=tuple((root_posn[0]-50,root_posn[1]+50, root_posn[2]-50, root_posn[3]+50))
            self.img = canvas.create_oval(self.posn, fill='white')
        elif lr =='r':
            self.posn=tuple((root_posn[0]+50,root_posn[1]+50, root_posn[2]+50, root_posn[3]+50))
            self.img = canvas.create_oval(self.posn, fill='white')
        else:
            self.img = canvas.create_oval(self.posn, fill='white')
        x0=self.posn[0]+18
        y0=self.posn[1]+18
        self.txt = canvas.create_text(x0, y0, text=self.data)
        
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=NewNode(data)
                    self.left.pos(self.posn, 'l')
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=NewNode(data)
                    self.right.pos(self.posn, 'r')
                else:
                    self.right.insert(data)
        else:
            self.data=data
        tk.update()
            
    def findval(self,searchval):
        if searchval<self.data:
            if self.left is None:
                return (str(searchval)  + " Not Found")
            return self.left.findval(searchval)
        elif searchval>self.data:
            if self.right is None:
                return (str(searchval) + " Not found")
            return self.right.findval(searchval)
        else:
            print(str(self.data) + ' is found')
            
    def MinValueNode(self,node):
        current=node
        while(current.left is not None):
            current=current.left
        return current
    
    def delete_node(self,data):
        if not self:
            return None
        
        if data<self.data:
            self.left=self.left.delete_node(data)
        elif data>self.data:
            self.right=self.right.delete_node(data)
        else:
            if self.left is None:
                temp=self.right
                self=None
                return temp
            elif self.right is None:
                temp=self.right
                self=None
                return temp
            
            temp=self.MinValueNode(self.right)
            self.data=temp.data
            self.right=self.right.delete_node(temp.data)
        return self
    
def preorder(node):
    if not node:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)
    return

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)
    return

def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)
    return

if __name__=='__main__':        
    root=NewNode(20)
    root.pos(root_pos, 'n')
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(8)
    root.insert(10)
    root.insert(21)
    root.insert(34)
    root.insert(24)
    root.insert(31)
    root.insert(9)
    root.insert(29)
    root.insert(15)
    root.insert(40)

label=Label(tk,bg='firebrick1',fg='white',text='B-Tree Pictorial Representation',font=('arial',20,'bold'))
label.pack()

tk.mainloop()