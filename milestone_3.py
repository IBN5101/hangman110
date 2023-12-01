import random


def check_guess(letter):
    letter = letter.lower()
    if letter in word:
        print(f"Good guess! {letter} is in the word.")
    else:
        print(f"Sorry, {letter} is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input("Insert guess: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


word_list = ["apple", "banana", "orange", "strawberry", "cookie"]
word = random.choice(word_list)

ask_for_input()
