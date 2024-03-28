# Prototype Function #

from time import sleep

LINE_UP = '\033[1A'
LINE_CLEAR = '\033[K'

# Custom print function with line clear and delay
def show(s="", del_:float = 0, end_:str="\n", sep_:str=" ") -> None:
    print(LINE_CLEAR + f"{s}", end=end_, sep=sep_)
    sleep(del_)

def line_up(up:int=1) -> None:
    # Set Cursor to previous n line
    for i in range(up):
        print("\033[1A", end='')

def clear_line(n:int=1) -> None:
    # Set Cursor to previous n line 
    for i in range(n):
        print("\033[1A", end='')

    # Clear line to current line
    for i in range(n):
        print('\033[K')
    
    # Return again to previous n line
    for i in range(n):
        print("\033[1A", end='')

show("ajdhaui\ndasdhash\nhadhiuadi",1)
clear_line(3)
show("HAHAHA",1)