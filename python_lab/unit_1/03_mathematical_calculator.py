# Mathematical Calculator using Built-in Functions and Math Module
# This program demonstrates built-in functions and common functions
# from Python's math module.

import math

print("Mathematical Calculator")

try:
    number = float(input("Enter a non-negative number: "))
except ValueError:
    print("Please enter a valid number.")
else:
    if number < 0:
        print("Please enter a non-negative number.")
    else:
        print("\nResults")
        print("Absolute value:", abs(number))
        print("Rounded value:", round(number))
        print("Floor value:", math.floor(number))
        print("Ceiling value:", math.ceil(number))
        print("Square root:", math.sqrt(number))
        print("Power of 2:", math.pow(number, 2))
        print("Natural logarithm:", math.log(number) if number > 0 else "undefined for zero")
        print("Sine in radians:", math.sin(number))
        print("Cosine in radians:", math.cos(number))
