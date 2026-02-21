# Division by zero example
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Value error example
try:
    number = int("hello")
except ValueError:
    print("Invalid number.")

# try-except-else example
try:
    value = int("25")
except ValueError:
    print("Conversion failed.")
else:
    print("Conversion successful:", value)

# try-except-finally example
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Done.")
