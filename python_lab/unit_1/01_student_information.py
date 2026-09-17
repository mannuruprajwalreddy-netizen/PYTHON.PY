# Student Information and Academic Summary
# This program reads student details and calculates the total, average,
# and result from three subject marks.

print("Student Information and Academic Summary")

name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
course = input("Enter course: ")

try:
    mark_1 = float(input("Enter marks for subject 1: "))
    mark_2 = float(input("Enter marks for subject 2: "))
    mark_3 = float(input("Enter marks for subject 3: "))
except ValueError:
    print("Please enter valid numbers for the marks.")
else:
    total = mark_1 + mark_2 + mark_3
    average = total / 3
    result = "Pass" if mark_1 >= 35 and mark_2 >= 35 and mark_3 >= 35 else "Fail"

    print("\nStudent Summary")
    print("Name:", name)
    print("Roll number:", roll_number)
    print("Course:", course)
    print("Total marks:", total)
    print("Average marks:", format(average, ".2f"))
    print("Result:", result)
