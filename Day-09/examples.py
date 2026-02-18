# Simple function
def greet():
    print("Hello!")

greet()

# Function with parameter
def greet_user(name):
    print("Hi", name)

greet_user("Alice")

# Function with return
def add(a, b):
    return a + b

print(add(10, 5))

# Multiply function
def multiply(x, y):
    return x * y

print(multiply(3, 4))

# Even check function
def is_even(number):
    return number % 2 == 0

print(is_even(6))
print(is_even(7))
