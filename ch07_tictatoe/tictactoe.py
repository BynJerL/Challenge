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
isPlayerWin = False
isPlayerLose = False
isGameOver = False

while(1):
    print("Board")
    print(tabulate(Board, tablefmt="grid"))

    if isGameOver == True:
        if isPlayerWin == True:
            print("Player Wins!")
        elif isPlayerLose == True:
            print("Computer Wins!")
        else:
            print("Draw!")
        break

    print("Slots")
    print(tabulate(AvailableSlot, tablefmt="grid"))

    if isPlayerTurn is True:
        mark = 'O'
        while(1):
            try:
                index = int(input("Choose position: "))
            except ValueError:
                continue
            if (index >= 1) and (index <= 9):
                c_j: int = (index - 1) % 3
                r_i: int = round((index - 1 - c_j) / 3)
                
                if AvailableSlot[r_i][c_j] == f"{index}":
                    Board[r_i][c_j] = mark
                    AvailableSlot[r_i][c_j] = "-"
                    sleep(0.5)

                    isPlayerTurn = False
                    break
                else:
                    print("The position has already been taken")
    else: 
        mark = 'X'
        while(1):
            index = randrange(9) + 1 # Default value of start is 0
            c_j: int = (index - 1) % 3
            r_i: int = round((index - 1 - c_j) / 3)

            if AvailableSlot[r_i][c_j] == f"{index}":
                Board[r_i][c_j] = mark
                AvailableSlot[r_i][c_j] = "-"
                sleep(0.5)
                print(f"The opponent has taken position {index}")

                isPlayerTurn = True
                break

    print("End of turn")

    # Checking
    for r in range(3):
        if (Board[r][0] == Board[r][1] == Board[r][2] == mark):
            if mark == 'O':
                isPlayerWin = True
            elif mark == 'X':
                isPlayerLose = True
            isGameOver = True

            break
    
    if isGameOver == True:
        continue

    for c in range(3):
        if (Board[0][c] == Board[1][c] == Board[2][c] == mark):
            if mark == 'O':
                isPlayerWin = True
            elif mark == 'X':
                isPlayerLose = True
            isGameOver = True

            break
    
    if isGameOver == True:
        continue
    
    if (Board[0][0] == Board[1][1] == Board[2][2] == mark) or (Board[0][2] == Board[1][1] == Board[2][0] == mark):
        if mark == 'O':
            isPlayerWin = True
        elif mark == 'X':
            isPlayerLose = True
        isGameOver = True

        continue

    if AvailableSlot == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]:
        isGameOver = True