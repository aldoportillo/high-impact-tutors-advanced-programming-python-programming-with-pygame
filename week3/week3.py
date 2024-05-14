# Lesson: Simplifying Fractions with Python
# This lesson covers how to create a Python function to simplify fractions. The function will determine the greatest common divisor (GCD) of the numerator and denominator and use it to reduce the fraction to its simplest form.
# I noticed during math tutoring this was a weakpoint

# Objectives:
# - Understand how to identify the smallest of two numbers.
# - Learn how to find all divisors of a number.
# - Use the GCD to simplify fractions.

# Simplify Fraction Function Explanation:

# 1. Determine the Smaller Number
# The function begins by comparing the numerator and the denominator to determine which one is smaller. This is crucial because the GCD has to be a factor of both numbers, and no factor can be larger than the smaller of the two numbers.

if numerator > denominator:
    smallest_number = denominator
    largest_number = numerator
else:
    smallest_number = numerator
    largest_number = denominator

# 2. Find Divisors of the Smaller Number
# Next, the function finds all possible divisors of the smaller number. These divisors are candidates for the GCD. We start our loop from 1 to the smallest number inclusive, checking if `smallest_number % factor == 0` to ensure it's a divisor.

array = []
for factor in range(1, smallest_number + 1):
    if smallest_number % factor == 0:
        array.append(factor)

# 3. Determine the Greatest Common Divisor
# With the list of divisors, we then check which of these is also a divisor of the larger number. The largest of these common divisors is the GCD.

largest_factor = 0
for factor in array:
    if largest_number % factor == 0:
        if largest_factor < factor:
            largest_factor = factor

# 4. Simplify the Fraction
# Finally, the function divides both the numerator and the denominator by the GCD to simplify the fraction.

simplified_numerator = numerator / largest_factor
simplified_denominator = denominator / largest_factor
return f'{int(numerator)}/{int(denominator)} Simplifies to {int(simplified_numerator)}/{int(simplified_denominator)}'

# Interactive Script
# The script prompts the user to enter a numerator and a denominator, and then it displays the simplified fraction.

print("Welcome to the fraction simplifier: ")
numerator = int(input("What is the Numerator: "))
denominator = int(input("What is the Denominator: "))
print(simplify_fraction(numerator, denominator))

# Discussion:
# - This function is a practical application of loops, conditionals, and lists in Python.
# - Understanding this process helps in grasping how mathematical concepts can be implemented in programming.
