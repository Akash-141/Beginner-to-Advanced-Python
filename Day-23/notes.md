
# Day 23: Functions in Python

## 1. Definition of the Topic

A function in Python is a reusable block of code that performs a specific task. Functions help organize code, reduce repetition, and improve readability.

Functions are defined using the 'def' keyword.

Official documentation:
https://docs.python.org/3/tutorial/controlflow.html#defining-functions

---

## 2. Detailed Explanation of the Topic

### Basic Syntax

```python
def function_name():
    pass
```

### Calling a Function

```python
def greet():
    print("Hello!")

greet()
```

### Parameters

```python
def greet(name):
    print("Hello", name)

greet("Alice")
```

### Return Values

```python
def add(a, b):
    return a + b

print(add(5, 3))
```

### Default Parameters

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Bob")
```

### Scope

```python
def show():
    x = 10
    print(x)

show()
```

---

## 3. Easy Short Code Examples

```python
def say_hello():
    print("Hello World")

say_hello()

def square(num):
    print(num * num)

square(5)

def subtract(a, b):
    return a - b

print(subtract(10, 5))

def welcome(name="User"):
    print("Welcome", name)

welcome()

def double(n):
    return n * 2

numbers = [1, 2, 3]
for num in numbers:
    print(double(num))
```

---

## 4. Do's and Don'ts

### Do's
- Use functions to avoid repetition
- Use meaningful names
- Keep functions small

### Don'ts
- Avoid large functions
- Avoid unclear names
- Do not ignore return values

---

## 5. Industry Standards

```python
def calculate_area(radius):
    return 3.14 * radius * radius
```

- Use snake_case naming
- Write reusable functions

---

## 6. Mistakes to Avoid

```python
def greet():
    print("Hello")

# greet() not called
```

```python
def add(a, b):
    a + b

print(add(2, 3))
```

```python
def greet(name):
    print(name)

# greet()
```

---

## Summary

- Functions improve code structure
- They make code reusable
- They are essential for clean programming

Next topic: [Function arguments and return values]()
