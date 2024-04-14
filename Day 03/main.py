# print("hello")
# print("this is my code")

# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")
# print("")

# #using one print statement
# print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

# #concat string
# print("Hello" + " Arshil")

# user input
# name = input("Enter your name: ")
# print(len(name))

# variable switch
# a=5
# b=6
# print("a: ", a)
# print("b: ", b)
# print("Switching....")
# temp=a
# a=b
# b=temp
# print("a: ", a)
# print("b: ", b)

# project 01 of day 01
# print("Welcome to the Band Name Generator.\nWhat's the name of the city you grew up in?")
# cityName=input()
# print("What's your pet name?")
# petName=input()
# bandName=cityName + " "+petName
# print("Your band name could be",bandName)
###################################################################################################
# Day 02
# subscripting from string
# print("Hello"[0:])

# challenge 1
# number = input("Enter a number: ")

# num1=int(number[0])
# num2=int(number[1])
# sum=str(num1+num2)
# print("Sum is: " + sum)

# challeng 2: BMI calculator
# weight=float(input("Enter your weight in kg: "))
# height=float(input("Enter your height in m: "))

# BMI = weight/(height**2)
# print("Your bmi is: ", round(BMI,2))

# f string example
# name = "John Doe"
# age = 35
# profession = "Engineer"
# country = "USA"
# print(f"Hi {name}, \nYou are {age} years old. \nYour profession is {profession}. \nYou live in {country}")

# age calculator in days weeks months

# age = float(input("Enter your age: "))
# month = age * 12
# week = month / 4
# day = week * 7
# print(f"You are {month} months, {week} weeks, and {day} days old.")

# Project 2: tip calculator
# print("Welcome to the tip calculator.")
# total_Bill = float(input("What was the total bill: $"))
# tipPercent = int(input("How much did you tip as a percentage of the total bill? 10, 12 or 15?: "))
# people = int(input("How many people to split the bill?: "))

# bill_with_tip = tipPercent/100 * total_Bill + total_Bill
# print(f"Your total payment is: {bill_with_tip}")
# each_person_bill = bill_with_tip/people
# print(f"Each person should pay: ${each_person_bill:.2f}")

#################################################################################################
# Day 03
# height = float(input("Enter your height: "))
# if height > 120:
#     print("You can ride")
#     age = float(input("Enter your age: "))
#     if age < 12:
#         print("Your ticket is $5")
#     elif age <= 18:
#         print("Your ticket is $7")
#     else:
#         print("Your ticket is $12")
# else:
#     print("You can't ride")

# even or odd
# num = int(input("Enter a number: "))
# if num%2==0:
#   print("Even")
# else:
#   print("Odd")

# upgraded bmi calculator
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in m: "))

# BMI = weight / (height**2)
# print(f"Your BMI is: {BMI:.2f}")  # Print BMI upfront for clarity

# if BMI < 18.5:
#     print("Underweight")
# elif BMI < 25:  # If BMI is >= 18.5 and < 25
#     print("Normal weight")
# elif BMI < 30:  # If BMI is >= 25 and < 30
#     print("Overweight")
# else:  # If BMI is >= 30
#     print("Obesity")

# Pizza order problem
# print("Welcome to python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, L: ")
# add_pepperoni = input("Do you want to add pepperoni? Y/N: ")
# extra_cheese = input("Do you want extra cheese? Y/N: ")

# if size.upper() == "S":
#     bill = 15
# elif size.upper() == "M":
#     bill = 20
# elif size.upper() == "L":
#     bill = 25
# else:
#     print("Wrong input!!")


# if add_pepperoni.upper() == "Y" and size.upper() == "S":
#     bill += 2
# elif add_pepperoni.upper() == "Y" and size.upper() == "M" or size.upper() == "L":
#     bill += 3

# if extra_cheese.upper() == "Y":
#     bill += 1

# print(f"Your final bill is: {bill}")

##################################################################################################
# love calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name?: ")
# name2 = input("What is their name?: ")
# combined_string = (name1 + name2).lower()

# t = combined_string.count("t")
# r = combined_string.count("r")
# u = combined_string.count("u")
# e = combined_string.count("e")
# true = t + r + u + e

# l = combined_string.count("l")
# o = combined_string.count("o")
# v = combined_string.count("v")
# e = combined_string.count("e")
# love = l + o + v + e

# love_score = int(str(true) + str(love))

# print(f"Your love score is: {love_score}%")

# if (love_score < 10) or (love_score > 90):
#     print("You go together like code and mentos")
# elif int(love_score) > 40 or int(love_score) < 50:
#     print("You are probably just friends.")
# else:
#     print("You two make a great pair.")

##########################
# treasure island

