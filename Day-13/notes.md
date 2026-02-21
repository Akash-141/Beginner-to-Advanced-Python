# Day 13: Exception Handling in Python

## 1. What Are Exceptions?

An exception is an error that occurs during program execution.

If not handled, the program will stop.

Official documentation:
https://docs.python.org/3/tutorial/errors.html

---

## 2. Basic try and except

Use try to test a block of code.
Use except to handle errors.

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input!")
```

---

## 3. Handling Specific Exceptions

It is better to catch specific errors.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

Another example:

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid number format.")
```

---

## 4. Using else

The else block runs if no exception occurs.

```python
try:
    number = int("10")
except ValueError:
    print("Error")
else:
    print("Conversion successful:", number)
```

---

## 5. Using finally

The finally block always runs.

```python
try:
    file = open("sample.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution finished.")
```

---

## 6. Why Use Exception Handling?

- Prevent program crashes
- Handle user input safely
- Improve program reliability

---

## Practice Tasks

1. Handle division by zero.
2. Handle invalid integer input.
3. Use try, except, else together.
4. Add a finally block.
5. Catch FileNotFoundError.

---

## What You Learned Today

- What exceptions are
- try and except
- Handling specific errors
- else block
- finally block
