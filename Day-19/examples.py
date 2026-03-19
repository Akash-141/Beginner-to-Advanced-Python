print("Day 19: Sets Examples")

numbers = {1, 2, 3, 4}
print(numbers)

numbers = set([1, 2, 3, 4])
print(numbers)

values = {1, 2, 2, 3, 3, 4}
print(values)

colors = {"red", "green", "blue"}
print(colors)

fruits = {"apple", "banana", "mango"}
print("apple" in fruits)
print("grape" in fruits)

animals = {"cat", "dog", "tiger"}
for animal in animals:
    print(animal)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2
print(result)

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1 & set2
print(result)

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1 - set2
print(result)

languages = {"Python", "Java", "C++"}
print(languages)

numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)

fruits = {"apple", "banana", "orange"}
if "apple" in fruits:
    print("Apple is in the set")

colors = {"red", "blue", "green"}
for color in colors:
    print(color)

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a & b)
print(a - b)

numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)

allowed_users = {"alice", "bob", "charlie"}
username = "alice"
if username in allowed_users:
    print("Access granted")

data = [1, 2, 2, 3, 4, 4, 5]
unique_data = list(set(data))
print(unique_data)

print("End of Day 19 examples")
