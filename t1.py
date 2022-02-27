from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()
root.geometry("800x500")
frame1 = Frame(root)
frame1.pack(side=TOP,fill=X)
   
canvas = Canvas(frame1, width = 300, height = 200)  
canvas.pack(side=LEFT,fill='both', expand='yes')

#canvas.grid(column=0, row=0, columnspan=3)
img1 = ImageTk.PhotoImage(Image.open("IPIC/ipic.png"))  
canvas.create_image(20, 20, anchor=NW, image=img1) 

frame2 = Frame(root) 
frame2.pack(side=TOP,fill=X)

canvas = Canvas(frame2, width = 300, height = 200)  
canvas.pack(side=RIGHT,fill='both', expand='yes')

img2 = ImageTk.PhotoImage(Image.open("IPIC/tyndall.png"))  
canvas.create_image(20, 20, anchor=NW, image=img2)
#canvas.grid(column=1, row=0)
 

root.mainloop()