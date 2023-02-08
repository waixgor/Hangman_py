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

def checkWord(animal, letter, wordList):
    # This function checks if the letter is in the word.
    # It will return an integer for the correct guesses or 0 for no correct guess.
    correctGuess = 0

    for i in range(len(animal)):
      if animal[i] == letter.upper():
        correctGuess += 1
        wordList[i] == letter.upper()
    
    return correctGuess
        
def printStuff(life, missedLetter, wordList):
    # This function prints current in-game information each time
    print(hangmanPic[life])
    print("\nMissed letters: ")
    print(*missedLetter)
    print()
    print(*wordList)

def question():
    # This function asks the user to exit the program or not and return a boolean value for the input
    switch = True
    question = input("Do you want to play again? (y/n) ")
    while question.lower() not in ['y', 'n']:
        print("Please enter y or n")
        question = input("Do you want to play again? (y/n) ")
    if question.lower() == 'n':
        switch = False
    return switch


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
        animal = randomWord().upper()
        correctGuessCounter = 0
        wordList = appendList(animal)
        print(animal)
        printStuff(life, missedLetter, wordList)
        gameSwitch = True
        while gameSwitch:
            letter = inputLetter(missedLetter)
            correctGuess = checkWord(animal, letter, wordList)
            if correctGuess > 0:
                correctGuessCounter += correctGuess
            else:
              life += 1
              missedLetter.append(letter.upper())
            
            if correctGuessCounter == len(animal):
                print(f"Yes! The secret word is {animal}! You have won!")
                gameSwitch = False
            else:
                printStuff(life, missedLetter, wordList)

                if life == len(hangmanPic):
                    print("You have run out of guesses!")
                    print(f"After {life} missed guesses and {correctGuessCounter} correct guesses, the word was \"{animal}\"")
                    gameSwitch = False
        programSwitch = question()
 
if __name__ == "__main__":
    main()