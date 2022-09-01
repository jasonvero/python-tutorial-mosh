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

# from utils import find_max
#
# numbers = [10, 3, 6, 2]
# maximum = find_max(numbers)  # The warning under 'max' is saying we are
# # changing the meaning of the original max function. This is considered a bad practice
# # print(max(numbers))  # purple 'max' indicates it is a built-in function
#
# print(maximum)

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Packages
# ---------------------------------------------------------------------------------------------------------------------

# Packages are another way to organize your code
# Packages are a container for multiple modules. A directory or folder to group related modules

# Think of mall: Different packages for Men's, Women's, and Kids clothing
# And when you go to the Men's section, there will be different modules: pants, shirts, jackets, socks

# Add new directory: ecommerce
# Put all modules related to ecommerce app: sales, shipping, customer service, etc.
# Having an empty directory, still need to add a special file within it
# Python file - __init__.py
# This is the manual way, but the automatic way is to just create a Python Package directly

# Create module 'shipping' in ecommerce package

# # First Approach
# import ecommerce.shipping  # prefix the name of package (ecommerce) to get the module (shipping)
# ecommerce.shipping.calc_shipping()

# # Second, less wordy approach
# from ecommerce import calc_shipping
# calc_shipping()

# # Or, below
# from ecommerce import shipping
# shipping.calc_shipping()

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Generating Random Values
# ---------------------------------------------------------------------------------------------------------------------

# Google : Python 3 Module Index
# These are all the modules built for Python: Datetime, email, etc.

# import random  # Because this is a built-in module, we do not need a module file to import

# for i in range(3):  # Using range() function to create a range object. We can loop through object 3 times in for loop
#     print(random.random())

# for i in range(3):
#     print(random.randint(10, 20))  # Get random values between a particular age

# members = ['John', 'Mary', 'Bob', 'Mosh']
# print(random.choice(members))  # Randomly picking an item from a list

# Exercise: Write program to roll a die
# Define class called 'Dice'
# Within the class, there will be a method called roll() - when we call the method, we get a tuple
# Tuple - a read only list

# import random
#
#
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second  # Return as a tuple.
#         # In Python, when returning a tuple as a function, don't need to add parentheses
#
#
# dice = Dice()
#
# print(dice.roll())



# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Working with Directories
# ---------------------------------------------------------------------------------------------------------------------

# Google : Python 3 Module Index
# Module: pathlib - Object-oriented filesystem paths. Meaning it provides classes
# which can be used to create objects to work with directories and files

from pathlib import Path

# Absolute path: Starts at the root of the hard disk
    # Windows: c:\Program Files\Microsoft
    # Mac: /user/local/bin
# Relative path: If we want to access the 'ecommerce' path directory

# path = Path("ecommerce")
# print(path.exists())

# path2 = Path("emails")
# path2.mkdir()  # this method will make a new directory
# path2.rmdir()  # this method will remove a directory


# path = Path()
# print(path.glob('*.py'))  # this method can search for files or directories in the current path
# passing an asterisk '*.*' means to search for all files in current directory
# '*.py' - searching for all the Python files
# '*.xls' - searching for all the Excel files

# We can iterate or loop through the generator object

# path = Path()
# for file in path.glob('*'):
#     print(file)

# path = Path()
# for file in path.glob('*.py'):
#     print(file)


# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Pypi and Pip
# ---------------------------------------------------------------------------------------------------------------------

# pypi.org
# Directory called Python Package Index or PyPI
# These packages are what people have built for their projects and have been published

# For example: Sending text messages in your program
# go to pypi.org and search for sms

# For this exercise, search for openpyxl on pypi.org
# this package is used for working on Excel worksheets

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Project 1: Automation with Python
# ---------------------------------------------------------------------------------------------------------------------

# Processing spreadsheets

# import openpyxl as xl  # alias xl
# from openpyxl.chart import BarChart, Reference  # In this package, we have a module called 'chart'
# # Within this module, we have classes called 'BarChart' and 'Reference'
#
#
# wb = xl.load_workbook('transactions.xlsx')  # Access workbook
# sheet = wb['Sheet1']  # Access sheet
#
# cell = sheet['a1']  # Give coordinate of cell; column and row
# # cell_a = sheet.cell(1, 1)  # Gives the exact same as above, but use the cell() method of the sheet object
# # Pass the row and the column (1, 1)
#
#
# # print(cell.value)
#
# # Now we want to iterate over all of these rows
#
# # First, how many rows do we have in this sheet object
# # print(sheet.max_row)  # sheet has four rows
#
# # Need to add a for loop that will generate the numbers 1-4
# for row in range(2, sheet.max_row + 1):  # By adding + 1, we will include the full range captured,
#     # which is only 1, 2, 3, and then + 1 to get the 4th row
#     # print(row)  # print this just to make sure program is running as expected
#
#     # We don't want the heading, so we want to ignore the first row
#     # Go back above and change range() function first parameter from 1 to 2
#
#     cell = sheet.cell(row, 3)
#     # print(cell.value)  # print to make sure we are grabbing the cells from column 3, and rows from row for loop
#     corrected_price = cell.value * 0.9
#     corrected_price_cell = sheet.cell(row, 4)  # gets the fourth column
#     corrected_price_cell.value = corrected_price  # sets the value of this corrected_price_cell
#
#
# # Now we want to add a chart by adding an import at the top
# # Select a range of values: We will take the 4th column and rows 2-4
#
# values = Reference(sheet,
#           min_row=2,  # Keyword arguments
#           max_row=sheet.max_row,  # This selects all the cells in all the columns, not what we want
#           min_col=4,  # Only want values in 4th column, need to set more keyword arguments
#           max_col=4)
#
# chart = BarChart()  # Create instance of BarChart() class
# chart.add_data(values)  # Pass values in add_data()
# sheet.add_chart(chart, 'e2')  # Add this chart to our sheet
#
# wb.save('transactions2.xlsx')  # Saves the workbook into a new file


# Code cleaned up

# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference
#
#
# def process_workbook(filename):  # create function and nest code within in
#
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet1']
#
#     for row in range(2, sheet.max_row + 1):
#         cell = sheet.cell(row, 3)
#         corrected_price = cell.value * 0.9
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#
#     values = Reference(sheet,
#               min_row=2,
#               max_row=sheet.max_row,
#               min_col=4,
#               max_col=4)
#
#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'e2')
#
#     wb.save(filename)

# Moving the above code into a module and then import it
# from excel_automation import process_workbook
#
# process_workbook(filename='transactions.xlsx')

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Project 2: Machine Learning with Python
# ---------------------------------------------------------------------------------------------------------------------

# Build a model or engine, and give it lots of data - 10K+ images of cats and dogs for example
# More input data, the more accurate model will be

# Steps:
# 1. Import data - normally through csv file
# 2. Clean the data - remove duplicates in data, remove bad data, conversions, etc. - model would learn bad patterns
# 3. Split Data into Training/Test sets - If 1k+ pics of cats and dogs, 80% can be for training, and 20% for testing
# 4. Create a Model - select an algorithm that will analyze the data
# 5. Train the Model - feed the model training data; the model will then look for patterns in the data
# 6. Make predictions - ask our model, is the image a cat or dog, and model will make a prediction
# 7. Evaluate and Improve - assess accuracy of predictions; fine-tune parameters of model


# Libraries and Tools:
# Numpy - multi-directional array
# Pandas - provides dataframes; a two-dimensional data structure like an Excel speadsheet
# Matplotlib - 2-dimensional plotting library for creating graphs and plots
# Scikit-Learn - provides common algorithms like decision trees, neural networks, etc.


# Jupyter - good tool to inspect data

# From this point of the tutorial we are working in Jupyter Notebooks

# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# --- Project 3: Building a Website with Django
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------





