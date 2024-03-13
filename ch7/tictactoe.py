from random import randrange
from tabulate import tabulate
from time import sleep

Board: list = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

AvailableSlot: list = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]

isPlayerTurn = True

while(1):
    print("Board")
    print(tabulate(Board, tablefmt="grid"))
    print("Slots")
    print(tabulate(AvailableSlot, tablefmt="grid"))

    if isPlayerTurn is True:
        while(1):
            try:
                index = int(input("Choose position: "))
            except ValueError:
                continue
            if (index >= 1) and (index <= 9):
                c_j: int = (index - 1) % 3
                r_i: int = round((index - 1 - c_j) / 3)
                
                if AvailableSlot[r_i][c_j] == f"{index}":
                    Board[r_i][c_j] = 'O'
                    AvailableSlot[r_i][c_j] = "-"
                    sleep(0.5)

                    isPlayerTurn = False
                    break
                else:
                    print("The position has already been taken")
    else: 
        while(1):
            index = randrange(9) + 1 # Default value of start is 0
            c_j: int = (index - 1) % 3
            r_i: int = round((index - 1 - c_j) / 3)

            if AvailableSlot[r_i][c_j] == f"{index}":
                Board[r_i][c_j] = 'X'
                AvailableSlot[r_i][c_j] = "-"
                sleep(0.5)
                print(f"The opponent has taken position {index}")

                isPlayerTurn = True
                break
    
    print("End of turn")