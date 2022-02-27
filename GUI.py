from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class Photonics_Escape_Room():

    def __init__(self, master):
        #Frame.__init__(self, master)
        self.parent = master
        self.frame = Frame(self.parent)
        #self.frame.grid(row=0, column=0)
        self.entry_box_list = []

        
        self.Widgets()
        self.Settings()
    
    def Widgets(self):
        # Create an object of tkinter ImageTk
        self.top_label = Label(self.frame,text=" PHOTONIC ESCAPE ROOM ",fg="black",font=("Times",40))
        self.top_label.grid(row=0, column=0, columnspan=8,sticky=EW)


        # IPIC logo
        image = ImageTk.PhotoImage(Image.open("IPIC/ipic.png"))       
        label = ttk.Label(self.frame, image=image, width=50 )
        label.photo = image   # assign to class variable to resolve problem with bug in `PhotoImage`

        label.grid(row=1, column=0, columnspan=4,sticky=E)

        #Tyndall Logo
        image = ImageTk.PhotoImage(Image.open("IPIC/tyndall.png"))
        label = ttk.Label(self.frame, image=image, width=50 )
        #label.config(width=40)
        label.photo = image   # assign to class variable to resolve problem with bug in `PhotoImage`

        label.grid(row=1, column=4, columnspan=4,sticky=W)

        box_width = 3
        font_size = 30
        initial_text ="D%s"

        col_index = 1
        Ebox1 = Entry(self.frame,font = "Helvetica %d bold"%font_size, justify="center",text=initial_text, bd = 5, width=box_width)
        Ebox1.insert(-1, "D1")
        Ebox1.grid(row=2,
            column=col_index,
            padx=5,
            pady=0,
            ipady=10,
            sticky=EW)
        self.entry_box_list.append(Ebox1)
        Ebox1.bind("<Button-1>", self.on_click1)
        print(self.entry_box_list)


        col_index = 2
        self.Ebox2 = Entry(self.frame,font = "Helvetica %d bold"%font_size, justify="center",text=initial_text, bd = 5, width=box_width)
        self.Ebox2.insert(-1, "D2")
        self.Ebox2.grid(row=2,
            column = col_index,
            padx=5,
            pady=0,
            ipady=10,
            sticky=EW)
        self.entry_box_list.append(self.Ebox2)
        #self.Ebox2.bind("<Button-1>", self.on_click2)
        print(self.entry_box_list)



    def Settings(self):
        # placing Frame
        self.frame.pack(fill=BOTH,expand=True)
        #self.frame.grid(row=0, column=0)

    def on_click1(self,event):
        #for e in self.entry_box_list:
        #    e.delete(0, 'end')
        self.entry_box_list[0].delete(0, 'end')
    
    def on_click2(self,event):
        #for e in self.entry_box_list:
        #    e.delete(0, 'end')
        self.Ebox2.delete(0, 'end')
    

    def Enter(self):
        s = E1.get()
        print(s)





def main():
    root = Tk()
    root.title(string='Photonic Escape Room')
    root.geometry("600x400")
    root.resizable(width=False, height=False)
    app = Photonics_Escape_Room(root)
    root.mainloop()

if __name__ == '__main__':
    main()