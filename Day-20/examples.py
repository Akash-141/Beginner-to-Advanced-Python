# Day 20 Examples: Modules and Packages

# ---------- Using built-in module ----------
import math

print("Square root of 36:", math.sqrt(36))
print("Value of pi:", math.pi)


# ---------- Import specific function ----------
from math import factorial

print("Factorial of 5:", factorial(5))


# ---------- Alias import ----------
import math as m

print("Cos(0):", m.cos(0))


# ---------- Demonstrating __name__ ----------
def demo_function():
    print("This is inside demo_function")

if __name__ == "__main__":
    print("This file is being run directly")
    demo_function()
