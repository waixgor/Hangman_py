# This program is written by Anthony Wu on Feb 8, 2022
import random

hangmanPic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def listOfWords():
    # This function return a list that contain all the words from a file
    in_file = open("words.txt", "r")
    words = [word.strip() for word in in_file.readlines()]
    in_file.close()
    return words

def randomWord():
    # This function return a random word from a list of words
    wordList = listOfWords()
    randomWord = random.choice(wordList)
    return randomWord

def appendList(animal):
    # This function return a list that contain underscores for the animal word 
    return ['_' for i in range(len(animal))]

def inputLetter(missedLetter):
    # This function asks user for a valid letter input
    switch = True
    while switch:
        letter = input("Guess a letter.\n")
        if checkLetter(letter, missedLetter):
            switch = False
    return letter

def checkLetter(letter, missedLetter):
    # This function return a boolean value to check if the letter is valid
    switch = False
    if not letter.isalpha():
        print("Please enger a LETTER.")
    elif len(letter) != 1:
        print("Please enter a single letter.")
    elif letter.upper() in missedLetter:
        print("You have already guessed that letter. Choose again.")
    else:
        switch = True
    return switch
        
# def printWord(aList):
#     # This function prints the word from list with spaces between the letters
#     for char in aList:
#       print(char, )

def printStuff(life, missedLetter, wordList):
    # This function 
    print(hangmanPic[life])
    print("\nMissed letters: ")
    print(*missedLetter)
    print()
    # printWord(missedLetter)
    print(*wordList)
    # printWord(wordList)

def main():
    # This is the mainline of the program
    print(
        "#     #   ###   #     #  #####  #     #   ###   #      #\n" + 
        "#     #  #   #  ##    # #     # ##   ##  #   #  # #    #\n" +
        "#     # #     # # #   # #     # # # # # #     # #  #   #\n" +
        "####### ####### #  #  # #       #  #  # ####### #   #  #\n" +
        "#     # #     # #   # # #   ### #     # #     # #    # #\n" +
        "#     # #     # #    ## #     # #     # #     # #     ##\n" +
        "#     # #     # #     #  #####  #     # #     # #      #")
    print("---------------------------------------------------------")
    print("Welcome to Hangman")
    print("---------------------------------------------------------")
    programSwitch = True
    while programSwitch:
        life = 0
        missedLetter = []
        animal = randomWord()
        wordList = appendList(animal)
        printStuff(life, missedLetter, wordList)
        gameSwitch = True
        while gameSwitch:
            letter = inputLetter(missedLetter)
            print(letter)
            gameSwitch = False #temp code to prevent infinity loops
        programSwitch = False #temp code to prevent infinity loops

if __name__ == "__main__":
    main()