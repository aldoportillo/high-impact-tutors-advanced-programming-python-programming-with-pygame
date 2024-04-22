# Python Introduction 
## Python is a popular programming language used for web development, data analysis, artificial intelligence, and more.
## It's known for its simplicity and readability, making it a great choice for beginners and professionals alike.
## Understanding how to code can open up many opportunities in technology and beyond.

# Setting Up Environment
## Today, we'll be using Replit, an online platform that allows us to write and run Python code directly in our web browsers.
## Show how to navigate to the Replit website and create a new account.
## Demonstrate how to start a new Python project: "Once you're logged in, click on the '+ New Repl' button, choose Python as the language, and give your project a name.
## Explain the basic features of the Replit interface, including the code editor, console, and run button.

# Basic Python Syntax

## Python is an interpreted language, which means that code is executed line by line.
## The syntax of Python is relatively simple and easy to learn.
## Let's start with a simple example:

print("Hello, World!")

## In this example, we're using the `print` function to display the text "Hello, World!" on the console.
## The `print` function is a built-in function that takes a string as an argument and displays it on the screen.

# Variables and Data Types

## Variables are used to store data in a program. They can hold different types of data, such as numbers, strings, and booleans.
## Here's an example of how to declare a variable and assign it a value:

name = "Alice"
age = 30
is_student = False

## In this example, we're creating three variables: `name`, `age`, and `is_student`.
## The variable `name` is assigned the string "Alice", `age` is assigned the number 30, and `is_student` is assigned the boolean value False.

# Data Types

## Python has several built-in data types, including:

## Strings: A sequence of characters enclosed in single or double quotes.
## Integers: Whole numbers without a decimal point.
## Floats: Numbers with a decimal point.
## Booleans: True or False values.

## We can use the `type` function to determine the data type of a variable:

print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(is_student))  # <class 'bool'>

## In this example, we're using the `type` function to print the data type of the variables `name`, `age`, and `is_student`.

# Basic Operators

## Python supports various operators for performing arithmetic, comparison, and logical operations.

## Arithmetic Operators:
## Addition: +
## Subtraction: -
## Multiplication: *
## Division: / # gives the quotient
## Exponentiation: **
## Modulus: % # gives the remainder

## Comparison Operators:

## Equal to: ==
## Not equal to: !=
## Greater than: >
## Less than: <
## Greater than or equal to: >=
## Less than or equal to: <=

## Logical Operators:

## And: and
## Or: or
## Not: not

## Let's see some examples:

x = 10
y = 5

print(x + y)  # 15

print(x > y)  # True

print(x == y)  # False

# Homework Machine

## Now that we've covered the basics of Python syntax, let's create a simple program called the "Homework Machine."
## When helping one of the student's with their homework, I noticed that everything was a pattern in steps.
## Patterns are algorithms in the computer science world, and we can use them to solve problems.

## The problem we were solving in the homework was to find the area of a shaded region. 
## To solve this problem, we found the area of the outside shape, the area of the inside shape and then subtracted the two areas.

## Let's write a Python program that calculates the area of a shaded region given the radius of the outside circle and the inside circle.

## Here's the code:

radius_outside = 10
radius_inside = 5

area_outside = 3.14 * radius_outside ** 2
area_inside = 3.14 * radius_inside ** 2
area_shaded = area_outside - area_inside

print( "The area of the shaded region is ", area_shaded)


## If time allows, ask for help to do the same with triangles.

outside_base = 10
outside_height = 5
inside_base = 4
inside_height = 3

area_outside = 0.5 * outside_base * outside_height
area_inside = 0.5 * inside_base * inside_height
area_shaded = area_outside - area_inside

print( "The area of the shaded region is ", area_shaded)

## If they seem to understand use the opportunity to introduce functions
def shaded_area(radius_outside, radius_inside):
    area_outside = 3.14 * radius_outside ** 2
    area_inside = 3.14 * radius_inside ** 2
    area_shaded = area_outside - area_inside
    return area_shaded



# End of week1.py
