# hangman project
import random
from hungman_words import word_list
from hungman_art import stages, logo

print(logo)
print("Welcome to Hangman!")
# word_list = ["ardvark", "baboon", "camel"]
secret_word = random.choice(word_list)
word_length = len(secret_word)
end_of_game = False
lives = 6
display = ["_"] * word_length
letters_guessed = []


def getGuess():
    global end_of_game, lives
    guess = input("Enter your guess: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid Input")
    elif guess in letters_guessed:
        print("You've already guessed that letter.")
    else:
        letters_guessed.append(guess)
        if guess not in secret_word:
            lives -= 1
            print("Wrong guess. You lose a life.")
            print(stages[lives])
        else:
            for i in range(word_length):
                if secret_word[i] == guess:
                    display[i] = guess
    print(" ".join(display))
    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print("You lose.")


while not end_of_game:
    getGuess()
