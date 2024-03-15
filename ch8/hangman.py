from wordlist import Words


# Hangman States
Hangman0 : str = "\n\n\n\n\n"
Hangman1 : str = "\n\n\n\n\n _____"
Hangman2 : str = "|\n|\n|\n|\n|\n|_____"
Hangman3 : str = "|____\n|\n|\n|\n|\n|_____"
Hangman4 : str = "|____\n|   |\n|\n|\n|\n|_____"
Hangman5 : str = "|____\n|   |\n|   O\n|\n|\n|_____"
Hangman6 : str = "|____\n|   |\n|   O\n|   |\n|\n|_____"
Hangman7 : str = "|____\n|   |\n|   O\n|  /|\n|\n|_____"
Hangman8 : str = "|____\n|   |\n|   O\n|  /|\\\n|\n|_____"
Hangman9 : str = "|____\n|   |\n|   O\n|  /|\\\n|  /\n|_____"
Hangman10 : str = "|____\n|   |\n|   O\n|  /|\\\n|  / \\\n|______"

HangmanStates : list = [Hangman0, Hangman1, Hangman2, Hangman3, Hangman4, Hangman5, Hangman6, Hangman7, Hangman8, Hangman9, Hangman10]

# Init


while(1):
    pass