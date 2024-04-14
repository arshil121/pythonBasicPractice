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

#user input
# name = input("Enter your name: ")
# print(len(name))

#variable switch
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

#project 01 of day 01
# print("Welcome to the Band Name Generator.\nWhat's the name of the city you grew up in?")
# cityName=input()
# print("What's your pet name?")
# petName=input()
# bandName=cityName + " "+petName
# print("Your band name could be",bandName)
###################################################################################################
#Day 02
#subscripting from string
# print("Hello"[0:])

#challenge 1
# number = input("Enter a number: ")

# num1=int(number[0])
# num2=int(number[1])
# sum=str(num1+num2)
# print("Sum is: " + sum)

#challeng 2: BMI calculator
# weight=float(input("Enter your weight in kg: "))
# height=float(input("Enter your height in m: "))

# BMI = weight/(height**2)
# print("Your bmi is: ", round(BMI,2))

#f string example
# name = "John Doe"
# age = 35
# profession = "Engineer"
# country = "USA"
# print(f"Hi {name}, \nYou are {age} years old. \nYour profession is {profession}. \nYou live in {country}")

#age calculator in days weeks months

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




  

