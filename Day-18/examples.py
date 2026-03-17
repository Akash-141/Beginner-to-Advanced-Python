
print("Day 18: Tuple Examples")

# Creating a tuple
numbers = (10, 20, 30)
print(numbers)

# Tuple with multiple data types
data = (10, "Python", 3.14, True)
print(data)

# Accessing tuple elements
fruits = ("apple", "banana", "mango")
print(fruits[0])
print(fruits[2])

# Negative indexing
print(fruits[-1])

# Tuple length
items = ("pen", "book", "eraser")
print(len(items))

# Nested tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6)
)

print(matrix[0])
print(matrix[1][2])

# Iterating through a tuple
numbers = (10, 20, 30)
for number in numbers:
    print(number)

# Tuple packing and unpacking
person = ("Alice", 25, "Engineer")

name, age, profession = person

print(name)
print(age)
print(profession)

# Tuple for coordinates
coordinates = (10.5, 20.3)
print(coordinates)

# Tuple unpacking example
point = (5, 10)
x, y = point
print(x)
print(y)

print("End of Day 18 examples")
