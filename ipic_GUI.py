from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class Photonics_Escape_Room():
    def __init__(self,root) -> None:
        self.root = root
        self.frame = Frame(self.root)

        self.box_width = 3
        self.font_size = 30
        self.entry_list = [] 
        self.passcode = "281820"
        self.user_code = []
        self.passcode_checklist = {"D1":None,"D2":None,"D3":None,"D4":None,"D5":None,"D6":None}
        self.passcode_status = False
        self.message = []



        self.Widgest()
    
    def Widgest(self):

        self.top_label = Label(self.frame,text=" PHOTONIC ESCAPE ROOM ", fg="black", font=("Times",40))
        self.top_label.grid(row=0, column=0, columnspan=8, sticky=EW)
        self.frame.pack(fill=BOTH, expand=True)

        # IPIC logo
        image = ImageTk.PhotoImage(Image.open("IPIC/ipic.png"))       
        label = ttk.Label(self.frame, image=image, width=50 )
        label.photo = image   # assign to class variable to resolve problem with bug in `PhotoImage`

        label.grid(row=1, column=0, columnspan=4,sticky=EW)

        #Tyndall Logo
        image = ImageTk.PhotoImage(Image.open("IPIC/tyndall.png"))
        label = ttk.Label(self.frame, image=image, width=50 )
        #label.config(width=40)
        label.photo = image   # assign to class variable to resolve problem with bug in `PhotoImage`

        label.grid(row=1, column=4, columnspan=4,sticky=EW)

        self.Ebox()

        add = Button(self.frame,text= "ENTER",font=("Times",13),fg="blue",bd = 5, height= 4, width=10, command=self.Enter)
        add.grid(row=3,column=3,columnspan=2,sticky=EW)
        add.bind("<Return>", self.Enter)

        reset = Button(self.frame,text= "RESET",font=("Times",13),fg="blue", height= 2, width=5, command=self.Reset)
        reset.grid(row=5,column=2,columnspan=2,sticky=EW)
        reset.bind("<Return>", self.Enter)

        quit = Button(self.frame,text= "QUIT",font=("Times",13),fg="blue", height= 2, width=5, command=self.root.destroy)
        quit.grid(row=5,column=4,columnspan=2,sticky=EW)
        #quit.bind("<Return>", self.Enter)


        #wrong_label = Label(self.frame,text=" PASSWORD IS NOT CORRECT ",fg="black",bd = 5,font=("Times",16))
        #wrong_label.grid(row=4, column=2, columnspan=4,sticky=EW)

    
    def Ebox(self):
        col_index=1
        initial_text = "D%d"%col_index
        E1 = Entry(self.frame,font = "Helvetica %d bold"%self.font_size, justify="center", bd = 5, width=self.box_width)
        E1.insert(-1, initial_text)
        E1.grid(row=2,
            column=col_index,
            padx=5,
            pady=0,
            ipady=10,
            sticky=EW)
        E1.bind("<Button-1>", self.on_click1)
        #E1.config({"background": "Red"})

        col_index=2
        initial_text = "D%d"%col_index
        E2 = Entry(self.frame,font = "Helvetica %d bold"%self.font_size, justify="center", bd = 5, width=self.box_width)
        E2.insert(-1, initial_text)
        E2.grid(row=2,
            column=col_index,
            padx=5,
            pady=0,
            ipady=10,
            sticky=EW)
        E2.bind("<Button-1>", self.on_click2)

        col_index=3
        initial_text = "D%d"%col_index
        E3 = Entry(self.frame,font = "Helvetica %d bold"%self.font_size, justify="center", bd = 5, width=self.box_width)
        E3.insert(-1, initial_text)
        E3.grid(row=2,
            column=col_index,
            padx=5,
            pady=0,
            ipady=10,
            sticky=EW)
        E3.bind("<Button-1>", self.on_click3)

        col_index=4
        initial_text = "D%d"%col_index
        E4 = Entry(self.frame,font = "Helvetica %d bold"%self.font_size, justify="center", bd = 5, width=self.box_width)
        E4.insert(-1, initial_text)
        E4.grid(row=2,
            column=col_index,
            padx=5,
            pady=0,
            ipady=10,
            sticky=EW)
        E4.bind("<Button-1>", self.on_click4)
        
        col_index=5
        initial_text = "D%d"%col_index
        E5 = Entry(self.frame,font = "Helvetica %d bold"%self.font_size, justify="center", bd = 5, width=self.box_width)
        E5.insert(-1, initial_text)
        E5.grid(row=2,
            column=col_index,
            padx=5,
            pady=0,
            ipady=10,
            sticky=EW)
        E5.bind("<Button-1>", self.on_click5)

        col_index=6
        initial_text = "D%d"%col_index
        E6 = Entry(self.frame,font = "Helvetica %d bold"%self.font_size, justify="center", bd = 5, width=self.box_width)
        E6.insert(-1, initial_text)
        E6.grid(row=2,
            column=col_index,
            padx=5,
            pady=0,
            ipady=10,
            sticky=EW)
        E6.bind("<Button-1>", self.on_click6)

        self.entry_list= [E1,E2,E3,E4,E5,E6] 
    

    def Enter(self):
        self.passcode_check={"D1":None,"D2":None,"D3":None,"D4":None,"D5":None,"D6":None}
        self.user_code=[]
        for i,e in enumerate(self.entry_list):
            s = e.get()
            self.user_code.append(s)
            print(s)
        self.Passcode_Check()
        self.Update_Box()

    def Reset(self):
        self.passcode_checklist={"D1":None,"D2":None,"D3":None,"D4":None,"D5":None,"D6":None}
        initial_text ="D%d"
        for i,e in enumerate(self.entry_list):
            e.delete(0, 'end')
            e.config({"background": "White"})
            s = e.insert(-1, initial_text%(i+1))
            print(s)
        #self.message.config({"background": "White"})
        try:
            self.message[0].destroy()
        except:
            pass
        
    
    def Passcode_Check(self):
        for i in range(len(self.passcode)):
            key = "D%d"%(i+1)
            if(self.passcode[i]==self.user_code[i]):
                self.passcode_checklist[key] = 1
            else:
                self.passcode_checklist[key] = 0
    
    def Update_Box(self):
        self.passcode_status = False
        for i,e in enumerate(self.entry_list):
            key = "D%d"%(i+1)
            if(self.passcode_checklist[key] == 0):
                e.config({"background": "Red"})
            else:
                e.config({"background": "Green"})
        try:
            if(sum(self.passcode_checklist.values()) == 6):
                self.passcode_status = True
        except:
            self.passcode_status = False
            self.Warning_Window()

        if(self.passcode_status):
            message = Label(self.frame,text=" UPLOAD of WiVirus HAS TERMINATED ",fg="black",bd = 5,font=("Times",16))
            message.grid(row=4, column=2, columnspan=4,sticky=EW)
            message.config({"background": "Green"})

        else:
            message = Label(self.frame,text=" CODE in RED COLORED BOX IS NOT CORRECT !! ",fg="black",bd = 5,font=("Times",16))
            message.grid(row=4, column=2, columnspan=4,sticky=EW)
            message.config({"background": "Red"})
        self.message = [message]

        
    def Warning_Window(self):
        #Create a Button to Open the Toplevel Window
        top= Toplevel(self.root)
        top.geometry("700x250")
        top.title("Child Window")
        #Create a label in Toplevel window
        Label(top, text= "Please Enter a number in each cell!")

    def on_click1(self,event):
        e_index = 0
        self.entry_list[e_index].delete(0, 'end')

    def on_click2(self,event):
        e_index = 1
        self.entry_list[e_index].delete(0, 'end')

    def on_click3(self,event):
        e_index = 2
        self.entry_list[e_index].delete(0, 'end')

    def on_click4(self,event):
        e_index = 3
        self.entry_list[e_index].delete(0, 'end')

    def on_click5(self,event):
        e_index = 4
        self.entry_list[e_index].delete(0, 'end')

    def on_click6(self,event):
        e_index = 5
        self.entry_list[e_index].delete(0, 'end')
    

        
        


def main():
    root = Tk()
    root.title(string='Photonic Escape Room')
    root.geometry("600x500")
    root.resizable(width=False, height=False)
    app = Photonics_Escape_Room(root)
    root.mainloop()

if __name__ == '__main__':
    main()