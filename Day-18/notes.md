# Day 18: Python Decorators and Generators

## 1. What is a Decorator?
A decorator is a function that modifies or enhances another function without changing its code directly.

### Basic Syntax
```python
def decorator_function(original_function):
    def wrapper():
        print("Before the function runs")
        original_function()
        print("After the function runs")
    return wrapper
```

## 2. Using the @decorator Syntax
```python
@decorator_function
def display():
    print("Hello")
```

## 3. Decorators with Arguments
Decorators can accept and pass arguments using *args and **kwargs.

## 4. What is a Generator?
A generator is a function that returns values one at a time using the `yield` keyword instead of `return`.

### Example
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
```

## 5. Generator vs Normal Function
- Generators use less memory
- They produce values lazily
- Useful for large datasets

## 6. When to Use Generators
- Reading large files
- Infinite sequences
- Streaming data processing
