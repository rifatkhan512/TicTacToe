import tkinter as tk
import Chok

root= tk.Tk()
root.title("Rifat's tic tac toe")
root.resizable(0,0)

current_player="O"


a=Chok.Board(current_player,root)


a.newboard()

root.mainloop()


