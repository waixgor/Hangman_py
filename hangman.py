# This program is written by Anthony Wu on December 5, 2022
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


if __name__ == "__main__":
    main()