
print("Day 23: Functions Examples")

def greet():
    print("Hello!")

greet()

def greet(name):
    print("Hello", name)

greet("Alice")

def add(a, b):
    return a + b

print(add(5, 3))

def greet_default(name="Guest"):
    print("Hello", name)

greet_default()
greet_default("Bob")

def show():
    x = 10
    print(x)

show()

def say_hello():
    print("Hello World")

say_hello()

def square(num):
    print(num * num)

square(5)

def subtract(a, b):
    return a - b

print(subtract(10, 5))

def welcome(name="User"):
    print("Welcome", name)

welcome()

def double(n):
    return n * 2

numbers = [1, 2, 3]
for num in numbers:
    print(double(num))

print("End of Day 23 examples")
