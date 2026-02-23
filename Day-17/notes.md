# Day 17: Exception Handling in Python

## 1. What is an Exception?

An exception is an error that occurs during program execution.
If not handled, it stops the program.

Official documentation:
https://docs.python.org/3/tutorial/errors.html

---

## 2. Basic Try and Except

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except:
    print("An error occurred.")
```

---

## 3. Handling Specific Exceptions

It is better to catch specific errors.

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
```

---

## 4. Using Else

The else block runs if no exceptions occur.

```python
try:
    x = int("5")
except ValueError:
    print("Conversion failed.")
else:
    print("Conversion successful:", x)
```

---

## 5. Using Finally

The finally block always runs.

```python
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")
```

---

## Practice Tasks

1. Write a program that handles division by zero.
2. Handle invalid user input using ValueError.
3. Use else to print a success message.
4. Use finally to print a completion message.
5. Try catching multiple exception types.

---

## What You Learned Today

- What exceptions are
- try and except
- Catching specific errors
- else block
- finally block
