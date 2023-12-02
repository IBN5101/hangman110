import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
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

    def check_guess(self, guess):
        guess = guess.lower()
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

    def ask_for_input(self):
        while True:
            guess = input("Insert guess: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


hm = Hangman(["apple"])
hm.ask_for_input()
print(hm.word_guessed)
