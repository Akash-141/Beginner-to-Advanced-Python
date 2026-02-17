# Creating a list
numbers = [5, 10, 15, 20, 25]

# Accessing items
print(numbers[0])
print(numbers[-1])

# Modifying an item
numbers[2] = 100
print(numbers)

# Adding items
numbers.append(30)
numbers.insert(1, 7)
print(numbers)

# Removing items
numbers.remove(7)
numbers.pop(0)
print(numbers)

# Looping through the list
for num in numbers:
    print(num)

# Length of the list
print(len(numbers))
