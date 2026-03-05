print("Day 9: Type Casting Examples")

# String + Integer error example (commented to avoid crash)
num = "10"
# print(num + 5)

# Correct conversion
converted_num = int(num)
print(converted_num + 5)

# Float to int
x = 5.9
print(int(x))

# String to int
age = "21"
print(int(age))

# Int to float
num2 = 10
print(float(num2))

# String to float
price = "19.99"
print(float(price))

# Int to string
number = 100
print(str(number))

# String concatenation with conversion
age2 = 25
print("I am " + str(age2) + " years old")

# Boolean conversions
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))

# List to set
numbers = [1, 2, 3, 3]
print(set(numbers))

# String to list
text = "hello"
print(list(text))

# Tuple to list
values = (1, 2, 3)
print(list(values))

# Safe conversion with try-except
user_input = "25"
try:
    age3 = int(user_input)
    print(f"Next year you will be {age3 + 1}")
except ValueError:
    print("Invalid input. Please enter a number.")

# Fixing float string conversion
print(int(float("12.5")))

# Boolean string example
print(bool("False"))

print("End of Day 9 examples")
