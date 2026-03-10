print("Day 14: For Loop Examples")

# Example 1: Basic for loop
for i in range(5):
    print(i)


# Example 2: Iterating over a list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# Example 3: Iterating over a string
word = "python"

for letter in word:
    print(letter)


# Example 4: Using break
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)


# Example 5: Using continue
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue
    print(num)


# Example 6: Range with start and stop
for i in range(1, 6):
    print(i)


# Example 7: enumerate
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# Good practice example
students = ["Alice", "Bob", "Charlie"]

for student in students:
    print(student)


# Pythonic iteration
items = ["a", "b", "c"]

for item in items:
    print(item)


# enumerate usage
for index, item in enumerate(items):
    print(index, item)

print("End of Day 14 examples")
