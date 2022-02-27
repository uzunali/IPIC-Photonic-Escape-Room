from tkinter import *
from tkinter import ttk

from PIL import ImageTk,Image  

root = Tk()
root.title(string='Photonic Escape Room')
root.geometry("600x500")
root.resizable(width=False, height=False)


frame1 = Frame(root)
#frame1.grid(row=0, column=0)

top_label = Label(frame1,text=" PHOTONIC ESCAPE ROOM ",fg="black",font=("Times",40))
top_label.grid(row=0, column=0, columnspan=8,sticky=EW)

image = ImageTk.PhotoImage(Image.open("logo/ipic.png"))
        
label = ttk.Label(frame1,image=image,width=50)
label.photo = image   # assign to class variable to resolve problem with bug in `PhotoImage`

label.grid(row=1, column=0, columnspan=4,sticky=E)


image = ImageTk.PhotoImage(Image.open("logo/tyndall.png"))
        
label = ttk.Label(frame1,image=image,width=50 )
#label.config(width=40)
label.photo = image   # assign to class variable to resolve problem with bug in `PhotoImage`

label.grid(row=1, column=4, columnspan=4,sticky=W)

def on_click1(event):
    E1.delete(0, 'end')

def on_click2(event):
    E2.delete(0, 'end')

def on_click3(event):
    E3.delete(0, 'end')

def on_click4(event):
    E4.delete(0, 'end')

def on_click5(event):
    E5.delete(0, 'end')

def on_click6(event):
    E6.delete(0, 'end')


box_width = 3
font_size = 30
initial_text ="D%s"
col_index=1

E1 = Entry(frame1,font = "Helvetica %d bold"%font_size, justify="center",text=initial_text, bd = 5, width=box_width)
E1.insert(-1, initial_text%col_index)
E1.grid(row=2,
    column=col_index,
    padx=5,
    pady=0,
    ipady=10,
    sticky=EW)
E1.bind("<Button-1>", on_click1)


col_index=2
E2 = Entry(frame1,font = "Helvetica %d bold"%font_size, justify="center", bd = 5, width=box_width)
E2.insert(-1, initial_text%col_index)
E2.grid(row=2,
    column=col_index,
    padx=5,
    pady=0,
    ipady=10,
    sticky=EW)
E2.bind("<Button-1>", on_click2)

col_index=3
E3 = Entry(frame1,font = "Helvetica %d bold"%font_size, justify="center", bd = 5, width=box_width)
E3.insert(-1, initial_text%col_index)
E3.grid(row=2,
    column=col_index,
    padx=5,
    pady=0,
    ipady=10,
    sticky=EW)
E3.bind("<Button-1>", on_click3)

col_index=4
E4 = Entry(frame1,font = "Helvetica %d bold"%font_size, justify="center", bd = 5, width=box_width)
E4.insert(-1, initial_text%col_index)
E4.grid(row=2,
    column=col_index,
    padx=5,
    pady=0,
    ipady=10,
    sticky=EW)
E4.bind("<Button-1>", on_click4)

col_index=5
E5 = Entry(frame1,font = "Helvetica %d bold"%font_size, justify="center", bd = 5, width=box_width)
E5.insert(-1, initial_text%col_index)
E5.grid(row=2,
    column=col_index,
    padx=5,
    pady=0,
    ipady=10,
    sticky=EW)
E5.bind("<Button-1>", on_click5)

col_index=6
E6 = Entry(frame1,font = "Helvetica %d bold"%font_size, justify="center", bd = 5, width=box_width)
E6.insert(-1, initial_text%col_index)
E6.grid(row=2,
    column=col_index,
    padx=5,
    pady=0,
    ipady=10,
    sticky=EW)
E6.bind("<Button-1>", on_click6)

entry_list = [E1,E2,E3,E4,E5,E6] 

def Enter():
    for i,e in enumerate(entry_list):
        s = e.get()
        print(s)

def Reset():
    initial_text ="D%d"
    for i,e in enumerate(entry_list):
        e.delete(0, 'end')
        s = e.insert(-1, initial_text%(i+1))
        print(s)

add=Button(frame1,text= "ENTER",font=("Times",13),fg="blue",bd = 5, height= 4, width=10, command=Enter)
add.grid(row=3,column=3,columnspan=2,sticky=EW)
add.bind("<Return>", Enter)

add=Button(frame1,text= "RESET",font=("Times",13),fg="blue", height= 2, width=5, command=Reset)
add.grid(row=5,column=3,columnspan=2,sticky=EW)
add.bind("<Return>", Enter)

wrong_label = Label(frame1,text=" PASSWORD IS NOT CORRECT ",fg="black",bd = 5,font=("Times",16))
wrong_label.grid(row=4, column=0, columnspan=4,sticky=EW)

correct_label = Label(frame1,text=" UPLOAD of WiVirus HAS STOPED ",fg="black",font=("Times",16))
correct_label.grid(row=4, column=4, columnspan=4,sticky=EW)

password = [12,4,1,0,6,8]

frame1.pack(fill=BOTH,expand=True)



root.mainloop()