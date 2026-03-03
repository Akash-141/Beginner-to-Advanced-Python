# Day 7: Input and Output

## 1. Definition of the Topic

**Input** in Python refers to receiving data from the user, a file, or another source.

**Output** refers to displaying or sending data to the user, screen, or another destination.

In beginner-level Python, input and output are primarily handled using:

- `input()` → for receiving user input
- `print()` → for displaying output

Official reference:
https://docs.python.org/3/library/functions.html

---

## 2. Detailed Explanation of the Topic

Input and output (I/O) are fundamental concepts in programming. Without input and output, programs cannot interact with users.

### 2.1 Output Using print()

The `print()` function displays information to the screen.

```python
print("Hello, World")
```

You can print multiple values:

```python
name = "Akash"
age = 21
print("Name:", name, "Age:", age)
```

You can control formatting using:

- `sep` → separator between values
- `end` → what prints at the end

```python
print("Python", "Java", "C++", sep=" | ")
print("Hello", end=" ")
print("World")
```

---

### 2.2 Input Using input()

The `input()` function takes user input as a string.

```python
name = input("Enter your name: ")
print("Hello", name)
```

Important: `input()` always returns a string.

---

### 2.3 Converting Input Data Types

If you need numbers, you must convert input manually.

```python
age = input("Enter your age: ")
age = int(age)
print("Next year you will be", age + 1)
```

Shorter version:

```python
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)
```

---

### 2.4 Taking Multiple Inputs

```python
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum:", x + y)
```

---

### 2.5 Formatted Output (f-strings)

```python
name = "Akash"
score = 95
print(f"{name} scored {score} marks")
```

---

## 3. Do's and Don'ts

### Do's

- Always convert input when expecting numbers
- Use clear prompts inside input()
- Use f-strings for clean formatting
- Validate input when possible
- Keep output readable

### Don'ts

- Do NOT assume input is numeric
- Do NOT forget type conversion
- Do NOT make prompts unclear
- Do NOT print messy, unreadable output
- Do NOT ignore user experience

---

## 4. Industry Standards

Professional Python code:

- Uses f-strings for formatting (Python 3.6+)
- Validates user input
- Handles errors using try-except
- Keeps prompts user-friendly
- Separates input logic from business logic

Example with basic validation:

```python
try:
    age = int(input("Enter your age: "))
    print(f"Next year you will be {age + 1}")
except ValueError:
    print("Please enter a valid number")
```

PEP 8 reference:
https://peps.python.org/pep-0008/

---

## 5. Mistakes to Avoid

### 5.1 Forgetting Type Conversion

```python
age = input("Enter age: ")
# print(age + 1)  # TypeError
```

---

### 5.2 Not Handling Invalid Input

```python
age = int(input("Enter age: "))  # Crashes if user enters text
```

---

### 5.3 Poor Formatting

```python
name = "Akash"
age = 21
print(name, age)
```

Better:

```python
print(f"My name is {name} and I am {age} years old")
```

---

## 6. Summary

Today you learned:

- What input and output mean
- How to use print()
- How to use input()
- Why input returns string
- How to convert data types
- How to format output professionally
- Common beginner mistakes

Next topic: [Comments and Code Readability]()
