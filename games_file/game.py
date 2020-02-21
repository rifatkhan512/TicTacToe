import tkinter as tk
import turtle as tl
import design
import level
import Chok

class Game():
    
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("1920x1080")
        self.root.title("Rifat's Tic Tac Toe")
        self.root["bg"]="black"
        self.root.resizable(0,0)
        self.root.iconbitmap("tictactoe.ico")
        self.root.state("zoomed")
        self.f=tk.Frame(self.root)
        self.f.pack()
        self.c=tk.Canvas(self.f,height=1080,width=1920,bg="Blue")
        
        self.sc=tl.TurtleScreen(self.c)
        
        self.c.pack()
        self.tt=tl.RawTurtle(self.sc)
        self.sc.bgcolor("Black")
        
        
    def make_intro(self):
        design.intro(self.tt)
        self.c.destroy()
        self.f.destroy()
    def level_menu(self):
        self.ls=level.Levelscreen(self.root)
        
    def make_board(self):
        self.bf=tk.Frame(self.root,bg="yellow")
        self.bf.pack(anchor="n")
        b=Chok.Board("X",self.bf)
        
        
        
a=Game()
a.make_intro()
a.level_menu()
        
        
    

