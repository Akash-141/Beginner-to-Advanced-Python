
print("Day 22: Basic Problem Solving with Collections")

# Sum using list
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)

# Remove duplicates using set
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)

# Counting using dictionary
text = "apple banana apple"
words = text.split()
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)

# Tuple usage
point = (10, 20)
print(point[0], point[1])

# Combine collections
numbers = [1, 2, 2, 3, 4]
unique = set(numbers)
result = list(unique)
print(result)

# Find max
numbers = [10, 20, 30, 5]
print(max(numbers))

# Remove duplicates example
data = [1, 1, 2, 3, 3]
print(list(set(data)))

# Frequency count
items = ["a", "b", "a", "c", "b", "a"]
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
print(freq)

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)

# Membership check
names = {"Alice", "Bob", "Charlie"}
print("Alice" in names)

print("End of Day 22 examples")
