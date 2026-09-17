# Fibonacci Series Using Recursion
# This function returns the Fibonacci number at a given position.

def fibonacci(position):
    if position <= 1:
        return position
    return fibonacci(position - 1) + fibonacci(position - 2)


try:
    terms = int(input("Enter the number of terms: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    if terms <= 0:
        print("Please enter a positive number of terms.")
    else:
        series = [str(fibonacci(position)) for position in range(terms)]
        print("Fibonacci series:", " ".join(series))
