# Fibonacci Series Using a Loop
# Each Fibonacci number is the sum of the two previous numbers.

try:
    terms = int(input("Enter the number of terms: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    if terms <= 0:
        print("Please enter a positive number of terms.")
    else:
        first = 0
        second = 1
        series = []

        for _ in range(terms):
            series.append(str(first))
            first, second = second, first + second

        print("Fibonacci series:", " ".join(series))
