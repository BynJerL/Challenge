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

isOddPlayerTurn = True
isPlayer1Win = False
isPlayer2Win = False
isGameOver = False

while(1):
    print("Board")
    print(tabulate(Board, tablefmt="grid"))

    if isGameOver == True:
        if isPlayer1Win == True:
            print("Player 1 Wins!")
        elif isPlayer2Win == True:
            print("Player 2 Wins!")
        else:
            print("Draw!")
        break

    print("Slots")
    print(tabulate(AvailableSlot, tablefmt="grid"))

    mark = 'O' if (isOddPlayerTurn is True) else 'X'
    print("Player 1") if (isOddPlayerTurn is True) else print("Player 2")

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

                isOddPlayerTurn = False if (isOddPlayerTurn is True) else True
                break
            else:
                print("The position has already been taken")

    print("End of turn")

    # Checking
    for r in range(3):
        if (Board[r][0] == Board[r][1] == Board[r][2] == mark):
            if mark == 'O':
                isPlayer1Win = True
            elif mark == 'X':
                isPlayer2Win = True
            isGameOver = True

            break
    
    if isGameOver == True:
        continue

    for c in range(3):
        if (Board[0][c] == Board[1][c] == Board[2][c] == mark):
            if mark == 'O':
                isPlayer1Win = True
            elif mark == 'X':
                isPlayer2Win = True
            isGameOver = True

            break
    
    if isGameOver == True:
        continue
    
    if (Board[0][0] == Board[1][1] == Board[2][2] == mark) or (Board[0][2] == Board[1][1] == Board[2][0] == mark):
        if mark == 'O':
            isPlayer1Win = True
        elif mark == 'X':
            isPlayer2Win = True
        isGameOver = True

        continue

    if AvailableSlot == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]:
        isGameOver = True