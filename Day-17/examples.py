
print("Day 17: List Methods Examples")

# append()
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

# extend()
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)

# insert()
fruits = ["apple", "banana"]
fruits.insert(1, "mango")
print(fruits)

# remove()
items = ["pen", "book", "eraser"]
items.remove("book")
print(items)

# pop()
numbers = [10, 20, 30]
last_item = numbers.pop()
print(last_item)
print(numbers)

# clear()
data = [1, 2, 3]
data.clear()
print(data)

# index()
fruits = ["apple", "banana", "mango"]
print(fruits.index("banana"))

# count()
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))

# sort()
numbers = [5, 1, 4, 2]
numbers.sort()
print(numbers)

# reverse()
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)

# copy()
original = [1, 2, 3]
duplicate = original.copy()
print(duplicate)

print("End of Day 17 examples")
