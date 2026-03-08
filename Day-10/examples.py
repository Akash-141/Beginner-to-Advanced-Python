print("Day 10: Conditional Statements Examples")

# Basic if
age = 18
if age >= 18:
    print("You are eligible to vote")

# if-else example
age = 16
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# elif example
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

# Comparison operator example
num = 10
if num == 10:
    print("Number is ten")

# Logical operators example
age = 20
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# Nested if example
age = 22
citizen = True
if age >= 18:
    if citizen:
        print("Eligible to vote")

# Ternary operator example
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# Early return function example
def check_even(number):
    if number % 2 != 0:
        return "Odd"
    return "Even"

print(check_even(4))

# Range comparison example
age = 30
if 18 <= age < 60:
    print("Working age")

print("End of Day 10 examples")
