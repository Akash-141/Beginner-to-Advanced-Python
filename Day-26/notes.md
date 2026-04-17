# Day 26: Lambda Functions

## 1. Definition of the Topic

A lambda function is a small anonymous function in Python defined using the `lambda` keyword.

It can take any number of arguments but can only have one expression.

Official documentation:
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

---

## 2. Detailed Explanation of the Topic

### Basic Syntax

```python
lambda arguments: expression
```

Example:

```python
add = lambda a, b: a + b
print(add(2, 3))
```

---

### Lambda with Multiple Arguments

```python
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))
```

---

### Lambda Inside Functions

```python
def apply(func, value):
    return func(value)

result = apply(lambda x: x * 2, 5)
print(result)
```

---

### Using Lambda with map()

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)
```

---

### Using Lambda with filter()

```python
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
```

---

### Using Lambda with sorted()

```python
pairs = [(1, 2), (3, 1), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)
```

---

## 3. Easy Short Code Examples

### Example 1: Simple Lambda

```python
square = lambda x: x * x
print(square(5))
```

---

### Example 2: Lambda with Two Inputs

```python
add = lambda a, b: a + b
print(add(10, 20))
```

---

### Example 3: Lambda with map()

```python
nums = [1, 2, 3]
result = list(map(lambda x: x + 1, nums))
print(result)
```

---

### Example 4: Lambda with filter()

```python
nums = [1, 2, 3, 4]
result = list(filter(lambda x: x > 2, nums))
print(result)
```

---

### Example 5: Lambda with sorted()

```python
data = [(1, 3), (2, 1), (4, 2)]
result = sorted(data, key=lambda x: x[1])
print(result)
```

---

## 4. Do's and Don'ts

### Do's

- Use lambda for short, simple operations
- Use lambda with functions like map, filter, sorted
- Keep lambda expressions concise

### Don'ts

- Do not write complex logic inside lambda
- Do not replace all functions with lambda
- Do not sacrifice readability

---

## 5. Industry Standards

### Use Lambda for Small Tasks

```python
numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers))
```

---

### Prefer Readability

```python
# Good
square = lambda x: x * x

# Better for complex logic
def square_func(x):
    return x * x
```

---

## 6. Mistakes to Avoid

### Overcomplicated Lambda

```python
# Avoid
func = lambda x: (x**2 + 2*x + 1) / (x + 1)
```

---

### Using Lambda Where def is Better

```python
# Not recommended
complex_func = lambda x: x**2 + x + 10
```

---

### Forgetting Lambda is Single Expression

```python
# This will cause error
# lambda x: x = x + 1
```

---

## Summary

- Lambda functions are anonymous, short functions
- Best used for simple operations
- Commonly used with map, filter, and sorted
- Avoid complex logic in lambda

Next topic: [Basic error handling](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-27/notes.md)
