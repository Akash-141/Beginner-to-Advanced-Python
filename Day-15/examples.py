
print("Day 15: Loop Control Statements Examples")

# break example
for number in range(1, 10):
    if number == 5:
        break
    print(number)

# continue example
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# pass example
for number in range(5):
    if number == 2:
        pass
    print(number)

# break inside a while loop
count = 1
while True:
    print(count)
    if count == 5:
        break
    count += 1

# searching for a value
numbers = [10, 25, 30, 45, 50]

for num in numbers:
    if num == 30:
        print("Number found")
        break

# skipping invalid data
numbers = [5, -2, 8, -1, 10]

for num in numbers:
    if num < 0:
        continue
    print(num)

# efficient search example
items = ["apple", "banana", "mango"]

for item in items:
    if item == "banana":
        print("Item found")
        break

# filtering odd numbers
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

print("End of Day 15 examples")
