# loops
# sequential loop with array:
# fruits = ['Apple','Mango','Pear']
# for fruit in fruits:
#   print(fruit)

# average from array:
# numbers = [156, 178, 165, 171, 187]
# sum_of_numbers = 0
# for items in numbers:
#     sum_of_numbers += items

# print(f"Average is: {sum_of_numbers/len(numbers)}")

# highest value from an array:
# numbers = [156,187, 178, 465, 171]
# highest = numbers[0]
# for items in numbers:
#     if highest < items:
#         highest = items

# print(f"Highest number is: {highest}")

# for loop with range
# for number in range(1, 10):
#     print(number)

# print("break")

# for number in range(1, 10, 2):
#     print(number)

# sum of even numbers from 1 to 100
# sum=0
# for i in range(1,101):
#   if(i%2==0):
#     sum+=i

# print(f"Sum of 1 to 100 of even numbers: {sum}")

############# PyPassword Generator
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
