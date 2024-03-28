from time import sleep

LINE_UP = '\033[A'
LINE_CLEAR = '\033[K'

# Custom print function with line clear and delay
def show(s="", del_:float = 0, end_:str="\n", sep_:str=" ") -> None:
    print('\033[K' + f"{s}", end=end_, sep=sep_)
    sleep(del_)

def line_up(up:int=1, clr=False) -> None:
    # Set Cursor to previous n line
    for i in range(up): print("\033[1A", end='')
    # Clear line option
    print("\033[K") if clr else None


def clear_line(n:int=1) -> None:
    # Set Cursor to and clearing previous n line(s)
    for i in range(n): print("\033[A\033[K", end='')