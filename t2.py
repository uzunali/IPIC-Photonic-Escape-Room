from tkinter import *  
from PIL import ImageTk,Image 

root = Tk()
root.geometry("800x500")
frame1 = Frame(root)
frame1.pack(side=TOP,fill=X)
 
my_canvas=Canvas(frame1,width=400,height=200,bd=0)
bg = ImageTk.PhotoImage(Image.open("IPIC/ipic.png"))  

my_canvas.create_image(20,20,anchor=NW,image=bg)
my_canvas.pack(fill="both",expand=True)            
originallbl = Label(my_canvas, text="Original", width=15).grid(row=2,column=1)
original = Entry(my_canvas, width=15).grid(row=2,column=2)
 

root.mainloop()