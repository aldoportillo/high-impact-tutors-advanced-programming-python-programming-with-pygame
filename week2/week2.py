# Python Functions with Interactive Console - AP
## As mentioned in the previous lesson, functions are powerful tools in programming that help you organize and reuse code. 
## This week, we'll make our lessons interactive by using console prompts to input data into functions.

# Defining Functions - CC
## As a refresher, to define a function in Python, use the `def` keyword followed by the function name and parentheses.
## Here's how to define a simple function that greets a user:

def greet(name):
    return "Hello, " + name + "!"

## This function takes one parameter, `name`, and returns a greeting message.

# Interactive Function Calls - AP
## Instead of hardcoding values, let's use the `input()` function to get user input.

user_name = input("Enter your name: ")
print(greet(user_name))

## This modification allows the user to input their name, which is then used by the `greet` function.

# Functions with Multiple Parameters - CC
## As a refresher, functions can accept more than one parameter. Here's a function to add two numbers:

def add_numbers(a, b):
    return a + b

## Let's make it interactive:

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
print("The sum is: ", add_numbers(first_number, second_number))

### The first_number line prompts the user to enter the first number.
### The input() function reads the input from the user as a string.
### The float() function then converts the input string to a floating-point number.
### The result is assigned to the variable first_number.

# Using Functions to Calculate Areas - AP
## We'll define functions to calculate areas and let users input the dimensions.

### We will ask students to help us rewrite these to gauge understanding. 
### Function to calculate circle area
def circle_area(radius):
    return 3.14 * radius ** 2

### Function to calculate shaded area between two circles
def shaded_area(radius_outside, radius_inside):
    area_outside = circle_area(radius_outside)
    area_inside = circle_area(radius_inside)
    return area_outside - area_inside

### We will take the lead here again
### Interactive area calculation
radius_outside = float(input("Enter the radius of the outside circle: "))
radius_inside = float(input("Enter the radius of the inside circle: "))
print("The area of the shaded region is:", shaded_area(radius_outside, radius_inside))

## If time allows: We will run through rectangle and triangle

## If time allows: Logic and Testing Functions with User Input - CC
## We'll now use logical operators to check conditions and print results based on user inputs.
### As a refresher: logical operators are "and", "or", and "not"
### Comparison operators are <, >, <=, >=, ==, !=

# If area is not smaller than inside circle and bigger than inside circle (if one of these is true, it would return false -- that it is not valid)
def check_area_validity(area_shaded, area_outside, area_inside):
    return area_shaded <= area_outside and area_shaded >= area_inside

## Calling the function with user inputs
is_valid = check_area_validity(shaded_area(radius_outside, radius_inside), circle_area(radius_outside), circle_area(radius_inside))
print("Is the calculated shaded area valid?", is_valid)



# End of week3.py
