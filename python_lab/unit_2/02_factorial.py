# Factorial Using a Loop
# The factorial of n is the product of all positive integers up to n.

try:
    number = int(input("Enter a non-negative integer: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    if number < 0:
        print("Factorial is not defined for a negative number.")
    else:
        factorial = 1
        for value in range(1, number + 1):
            factorial *= value

        print("Factorial of", number, "is", factorial)
