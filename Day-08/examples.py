print("Day 8: Comments and Code Readability Examples")

# Single-line comment
print("Hello, Python")

# Inline comment example
x = 10  # store the value 10 in x
print(x)

# Docstring example
"""
This program calculates the area of a rectangle.
It takes length and width as input.
"""
length = 5
width = 3
print(length * width)

# Poor readability example
a = 5
b = 10
c = a + b
print(c)

# Improved readability example
first_number = 5
second_number = 10
total_sum = first_number + second_number
print(total_sum)

# Good spacing example
result = (5 + 3) * 2
print(result)

# Function with docstring
def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width

print(calculate_area(5, 3))

# Loop readability example
for i in range(10):
    print(i)

print("End of Day 8 examples")
