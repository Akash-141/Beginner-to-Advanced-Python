# Day 9: Type Casting

## 1. Definition of the Topic

**Type casting** (also called type conversion) is the process of converting one data type into another.

In Python, type casting allows you to change the type of a variable explicitly using built-in functions like:

- int()
- float()
- str()
- bool()
- list()
- tuple()
- set()

Python is a dynamically typed language, but sometimes we must manually convert types to perform correct operations.

---

## 2. Detailed Explanation of the Topic

Python automatically assigns data types to variables, but it does NOT automatically convert incompatible types during operations.

Example:

num = "10"
# print(num + 5)  # This will cause an error

Why? Because "10" is a string, and 5 is an integer.

To fix this, we use type casting:

num = "10"
converted_num = int(num)
print(converted_num + 5)

---

### 2.1 Converting to Integer

x = 5.9
print(int(x))  # Removes decimal part

Converting string to integer:

age = "21"
print(int(age))

Invalid conversion example:

# print(int("hello"))  # ValueError

---

### 2.2 Converting to Float

num2 = 10
print(float(num2))

price = "19.99"
print(float(price))

---

### 2.3 Converting to String

number = 100
print(str(number))

Useful in concatenation:

age2 = 25
print("I am " + str(age2) + " years old")

---

### 2.4 Converting to Boolean

In Python:

- 0, 0.0, "", None → False
- Everything else → True

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))

---

### 2.5 Converting Between Collections

numbers = [1, 2, 3, 3]
print(set(numbers))  # Removes duplicates

text = "hello"
print(list(text))

values = (1, 2, 3)
print(list(values))

---

## 3. Do's and Don'ts

### Do's

- Always check the original data type before casting
- Use int() or float() when taking numeric input
- Use str() when combining numbers with text
- Handle potential errors using try-except
- Understand how boolean conversion works

### Don'ts

- Do NOT assume string numbers behave like integers
- Do NOT cast invalid strings to numbers
- Do NOT ignore possible ValueError exceptions
- Do NOT overuse casting unnecessarily

---

## 4. Industry Standards

Professional developers:

- Validate input before casting
- Use try-except for safe conversions
- Avoid unnecessary type conversions
- Write readable conversion logic

Example with validation:

user_input = "25"

try:
    age3 = int(user_input)
    print(f"Next year you will be {age3 + 1}")
except ValueError:
    print("Invalid input. Please enter a number.")

---

## 5. Mistakes to Avoid

### 5.1 Forgetting That input() Returns String

age = input("Enter age: ")
# print(age + 1)  # Error

Correct:

age = int(input("Enter age: "))
print(age + 1)

---

### 5.2 Invalid Numeric Conversion

# int("12.5")  # ValueError

Correct:

print(int(float("12.5")))

---

### 5.3 Misunderstanding Boolean Conversion

print(bool("False"))  # True because non-empty string

---

## 6. Summary

Today you learned:

- What type casting is
- Why type conversion is necessary
- How to use int(), float(), str(), bool()
- How to convert between collections
- Common beginner mistakes
- Industry-level best practices

Type casting is essential for handling user input, data processing, and real-world Python applications.

Next topic: [Conditional statements (if, else)](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-10/notes.md)

