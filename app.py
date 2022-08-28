# ---------------------------------------------------------------------------------------------------------------------
# --- Date: 8/23/2022
# --- Project: Python Tutorial - Python Full Course for Beginners
# --- Source: https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=WL&index=1&t=61s&ab_channel=ProgrammingwithMosh
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Input
# ---------------------------------------------------------------------------------------------------------------------

# name = input('What is your name? ')
# fav_color = input('What is your favorite color? ')
# print(name + ' likes ' + fav_color)
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Type Conversion
# ---------------------------------------------------------------------------------------------------------------------

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(type(age))
# print(age)

# weight_lbs = input('What is your weight? (in pounds) ')
# print(type(weight_lbs))
# weight_kg = float(weight_lbs) * 0.453592
# print(type(weight_kg))
# print(weight_kg)
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Strings
# ---------------------------------------------------------------------------------------------------------------------

# Examples when using double quote vs. single quote
# course = "Python's Course for Beginners"
# print(course)

# course_2 = 'Python for "Beginners"'
# print(course_2)

# course_3 = '''
# Hi John,
# Here is our first email to you.
#
# Thank you,
# '''
# print(course_3)

# course_4 = 'Python for Beginners'
# print(course_4[0])  # index of first character
# print(course_4[-1])  # index of last character
# print(course_4[0:3])  # return first character to third character
# print(course_4[0:])   # return all characters starting at first index
# print(course_4[:5])   # return all characters up to fifth character
#
# another = course_4[:]  # return all characters from course_4 variable
# print(another)

# name = 'Jennifer'
# print(name[1:-1])  # returns character starting from index one, all the way to end but excluding the last index
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Formatted Strings
# ---------------------------------------------------------------------------------------------------------------------

# non-formatted string
# first_name = 'John'
# last_name = 'Smith'
# message = first_name + ' [' + last_name + '] is a coder'
# print(message)

# formatted string
# first_name = 'John'
# last_name = 'Smith'
# msg = f'{first_name} [{last_name}] is a coder'
# print(msg)
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- String Methods
# ---------------------------------------------------------------------------------------------------------------------

# For example, upper() is a function that belongs to strings object exclusively, so it is a method
# print() and len() are general purpose functions that are not specific to any type of object, so they are not methods
#
# Other String methods include: upper(), lower(), title(), find(), replace(),
# In Operator

# course = 'Python for Beginners'
#
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.title())
#
# print(course.find('Beginners'))  # find() method -- searches for index of a character or sequence of characters
#
# print(course.replace('Beginners', 'Absolute Beginners'))  # replace()
# print(course.replace('P', 'J'))
#
# print('Python' in course)  # in operator -- boolean expression
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Arithmetic Operations
# ---------------------------------------------------------------------------------------------------------------------

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
#
# print(10 // 3)  # // -- returns integer value
# print(10 % 3)  # % modulus -- returns remainder of the division
# print(10 ** 3)  # ** exponent -- power

# Augmented assignment operator

# x = 10
# x = x + 3  # incrementing a number
# x += 3  # += augmented assignment operator
# x -= 3  # augmented assignment operator
# print(x)
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Operator Precedence
# ---------------------------------------------------------------------------------------------------------------------

# x = (10 + 3) * 2 ** 2
# print(x)

# Order
# Parenthesis -- always takes priority
# Exponentiation -- 2 ** 3
# Multiplication or Division
# Addition or Subtraction
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Math Functions
# ---------------------------------------------------------------------------------------------------------------------

# Math module -- a module is a separate file with some reusable code
# Think of supermarket; different sections of fruits, vegetables, cleaning supplies, etc.
# Each section is a module
# Google python 3 math module to look at math function documentation


# import math
#
# print(math.ceil(2.9))  # ceil() -- the ceiling of the value
# print(math.floor(2.9))  # floor() -- the floor of the value
#
# x = 2.9
# print(round(x))
# print(abs(-2.9))  # abs() -- absolute value; always returns the positive representation of that value


# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# --- If Statements
# ---------------------------------------------------------------------------------------------------------------------

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")


# house_price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = house_price * 0.10
#
# else:
#     down_payment = house_price * 0.20
# print(f"Down payment: ${down_payment}")

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Logical operators
# ---------------------------------------------------------------------------------------------------------------------

# Used when we have multiple conditions
# and operator -- both conditions must be true
# or Operator -- at least one conditions must be true
# and not operator -- inverses any boolean value given; false becomes true; true becomes false

# If applicant has high income AND good credit; Eligible for a loan
# has_high_income = False
# has_good_credit = True
#
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# else:
#     print("Ineligible for loan")
#
#
# if has_high_income or has_good_credit:
#     print("Eligible for loan")


# If applicant has high income AND doesn't have a criminal record; Eligible for a loan
# has_good_credit = True
# has_criminal_record = False
#
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Comparison Operators
# ---------------------------------------------------------------------------------------------------------------------

# Where we want to compare a variable with a value
# boolean expression's
# >, >=, <, <
# == equality operator
# = assignment operator; changing the value, not expressing a boolean value
# !=

# temperature = 35
#
# if temperature > 30:  # boolean expression
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# name = input("What is your name? ")
# name_length = len(name)
#
# if name_length < 3:
#     print("Name must be at least 3 characters")
# elif name_length > 50:
#     print("Name can only be a maximum of 50 characters")
# else:
#     print("Name looks good!")

# ---------------------------------------------------------------------------------------------------------------------
# --- Weight Converter Program
# ---------------------------------------------------------------------------------------------------------------------

# weight = int(input("Weight: "))  # Pass int conversion on input so that it can be calculated in if statement
#
# unit = input("(L)bs or (K)g: ")
#
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"Your weight is {converted} kilos" )
# else:
#     converted = weight / 0.45
#     print(f"Your weight is {converted} lbs" )


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- While Loops
# ---------------------------------------------------------------------------------------------------------------------

# Executes block of code multiple times

# i = 1
#
# while i <= 5:
#     print('*' * i)
#     i = i + 1  # if we don't do this, i will always be '1', so loop will be stuck forever
# print("Done")


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Building a Guessing Game
# ---------------------------------------------------------------------------------------------------------------------

# Shift + F6 to refactor a variable to another designated value
# While loops also can run an else block

# secret_number = 9
# guess_count = 0  # number of guesses a user has made
# guess_limit = 3  # the limit of guesses a user gets to make
#
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1  # increments the guess count by 1
#     if guess == secret_number:
#         print("You won!")
#         break  # terminates the loop
# else:
#     print("Sorry, you failed!")

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Building the Car Game
# ---------------------------------------------------------------------------------------------------------------------

# D.R.Y -- Don't Repeat Yourself (all of those lower methods below)

# command = ""
# started = False
#
# while True:  # this original line was simplified from --> command != "quit": to True
#     command = input("> ").lower()  # call the lower method here because it doesn't need to be repeated
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True  # The else condition executes first, and sets started to True, so if ran again,
#                             # the above if statement executes
#             print("The car has started")
#     elif command == "stop":
#         if not started:
#             print("The car is already stopped")  # If the car has not been started,
#                                                  # this will output from the beginning.
#         else:
#             started = False
#             print("The car has stopped")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)  # remove indentations for the triple quote string
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, what did you enter?")

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- For Loops
# ---------------------------------------------------------------------------------------------------------------------

# Iterate over items of a collection, such as a string
# Which is a sequence of characters, so it looks like a collection

# Define a list with square brackets []
# A list is a list of items: emails, blog posts, numbers, names, etc.

# for item in ['Mosh', 'John', 'Sarah', 1, 2, 3]:
#     print(item)

# for item in range(5, 10, 2):  # range() function creates an object that we can iterate over
#     print(item)               # the 2 in the above range function adds a step

# Exercise: For loop to calculate total cost in shopping cart

# My solution:
# prices = [10, 20, 30]
#
# for cart in prices:
#     print(sum(prices))
#     break

# Mosh's solution:
# prices = [10, 20, 30]
# total = 0
#
# for price in prices:
#     total += price
# print(f"Total: {total}")

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Nested Loops
# ---------------------------------------------------------------------------------------------------------------------

# Adding one loop inside another loop
# Coordinates, combination of x and y value

# (x, y)
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)


# for x in range(4):  # outside loop, first iteration x is '; after three iterations of y loop, x moves to second iteration, 1
#     for y in range(3):  # inner loop, first iteration y is 0
#         print(f'({x}, {y})')

# Challenge - create a nested for loop that will iterate through a list and output a shape


# Cheating
# numbers = [5, 3, 5, 2, 2]
# for x_count in numbers:
#     print('x' * x_count)

# numbers = [5, 3, 5, 2, 2]
#
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):  # inner loop will execute 5 times
#         output += 'x'
#     print(output)

# Challenge 2: Modify numbers list to print an 'L' instead of 'F'

# numbers = [2, 2, 2, 2, 7]
#
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):  # inner loop will execute 5 times
#         output += 'x'
#     print(output)

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Lists
# ---------------------------------------------------------------------------------------------------------------------

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[0])  # specifying index to pull out specific item in the list
# print(names[-1])
# print(names[2:])
# print(names[2:4])
# print(names[:])

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'  # If we want to change a value in the list, at a specific index
#
# print(names)

# Challenge: Write a program to find the largest number in a list

# My solution
# numbers = [1, 5, 8, 55, 2]
#
# print(max(numbers))

# Mosh solution
# We want to iterate through the list to determine the largest number
# We get each item and compare it to the max variable
# If it is greater than max, we reset the max value and iterate again

# numbers = [1, 5, 8, 55, 2, 77]
# max_val = numbers[0]
#
# for number in numbers:
#     if number > max_val:
#         max_val = number
# print(max_val)

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- 2D Lists
# ---------------------------------------------------------------------------------------------------------------------

# In math, there's a concept called matrix; a rectangular array of numbers
# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
# 3x3 matrix in math

# A 2-dimensional list is a list where each item in that list is another list

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix[0][1] = 20  # Modifying the index within a matrix
# print(matrix[0][1])


# Using a for loop to iterate through the matrix

# for row in matrix:  # in each iteration, row will contain one value/item in the list
#     for item in row:
#         print(item)  # We get all items in our list

# ---------------------------------------------------------------------------------------------------------------------
# --- List Methods
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Tuples
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Unpacking
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Dictionaries
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Emoji Converter
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Functions
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Parameters
# ---------------------------------------------------------------------------------------------------------------------
