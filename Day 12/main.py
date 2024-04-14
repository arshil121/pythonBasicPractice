import random

number = random.randint(1, 100)
print("Number: ", number)
print(
    "Welcome to the number guessing game!\nI am thinking of a number between 1 and 100"
)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    print("You have 10 attempts")
    attempts = 10
elif difficulty == "hard":
    print("You have 5 attempts")
    attempts = 5

while attempts != 0:
    guess = int(input("Make a guess: "))
    if guess < number:
        attempts -= 1
        print(f"You have remainning guess: {attempts}")
        print("Your guess is too low.")
    elif guess > number:
        attempts -= 1
        print(f"You have remainning guess: {attempts}")
        print("Your guess is too high.")
    else:
        print("Correct guess")
        break
