from wordlist import Words
from random import shuffle
from tabulate import tabulate
from time import sleep

# Hangman States
Hangman0 = "\n\n\n\n\n"
Hangman1 = "\n\n\n\n\n _____"
Hangman2 = "|\n|\n|\n|\n|\n|_____"
Hangman3 = "|____\n|\n|\n|\n|\n|_____"
Hangman4 = "|____\n|   |\n|\n|\n|\n|_____"
Hangman5 = "|____\n|   |\n|   O\n|\n|\n|_____"
Hangman6 = "|____\n|   |\n|   O\n|   |\n|\n|_____"
Hangman7 = "|____\n|   |\n|   O\n|  /|\n|\n|_____"
Hangman8 = "|____\n|   |\n|   O\n|  /|\\\n|\n|_____"
Hangman9 = "|____\n|   |\n|   O\n|  /|\\\n|  /\n|_____"
Hangman10 = "|____\n|   |\n|   O\n|  /|\\\n|  / \\\n|______"

HangmanStates : list = [Hangman0, Hangman1, Hangman2, Hangman3, Hangman4, Hangman5, Hangman6, Hangman7, Hangman8, Hangman9, Hangman10]

# Init
Category: str = 'City'
Levels: list = Words[Category]
shuffle(Levels)
isPlayerLose = False
score = 0

print(f"Category: {Category}")
sleep(1)

for word in Levels:
    currentLetters = list('_' * len(word))
    options = [
        ['A','B','C','D','E','F','G','H','I','J','K','L','M'],
        ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ]
    Chance = 10
    isLevelOver = False

    while(1):
        currentWord = "".join(currentLetters)

        print('-'*20)
        print(HangmanStates[10 - Chance])
        print(f"Word: {currentWord}")
        
        if Chance <= 0:
            isPlayerLose = True
            isLevelOver = True
        elif currentWord == word:
            isLevelOver = True
        
        if isLevelOver == True:
            if isPlayerLose == False:
                score += 1
                print("Wow, You\'ve Guessed the Word!")
                sleep(1)
            else:
                print(f"Correct Word: {word}")
            break

        print("Options")
        print(tabulate(options))
        while(1):
            try:
                option = str(input("Enter your letter: "))
            except ValueError:
                continue
            
            if len(option) == 1:
                if option != '-':
                    option = option.upper()
                    if option in options[0]:
                        options[0][options[0].index(option)] = '-'
                        break
                    elif option in options[1]:
                        options[1][options[1].index(option)] = '-'
                        break
        
        # Checking
        if option in word:
            for i in range(0,len(word)):
                letter = word[i]
                if option == letter:
                    currentLetters[i] = letter
        else:
            Chance -= 1
    
    if isPlayerLose == True:
        print("You Lose\n")
        sleep(1)
        print(f"Your Final Score: {score}")
        sleep(1)
        print(f"Thank you for playing!")
        break

if isPlayerLose == False:
    print("You Win")
    sleep(1)
    print(f"Your Final Score: {score}")
    sleep(1)
    print(f"Thank you for playing!")