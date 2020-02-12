import random
import time
import Chok


def computers_move():
    
    time.sleep(1)
    while True:
        x=random.randint(0,2)
        y=random.randint(0,2)
        if Chok.Board.cells[x][y].mark:
            Chok.Board.cells[x][y].make_canvas()
            Chok.Board.cells[x][y].draw(Chok.Board.current_player)
            break
    
