# Program for student's fundraising event?

# Python Functions - AP
## Functions are a way to organize your code into blocks that can be reused multiple times.
## They can take parameters, perform operations, and return results.
## Learning to define and use functions is a key skill in programming.

# Defining Functions - CC
## To define a function in Python, we use the `def` keyword followed by the function name and parentheses.
## Here's how to define a simple function:

def greet(name):
    return "Hello, " + name + "!"

## In this example, `greet` is a function that takes one parameter, `name`, and returns a greeting message.
## Make note of the indentation

# Calling Functions - AP
## To use a function, you simply call it by its name and pass the required parameters.
## Here's how to call the `greet` function:

print(greet("Alice"))

## This will output: Hello, Alice!

# Parameters and Arguments - CC
## Parameters are variables that you define in the function definition.
## Arguments are the values you pass to the function when you call it.
## In the `greet` function, `name` is a parameter, and "Alice" is an argument.

# Functions with Multiple Parameters - AP
## Functions can also take more than one parameter. Here's an example:

def add_numbers(a, b):
    return a + b

## This function `add_numbers` takes two parameters, `a` and `b`, and returns their sum.

# Using Functions in Programs - CC
## Functions are useful for breaking down complex problems into simpler parts.
## Let's use functions to solve the area problem from the last lesson.

## Here's how we can modify the program to use functions:

### Function to calculate circle area
def circle_area(radius):
    return 3.14 * radius ** 2

### Function to calculate shaded area
def shaded_area(radius_outside, radius_inside):
    area_outside = circle_area(radius_outside)
    area_inside = circle_area(radius_inside)
    return area_outside - area_inside

### Using the functions
radius_outside = 10
radius_inside = 5

print("The area of the shaded region is ", shaded_area(radius_outside, radius_inside))

# Using logical operators to test functions
answer_is_incorrect = (area_shaded > area_outside) || (area_shaded < area_inside)

# Individual Practice - AP

## They should define functions for the area of a triangle and use those functions to find the shaded area.



# End of week2.py
