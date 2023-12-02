'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

    def __init__(self, word_list, num_lives=5):
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}

        # Word to be guessed
        self.word = str(random.choice(word_list))
        # Guess attempt
        self.word_guessed = ["_"] * len(self.word)
        # Number of UNIQUE letter in the word that has not been guessed yet
        self.num_letters = len(set(self.word))
        # Lives
        self.num_lives = num_lives
        # Initial word list
        self.word_list = word_list
        # List of guess tried
        self.list_of_guesses = []

        print(f"The mistery word has {self.num_letters} characters")
        print(f"{self.word_guessed}")

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        guess = letter.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = guess
            self.num_letters -= 1

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            guess = input("Insert guess: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"{guess} was already tried.")
            else:
                self.check_letter(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    # If the user guesses the word, print "Congratulations! You won!"
    # If the user runs out of lives, print "You lost! The word was {word}"
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break
        if game.num_letters > 0:
            print(f"\t{game.word_guessed}")
            game.ask_letter()
        if game.num_lives > 0 and game.num_letters == 0:
            print("Congratulation! You won!")
            break


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
