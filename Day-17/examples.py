# Example 1: Division handling
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Operation successful.")
finally:
    print("Done.")

# Example 2: File handling exception
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("The file does not exist.")
