from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser
from tkinter import filedialog, messagebox
from PIL import ImageGrab   #form pillow package


class paint(object):
    DEFAULT_PEN_SIZE = 10.0
    
    def __init__(self):
        self.root= Tk()
        self.root.title("My Paint")
        self.root.geometry("800x500")
        self.size=Canvas(self.root, width=800, height=500)
        self.root.configure(bg="white")

        self.pen_color="black"
        self.eraser_color="white"
        
        
        self.color_frame=LabelFrame(self.root, text="Color", font=('arial', 15, 'bold'), bd=5, relief=RIDGE, bg="#6FA5F5")
        self.color_frame.place(x=10, y=400, width=240, height=90)

        colors=['white', 'black', 'brown','red', 'orange','yellow','green', 'blue', '#3E1C91', '#F20A85']
        i=j=0
        for color in colors:                                                            #col is value of color
            Button(self.color_frame, bg=color, bd=2, relief=RIDGE, width=5, command=lambda col= color: self.select_color(col)).grid(row=i, column=j)
            j+=1
            if j==5:
                j=0
                i=1

        self.edit_color_button=Button(self.root, text="Edit Color",font=('arial', 11, 'bold'), bd=3, bg="#6FA5F5", command=self.edit_color, width=12,height=2, relief=RIDGE)
        self.edit_color_button.place(x=255, y=400)

        self.eraser_button=Button(self.root, text="Eraser",font=('arial', 11, 'bold'), bd=3, bg="#6FA5F5", command=self.eraser, width=12,height=2, relief=RIDGE)
        self.eraser_button.place(x=255, y=445)

        self.clear_button=Button(self.root, text="Clear",font=('arial', 11, 'bold'), bd=3, bg="#6FA5F5", command=lambda : self.canvas.delete("all"), width=12,height=2, relief=RIDGE)
        self.clear_button.place(x=355, y=400)

        self.save_button=Button(self.root, text="Save",font=('arial', 11, 'bold'), bd=3, bg="#6FA5F5", command=self.save_paint, width=12,height=2, relief=RIDGE)
        self.save_button.place(x=355, y=445)

        

        self.pen_size_scale_frame=LabelFrame(self.root, text="size", bd=5, bg="#6FA5F5", font=('areal',15,'bold'), relief=RIDGE)
        self.pen_size_scale_frame.place(x=480, y=400, height=70, width=250)

        self.pen_size=Scale(self.pen_size_scale_frame, orient=HORIZONTAL, from_=0, to=50, length=220)
        self.pen_size.set(1)
        self.pen_size.grid(row=0, column=1, padx=15)

        self.canvas=Canvas(self.root, bg='white', bd=5, relief=GROOVE, height=380, width=787)
        self.canvas.place(x=0, y=0)

        #self.setup()
        self.canvas.bind('<B1-Motion>', self.paint)
        

        self.root.mainloop()

        
        #dragging of mouse
    def paint(self, event):
        x1, y1=(event.x-2), (event.y-2)
        x2, y2=(event.x+2),(event.y+2)

        self.canvas.create_oval(x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color, width=self.pen_size.get())
        
        
    def select_color(self, col):
        self.pen_color=col

    def eraser(self):
        self.pen_color=self.eraser_color

    def edit_color(self):
        color=colorchooser.askcolor()
        self.pen_color=color[1]

    def save_paint(self):
        try:
            #self.canvas.update()
            filename = filedialog.asksaveasfilename(defaultextension='.jpg')
            #print(filename)
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            #print(x, self.canvas.winfo_x())
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            #print(y)
            x1 = x + self.canvas.winfo_width()
            #print(x1)
            y1 = y + self.canvas.winfo_height()
            #print(y1)
            ImageGrab.grab().crop(x, y, x1, y1).save(filename)
            messagebox.showinfo('paint says image is saved as ', + str(filename))
            
        except:
            messagebox.showerror("paint says", "unable to save image, \n something went wrong")


if __name__=='__main__':
    paint()
    
