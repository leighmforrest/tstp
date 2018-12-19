from random import choice

words = list()

# SOURCE: https://stackoverflow.com/questions/3142054/python-add-items-from-txt-file-into-a-list
# HANGMAN.TXT SOURCE: https://raw.githubusercontent.com/Xethron/Hangman/master/words.txt
with open("hangman.txt", "r") as f:
    words = [line.strip() for line in f]


def get_word():
    """Get a word from the official list."""
    return choice(words)

def hangman(word):
    wrong = 0
    stages = ["",
              "---------",
              "|    |   ",
              "|    |   ",
              "|    0   ",
              "|   /|\  ",
              "|   / \  ",
              "|        ",
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg).strip()[0]
        if char in rletters:
            # Add all instances to board in a single turn
            while char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print(f"You lose! It was {word}.")


word = get_word()
# print("WORD:", word) NOTE: THIS LINE IS FOR TESTING
hangman(word)

