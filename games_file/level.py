import tkinter as tk
import Chok



class Levelscreen():
    def __init__(self,master):
        self.levelframe=tk.Frame(master,bg='black')
        self.master=master
        self.easy=tk.Label(self.levelframe,text="Easy",width=9,font=("arial",24),fg="black",bg="white")
        self.easy.place(x=900,y=400)
        self.medium=tk.Label(self.levelframe,text="Medium",width=9,font=("arial",24),fg="white",bg="black")
        self.medium.place(x=900,y=480)
        self.hard=tk.Label(self.levelframe,text="Hard",width=9,font=("arial",24),fg="white",bg="black")
        self.hard.place(x=900,y=560)
        self.levelframe.pack(fill='both',expand=True)
        self.levelframe.focus_set()
        self.easy.bind('<1>',self.easyclick)
        self.medium.bind('<1>',self.mediumclick)
        self.hard.bind('<1>',self.hardclick)
        self.levelframe.bind('<Up>',self.levelup)
        self.levelframe.bind('<Down>',self.leveldown)
        self.levelframe.bind('<Return>',self.newframe)
        self.levelframe.mainloop()

    current_player="X"   
    
    def levelup(self,event):
        if self.easy["fg"]=="black":
            self.easy.configure(fg="white",bg="black")
            self.hard.configure(fg="black",bg="white")
        elif self.medium["fg"]=="black":
            self.medium.configure(fg="white",bg="black")
            self.easy.configure(fg="black",bg="white")
        elif self.hard["fg"]=="black":
            self.hard.configure(fg="white",bg="black")
            self.medium.configure(fg="black",bg="white")
        


    def leveldown(self,event):
        if self.easy["fg"]=="black":
            self.easy.configure(fg="white",bg="black")
            self.medium.configure(fg="black",bg="white")
        elif self.medium["fg"]=="black":
            self.medium.configure(fg="white",bg="black")
            self.hard.configure(fg="black",bg="white")
        elif self.hard["fg"]=="black":
            self.hard.configure(fg="white",bg="black")
            self.easy.configure(fg="black",bg="white")
            
    def easyclick(self,event):
        if self.easy["fg"]=="white":
            self.easy.configure(fg="black",bg="white")
            
    def mediumclick(self,event):
        if self.medium["fg"]=="white":
            self.medium.configure(fg="black",bg="white")
            
    def hardclick(self,event):
        if self.hard["fg"]=="white":
            self.hard.configure(fg="black",bg="white")

    def newframe(self,event):
        self.easy.destroy()
        self.medium.destroy()
        self.hard.destroy()
        self.levelframe.destroy()
        self.bf=tk.Frame(self.master,bg="yellow")
        self.bf.pack(anchor="n")
        b=Chok.Board(self.bf)
        b.newboard()

   





