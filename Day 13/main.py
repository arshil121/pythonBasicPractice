import random
from game_data import data
from art import logo, vs
import os


def get_random_account():
    return random.choice(data)


# Format account data into printable format.
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


## Get follower count.
## If Statement
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
is_game_ended = True
account_b = get_random_account()

# Make game repeatable.
while is_game_ended:
    # Generate a random account from the game data.
    account_a = account_b
    account_b = get_random_account()
    while account_a == account_b:
        account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")
    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(
        guess, account_a["follower_count"], account_b["follower_count"]
    )
    os.system("cls")
    # Check if user is correct.
    if is_correct:
        score += 1
        print(f"You are correct. Your current score: {score}")
    else:
        is_game_ended = False
        print(f"You are wrong. Your final score: {score}")
