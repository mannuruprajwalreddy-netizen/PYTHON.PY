# Generate a Random OTP
# This program generates a random 4-digit or 6-digit numeric OTP.

import random

try:
    number_of_digits = int(input("Enter OTP length (4 or 6): "))
except ValueError:
    print("Please enter 4 or 6.")
else:
    if number_of_digits not in (4, 6):
        print("OTP length must be 4 or 6.")
    else:
        first_digit = random.randint(1, 9)
        remaining_digits = "".join(
            str(random.randint(0, 9)) for _ in range(number_of_digits - 1)
        )
        otp = str(first_digit) + remaining_digits
        print("Your OTP is:", otp)
