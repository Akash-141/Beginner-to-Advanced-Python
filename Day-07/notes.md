# Day 7: Input and Output

## 1. What is Input and Output?

**Input** in Python means receiving data from the user, a file, or another source.

**Output** means displaying or sending data to the user, the screen, a file, or another destination.

In beginner-level Python, input and output are primarily handled using two built-in functions:

- `input()` → for receiving user input
- `print()` → for displaying output

These two functions form the foundation of interactive programs.

Official reference:  
https://docs.python.org/3/library/functions.html

---

## 2. Why Input and Output Matter

Input and output (I/O) are fundamental concepts in programming. Without them, programs cannot interact with users.

Almost every real-world application needs I/O:

- Asking the user for their name, age, or preferences
- Showing results, messages, or calculations
- Reading data from files or APIs (advanced)
- Writing logs or reports

Mastering `input()` and `print()` is the first step toward building interactive programs.

---

## 3. Output Using `print()`

The `print()` function displays information on the screen.

### 3.1 Basic Printing

```python
print("Hello, World")
```

### 3.2 Printing Multiple Values

You can print several values at once. By default, they are separated by a space:

```python
name = "Akash"
age = 21
print("Name:", name, "Age:", age)
```

### 3.3 Controlling the Separator and Ending

The `print()` function has two useful parameters:

- `sep` → controls what is placed between values (default is a space)
- `end` → controls what is printed at the end (default is a newline `\n`)

```python
print("Python", "Java", "C++", sep=" | ")
# Output: Python | Java | C++

print("Hello", end=" ")
print("World")
# Output: Hello World
```

### 3.4 Printing Empty Lines

```python
print()          # prints a blank line
print("Next line")
```

---

## 4. Input Using `input()`

The `input()` function pauses the program and waits for the user to type something, then presses Enter.

### 4.1 Basic Input

```python
name = input("Enter your name: ")
print("Hello", name)
```

**Very important:**  
`input()` **always returns a string**, even if the user types a number.

### 4.2 Why Input is Always a String

```python
age = input("Enter your age: ")
print(type(age))          # <class 'str'>
```

If you try to do math directly with the input, you will get an error unless you convert it first.

---

## 5. Converting Input Data Types

When you need a number, you must convert the input using `int()` or `float()`.

### 5.1 Converting to Integer

```python
age = input("Enter your age: ")
age = int(age)
print("Next year you will be", age + 1)
```

### 5.2 Shorter and Cleaner Version

```python
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)
```

### 5.3 Converting to Float

```python
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters")
```

---

## 6. Taking Multiple Inputs

You can ask for several values one after another:

```python
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum:", x + y)
```

You can also take multiple values in a single line (more advanced):

```python
a, b = input("Enter two numbers separated by space: ").split()
a = int(a)
b = int(b)
print("Sum:", a + b)
```

---

## 7. Formatted Output (f-strings)

The cleanest and most modern way to format output is using **f-strings** (available since Python 3.6).

```python
name = "Akash"
score = 95
print(f"{name} scored {score} marks")
```

You can also perform calculations inside f-strings:

```python
print(f"Next year you will be {age + 1}")
```

Other older methods still work but are less preferred:

```python
print("{} scored {} marks".format(name, score))
print("%s scored %d marks" % (name, score))
```

---

## 8. Do’s and Don’ts

### Do’s

- Always convert input when you expect a number (`int()` or `float()`)
- Write clear and friendly prompts inside `input()`
- Prefer f-strings for clean and readable output
- Validate user input when possible
- Keep output neat and easy to understand
- Use `sep` and `end` when you need special formatting

### Don’ts

- Do **not** assume that input is already a number
- Do **not** forget type conversion
- Do **not** write unclear or incomplete prompts
- Do **not** produce messy or hard-to-read output
- Do **not** ignore the user experience
- Do **not** crash the program when the user types invalid data

---

## 9. Industry Standards and Best Practices

Professional Python code usually:

- Uses **f-strings** for formatting (Python 3.6+)
- Validates user input
- Handles errors gracefully with `try-except`
- Keeps prompts user-friendly and clear
- Separates input logic from the main business logic

### Example with Basic Validation

```python
try:
    age = int(input("Enter your age: "))
    print(f"Next year you will be {age + 1}")
except ValueError:
    print("Please enter a valid number")
```

This prevents the program from crashing if the user types text instead of a number.

PEP 8 reference:  
https://peps.python.org/pep-0008/

---

## 10. Common Mistakes to Avoid

### 10.1 Forgetting Type Conversion

```python
age = input("Enter age: ")
# print(age + 1)          # TypeError: can only concatenate str to str
print(int(age) + 1)       # Correct
```

### 10.2 Not Handling Invalid Input

```python
age = int(input("Enter age: "))   # Crashes if user types "twenty"
```

Always consider using `try-except` for safer programs.

### 10.3 Poor Formatting

```python
name = "Akash"
age = 21
print(name, age)                  # Less readable
```

Better:

```python
print(f"My name is {name} and I am {age} years old")
```

### 10.4 Unclear Prompts

```python
x = input()                       # User doesn’t know what to enter
```

Better:

```python
x = input("Enter a number: ")
```

---

## 11. Practice Tasks

1. Ask the user for their name and greet them using an f-string.
2. Ask for two numbers, convert them to integers, and print their sum, difference, and product.
3. Ask for the user’s age and print how old they will be in 10 years.
4. Use `sep` and `end` to create a specially formatted line of output.
5. Write a small program that asks for a float value (e.g., height or price) and displays it nicely.
6. Add basic error handling with `try-except` so the program does not crash on invalid input.

---

## 12. What You Learned Today

- What input and output mean in programming
- How to use the `print()` function effectively (including `sep` and `end`)
- How to use the `input()` function
- Why `input()` always returns a string
- How to convert input to integers or floats
- How to take multiple inputs
- How to format output professionally with f-strings
- Best practices and common beginner mistakes
- Basic input validation with `try-except`

Next topic: [Comments and Code Readability](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-08/notes.md)
