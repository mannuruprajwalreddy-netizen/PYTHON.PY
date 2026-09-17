# Scientific Calculator for Two Numbers
# This program performs common arithmetic and scientific operations
# on two numbers.

import math

print("Scientific Calculator for Two Numbers")

try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
except ValueError:
    print("Please enter valid numbers.")
else:
    print("\nResults")
    print("Addition:", first_number + second_number)
    print("Subtraction:", first_number - second_number)
    print("Multiplication:", first_number * second_number)

    if second_number != 0:
        print("Division:", first_number / second_number)
        print("Remainder:", first_number % second_number)
    else:
        print("Division: undefined because the second number is zero")
        print("Remainder: undefined because the second number is zero")

    print("Power:", first_number ** second_number)

    if first_number >= 0:
        print("Square root of first number:", math.sqrt(first_number))
    else:
        print("Square root of first number: not a real number")

    if second_number >= 0:
        print("Square root of second number:", math.sqrt(second_number))
    else:
        print("Square root of second number: not a real number")
