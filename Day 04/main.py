# day 04 - random and list
import random

# randomInteger = random.randint(1,10)
# print(randomInteger)

# randomFloat = random.random() * 5 # 0.1 to multiplication is the range
# print(randomFloat)

# ##########################################
# print("Heads or Tails")
# input = input("Enter head or tail as 1 or 0: ")

# random_int = random.randint(0,1)

# if(int(input) == random_int):
#   print("You guessed it right!")
# else:
#   print("Sorry you are wrong.")
#################################################################################################
# list - Array - Python
# arr = ["a", "b", "c"]
# print(arr[0])
# print(arr[2])
# print(len(arr))
# arr.append("d")
# arr.extend(["e","f","g"])
# print(arr)

##########################################
# names = input("Enter everybody's name with separated with comma: ").split(", ")

# # length_of_names = len(names)

# # random_value = random.randint(0, length_of_names-1)
# print(f"{random.choice(names)} is going to buy the meals today!!")

# fruits = ['apple', 'banana', 'cherry']
# vegetables = ['carrot','onion','potato']
# foods = [fruits, vegetables] # nested array
# print(foods)
##################################################################################################
# create 3x3 matrix
# map = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# position = input("Where you want to put X: ")
# row = int(position[0]) - 1
# col = int(position[1]) - 1
# map[row][col] = 0
# print(map)

choices = ["rock", "paper", "scissors"]
user_input = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.choice(choices)
print(f"Your choice is {user_input} and computer choice is {computer_choice}")

if user_input == computer_choice:
    print("Draw")
elif (
    (user_input == "rock" and computer_choice == "scissors")
    or (user_input == "scissors" and computer_choice == "paper")
    or (user_input == "paper" and computer_choice == "rock")
):
    print("You win")
else:
    print("Computer wins")
