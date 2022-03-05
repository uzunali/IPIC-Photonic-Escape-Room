# -*- encoding: utf-8 -*-
'''
@Author  :   Ali Uzun 
@Time    :   2022/02/27 20:52:35
@Version :   1.0
'''

# here put the import lib

from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
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
        self.passcode_status = None
        self.message = []
        self.initial_message = " ENTER YOUR CODE! "

        self.test = 0


        self.Widgest()
        self.frame.pack(fill=BOTH, expand=True)
    
    def Widgest(self):

        #self.top_label = Label(self.frame,text=" PROJECT FIBER STORM ", fg="black", font=("Times",34))
        #self.top_label.grid(row=0, column=0, columnspan=4, sticky=EW)

        #self.top_label2 = Label(self.frame,text=" FAILSAFE ", fg="black", font=("Times",24))
        #self.top_label2.grid(row=0, column=0, columnspan=8, sticky=EW)
        #self.frame.pack(fill=BOTH, expand=True)

        # IPIC logo
        image = ImageTk.PhotoImage(Image.open("logo/ipic.png"))       
        label = ttk.Label(self.frame, image=image, width=20 )
        label.photo = image   # assign to class variable to resolve problem with bug in `PhotoImage`

        label.grid(row=0, column=1, columnspan=8,rowspan=1,padx=(40, 0), sticky=EW)

        self.Ebox()

        message = Label(self.frame,text = self.initial_message,fg="black",bd = 5,font=("Times",16))
        #message = Label(self.frame,text=" ",fg="black",bd = 5,font=("Times",16))

        message.grid(row=4, column=2, columnspan=4,sticky=EW)
        message.config({"background": "White"})

        add = Button(self.frame,text= "STOP UPLOAD",font=("Times",18, BOLD),fg="blue",bd = 5, height= 3, width=10, command=self.Enter)
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
        row_index=2
        col_index=1
        initial_text = "D%d"%col_index
        E1 = Entry(self.frame,font = "Helvetica %d bold"%self.font_size, justify="center", bd = 5, width=self.box_width)
        E1.insert(-1, initial_text)
        E1.grid(row=row_index,
            column=col_index,
            #padx=5,
            padx=(60, 0),
            pady=0,
            ipady=10,
            sticky=EW)
        E1.bind("<Button-1>", self.on_click1)
        #E1.config({"background": "Red"})

        col_index=2
        initial_text = "D%d"%col_index
        E2 = Entry(self.frame,font = "Helvetica %d bold"%self.font_size, justify="center", bd = 5, width=self.box_width)
        E2.insert(-1, initial_text)
        E2.grid(row=row_index,
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
        E3.grid(row=row_index,
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
        E4.grid(row=row_index,
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
        E5.grid(row=row_index,
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
        E6.grid(row=row_index,
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

        self.passcode_status = None
        self.check_cells()
        self.Passcode_Check()
        self.Update_Box()
        print("Passcode is %d "%self.passcode_status)
        self.passcode_status = None

    def Reset(self):
        self.passcode_checklist={"D1":None,"D2":None,"D3":None,"D4":None,"D5":None,"D6":None}
        initial_text ="D%d"
        for i,e in enumerate(self.entry_list):
            e.delete(0, 'end')
            e.config({"background": "White"})
            s = e.insert(-1, initial_text%(i+1))
            #print(s)
        #self.message.config({"background": "White"})
        self.passcode_status = None
        #try:
        self.message[0].destroy()
        message = Label(self.frame,text = self.initial_message,fg="black",bd = 5,font=("Times",16))
        #message = Label(self.frame,text=" ",fg="black",bd = 5,font=("Times",16))
        message.grid(row=4, column=2, columnspan=4,sticky=EW)
        message.config({"background": "White"})
        #message.destroy()
        print("Reset Done")
        #except:
        #    pass
        
    
    def Passcode_Check(self):
        for i in range(len(self.passcode)):
            key = "D%d"%(i+1)
            if(self.passcode[i] == self.user_code[i]):
                self.passcode_checklist[key] = 1
            else:
                self.passcode_checklist[key] = 0
            
            
    
    def check_cells(self):
        for i,e in enumerate(self.entry_list):
            s = e.get()
            if(not s.isnumeric()):
                self.passcode_status = 3
        if(self.passcode_status != 3):
            try:
                if(sum(self.passcode_checklist.values()) == 6):
                    self.passcode_status = 1
                else:
                    self.passcode_status = 2
            except:
                pass
                

    
    def Update_Box(self):
        #self.passcode_status = False
        for i,e in enumerate(self.entry_list):
            key = "D%d"%(i+1)
            if(self.passcode_status in [1, 2]):
                if(self.passcode_checklist[key] == 0):
                    e.config({"background": "Red"})
                else:
                    e.config({"background": "Green"})

            #self.Warning_Window()
        self.check_cells()
        if (self.passcode_status != None):
            if(self.passcode_status == 1):
                message = Label(self.frame,text=" UPLOAD of WiVirus HAS TERMINATED ",fg="black",bd = 5,font=("Times",16))
                message.grid(row=4, column=2, columnspan=4,sticky=EW)
                message.config({"background": "Green"})

            elif(self.passcode_status == 2):
                message = Label(self.frame,text=" CODE in RED BOX IS NOT CORRECT !! ",fg="black",bd = 5,font=("Times",16))
                message.grid(row=4, column=2, columnspan=4,sticky=EW)
                message.config({"background": "Red"})

            elif(self.passcode_status == 3):
                message = Label(self.frame,text=" PLEASE ENTER a NUMBER IN EACH CELL ",fg="black",bd = 5,font=("Times",16))
                message.grid(row=4, column=2, columnspan=4,sticky=EW)
                message.config({"background": "Pink"})
            self.message = [message]
        #self.passcode_status = 0 # set it back to 0

        
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
    root.geometry("820x500")
    root.resizable(width=True, height=True)
    app = Photonics_Escape_Room(root)
    root.mainloop()

if __name__ == '__main__':
    main()