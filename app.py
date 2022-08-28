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

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in matrix:  # in each iteration, row will contain one value/item in the list
#     for item in row:
#         print(item)  # We get all items in our list

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- List Methods --- #
# ---------------------------------------------------------------------------------------------------------------------

# Operations we can perform on a list

# numbers = [5, 5, 2, 1, 7, 4]

# numbers.append(20)  # Add a new item to the end of the list
# numbers.insert(0, 10)  # Add a new item to the list; first specify index then specify value
# numbers.remove(5)  # Remove item from list
# print(numbers)
#
# numbers.clear()  # Clear all items from the list
# print(numbers)

# numbers.pop()  # Removes last item on the list
# print(numbers)

# print(numbers.index(4))  # Check for the existence of an item within a list

# print(50 in numbers)  # 'in' operator is another way to check fo the existence of an item within a list
#                       # unlike the index() method, this in expression doesn't generate an error

# print(numbers.count(5))  # Method for counting occurrences in an item

# print(numbers.sort())  # sort() to sort your lists
#                        # None represents the absence of a value
#                        # This sort method doesn't return any values, it sorts the list in place

# So format the sort as below
# numbers.sort()
# numbers.reverse()  # Reverses the sort of the list
# print(numbers)

# numbers = [5, 5, 2, 1, 7, 4]
# numbers2 = numbers.copy()  # copy() gets a copy of our list; remains independent of the list it copies
# numbers.append(10)
#
# print(numbers)
# print(numbers2)

# Exercise: Write a program to remove the duplicates in a list

# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []  # Create empty list to store the unique items
#
# for number in numbers:
#     if number not in uniques:  # if number in numbers is not in uniques empty list, append number to the empty list
#         uniques.append(number)
# print(uniques)


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Tuples --- #
# ---------------------------------------------------------------------------------------------------------------------

# Tuples are similar to lists, but unlike lists, you cannot modify tuples. They are immutable
# Tuples use parentheses () and lists use brackets []

# You will typically use lists, but there may be a situation where you don't want your list to accidently change
# In this instance, you'd use a tuple

# __dict__ magic method

# numbers = (1, 2, 3)
# print(numbers[0])

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Unpacking
# ---------------------------------------------------------------------------------------------------------------------

# coordinates = (1, 2, 3)  # coordinates for x, y, z
# x = coordinates = [0]
# y = coordinates = [1]
# z = coordinates = [2]

# unpacking will use far less code than above
# coordinates = (1, 2, 3)  # as a tuple
#
# x, y, z = coordinates
# print(x)

# coordinates = [1, 2, 3]  # as a list
#
# x, y, z = coordinates
# print(y)


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Dictionaries
# ---------------------------------------------------------------------------------------------------------------------

# You use a dictionary when you want to store information that comes as key-valued pairs
# Use curly braces {} to define a dictionary
# Each key in a dictionary must be unique. Like in a real world dictionary. One word listed, with its definition

# Example: A customer and their attributes
    # Name: John Smith
    # Email: john@gmail.com
    # Phone: 1234
    # What we have here are key value pairs: Name is a key, and associated value is John Smith

# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
#
# customer["name"] = "Jack Smith"
# customer["birthdate"] = "Jan 2 1980"
# print(customer.get("name"))  # get() method to access a key and its value
# print(customer.get("birthdate", "Jan 1 1980"))  # if key doesn't exist, returns the 'None' value, the absence of a value
#                                                 # you can also set a default value after the comma
# print(customer["name"])
# print(customer["birthdate"])

# Exercise: Type in phone number, and it outputs the digits into words

# phone = input("Phone: ")
#
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
#
# output = ""
# for char in phone:  # need to loop through the phone string
#     output += digits_mapping.get(char, "!") + " " # these quotes are adding a space to the end of each output string
#         # pass char as the key in this dictionary, "!" is a default value
#         # add what gets passed to an output string variable, above the for loop
# print(output)


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Emoji Converter
# ---------------------------------------------------------------------------------------------------------------------

# message = input(">")
# words = message.split(' ')  # goes through string, and any time it finds this character, it serves as a boundary
# emojis = {
#     ":)": "😀",  # control + command + space bar
#     ":(": "😞"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Functions
# ---------------------------------------------------------------------------------------------------------------------

# Breaking up our code in more manageable chunks
# A Function is a container for a few lines of code that perform a specific task

# def greet_user():  # means define; Python knows def means you are trying to define a function
#     print('Hi there!')
#     print('Welcome aboard')
#
#
# # When defining a function, should add two line breaks after the function
# print("Start")
# greet_user()
# print("Finish")


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Parameters
# ---------------------------------------------------------------------------------------------------------------------

# def greet_user(first_name, last_name):  # inside parenthesis, we can add parameters, which are placeholders for receiving information
#     print(f'Hi {first_name} {last_name}!')  # take this line of code with a specific function, and can pass it in the function multiple times
#     print('Welcome aboard')
#
#
# print("Start")
# greet_user("Mary", "Jane")  # An argument is the value supplied to a function. Mary is an argument that is passed to the name parameter
# print("Finish")

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Keyword Arguments
# ---------------------------------------------------------------------------------------------------------------------

# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')


# print("Start")
# greet_user("Smith", "John")  # These are positional arguments, meaning their order matters
# print("Finish")


# print("Start")
# greet_user(last_name="Smith", first_name="John")  # In Keyword Arguments, position doesn't matter
# print("Finish")

# Most of the time, you'd use positional arguments
# But in certain situations, keyword arguments help with code readability
# Like when the arguments being passed are hard to determine what parameter they should be passed to
# For example: if a function calc_cost(50, 5, 0.1), it's hard to determine what these numbers mean
# Keyword Arguments help here: calc_cost(total=50, shipping=5, discount=0.1)


# print("Start")
# greet_user("John", last_name="Smith")  # Keyword Arguments should always come after Positional Arguments
# print("Finish")


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Return Statement
# ---------------------------------------------------------------------------------------------------------------------

# How to create functions that return values
# Helpful if doing a calculation in a function, and you want to return a result

# def square(number):  # Function calculating square of a number
#     return number * number  # To return the calculation outside this function, use return statement
#
#
# print(square(3))  # We are passing square(3) as an argument to the print() function


# def square(number):
#     print(number * number)  # By default, all functions return the value 'None'
# None is the absence of a value; nothing, or NULL
#
#
# print(square(3))


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Creating a Reusable Function
# ---------------------------------------------------------------------------------------------------------------------

# Exercise: Reorganize Emoji Converter into a function

# You don't want to put the input() function into our reusable function
# input() can be used to receive input from terminal, but in other apps, it could be received in a GUI
# input() may not be reusable, so don't put it in our reusable function

# Similarly, we shouldn't include print() into our reusable function
# How we decide to output can be different between one program and another

# Takeaway: Your reusable function should not be worried about inputting or outputting


# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😀",
#         ":(": "😞"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input(">")
# print(emoji_converter(message))


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Exceptions
# ---------------------------------------------------------------------------------------------------------------------

# exit code 0 means we executed code with no errors
# any exit code other than 0 means there was an error and program has crashed
# ValueError is a type of error
# These type of errors are considered 'Exceptions' which crash our program

# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age  # This throws a ZeroDivisionError, which the except block we've defined below won't catch
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0')
# except ValueError:
#     print('Invalid value')


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Comments
# ---------------------------------------------------------------------------------------------------------------------

# Avoid using comments to explain what the code does
# Use comments to explain "Why's" and "How's" not "What's"
# If you've made certain assumptions, call this out in comments

# print Sky is blue -- # example of a bad comment
# Not only is the comment wordy, but if I change the string to 'Ocean', the comment becomes outdated
# print("Ocean is blue")


# Calculates and returns the square of a number -- # repetitive and creates noise in code
# def square(number):
#     return number * number


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Classes
# ---------------------------------------------------------------------------------------------------------------------

# Not specific to Python
# Classes are used to define new types
# Basic / simple types: Numbers, Strings, Booleans
# Complex types: Lists, Dictionaries

# These identified types can't always be used to model complex concepts
# Think of a concept of a point or a shopping cart
# A shopping cart is not a boolean, list, or dictionary, it's different

# We can use classes to define new types to model real concepts

# For this lesson, we will create a new class called 'point'

# With this class 'Point' created, we can create new objects
# An object is an instance of a class
# Where a class defines the template or blueprint of creating objects
# And objects are the actual instances based on that blueprint

# class Point:  # Pascal Naming Convention when first letter of every word is capitalized. Do not use underscores.
#     def move(self):  # self - special keyword
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()  # This creates a new object and returns it. We can then store it in a variable
# point1.x = 10  # Apart from methods, these objects can also have attributes. These attributes are variables that belong to a particular object
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()  # Each object is a different instance of our 'Point' class
# point2.x = 1
# print(point2.x)

# Summary: Classes are used to define new types
# These classes can have methods that are defined within the body of the class
# They can also have attributes that we set anywhere in our programs


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Constructors
# ---------------------------------------------------------------------------------------------------------------------

# We can create a point object with an x or y coordinate
# A constructor is a function that gets called at the time of creating an object

# class Point:
#     def __init__(self, x, y):  # init is short for initialize. This method/or function gets called when we create a new point object.
#         # This method is also what's considered a constructor. This method is used to construct or create an object
#         self.x = x  # self is a reference to the current object
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point = Point(10, 20)
# point.x = 11
# print(point.x)

# Exercise: Define a new type called 'Person'
# Each Person object should have a name attribute and a talk() method

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi, I am {self.name}.")
#
#
# person1 = Person('John Smith')
# person1.talk()
#
# person2 = Person('Bob Bob')
# person2.talk()

# Each object, person1 and person2, is a different instance of the 'Person' class


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Inheritance
# ---------------------------------------------------------------------------------------------------------------------

# Inheritance is a mechanism for reusing code
# Repeating or duplicating code is bad - D.R.Y : Don't Repeat Yourself

# In this example, we can create a parent class called 'Mammal'
# and have the Dog and Cat class inherit the method from Mammal

# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("BARK BARK")
#     # pass  # We are telling Python interpreter to pass this line. This resolves the issue with an empty class
#
#
# class Cat(Mammal):
#     def meow(self):
#         print("MEOW")
#
#
# dog1 = Dog()
# dog1.walk()
# dog1.bark()
#
# cat1 = Cat()
# cat1.walk()
# cat1.meow()


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Modules
# ---------------------------------------------------------------------------------------------------------------------

# Modules are files with some Python code
# Used to organize code into multiple files
# Think of a supermarket - different sections for fruits, vegetables, cleaning supplies, etc.

# For example, we can take the below functions, break them out into a "converter module (files)
# and we can import that converter into any program that needs a converter function

# Cut this code and paste it into the 'converters.py' module
# def lbs_to_kg(weight):
#     return weight * 0.45
#
#
# def kg_to_lbs(weight):
#     return weight / 0.45

# import converters
# from converters import lbs_to_kg  # after import, press control + space bar
# # you can directly call the function you need to use
#
# print(lbs_to_kg(160))  # This is cleaner than below,
# # since you don't need to prefix with the module name to use the function
#
# print(converters.lbs_to_kg(160))


# Exercise: Write function 'find_max()', it should take a list and find the largest number in list
# Afterwards, put the function in a module called 'utils'
# Then import utils into current app.py module and call the find_max() function
# Finally get the result and print it to the terminal

from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)  # The warning under 'max' is saying we are
# changing the meaning of the original max function. This is considered a bad practice
# print(max(numbers))  # purple 'max' indicates it is a built-in function

print(maximum)

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Packages
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Generating Random Values
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Working with Directories
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Pypi and Pip
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Project 1: Automation with Python
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Project 2: Machine Learning with Python
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Project 3: Building a Website with Django
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------





