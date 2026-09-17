# Check Whether a Number is Prime or Not Prime
# A prime number has exactly two factors: 1 and itself.

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    is_prime = number >= 2

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
