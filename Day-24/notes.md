
# Day 24: Function Arguments and Return Values

## 1. Definition of the Topic

Function arguments are values passed into a function when it is called, and return values are the results that a function sends back after execution.

They allow functions to be dynamic, reusable, and flexible.

Official documentation:
https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions

---

## 2. Detailed Explanation of the Topic

### Positional Arguments

Arguments are passed in order.

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

---

### Keyword Arguments

Arguments are passed using parameter names.

```python
def greet(name, age):
    print(name, age)

greet(age=20, name="Alice")
```

---

### Default Arguments

Provide default values if no argument is given.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Bob")
```

---

### Arbitrary Arguments (*args)

Used when the number of arguments is unknown.

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))
```

---

### Keyword Arbitrary Arguments (**kwargs)

Accepts multiple key-value pairs.

```python
def show_info(**data):
    print(data)

show_info(name="Alice", age=20)
```

---

### Return Values

Functions return values using the return keyword.

```python
def square(n):
    return n * n

result = square(4)
print(result)
```

---

### Multiple Return Values

```python
def get_values():
    return 1, 2, 3

a, b, c = get_values()
print(a, b, c)
```

---

## 3. Easy Short Code Examples

### Example 1: Positional Argument

```python
def multiply(a, b):
    return a * b

print(multiply(3, 4))
```

### Example 2: Keyword Argument

```python
def display(name, age):
    print(name, age)

display(age=25, name="John")
```

### Example 3: Default Argument

```python
def welcome(name="User"):
    print("Welcome", name)

welcome()
```

### Example 4: *args

```python
def add_all(*nums):
    return sum(nums)

print(add_all(1, 2, 3))
```

### Example 5: Return Multiple Values

```python
def calc(a, b):
    return a + b, a * b

s, p = calc(2, 3)
print(s, p)
```

---

## 4. Do's and Don'ts

### Do's

- Use default arguments for optional values
- Use *args when number of inputs is unknown
- Use **kwargs for flexible keyword data
- Always return values when needed

### Don'ts

- Do not mix argument types incorrectly
- Do not forget return statements
- Do not overuse *args unnecessarily

---

## 5. Industry Standards

### Clear Function Design

```python
def calculate_total(price, tax=0.1):
    return price + (price * tax)
```

---

### Use of *args and **kwargs

```python
def log_data(*args, **kwargs):
    print(args)
    print(kwargs)
```

---

### Readable Function Calls

```python
def create_user(name, age):
    print(name, age)

create_user(name="Alice", age=25)
```

---

## 6. Mistakes to Avoid

### Missing Arguments

```python
def greet(name):
    print(name)

# greet()
```

---

### Wrong Order of Arguments

```python
def func(a, b):
    print(a, b)

# func(b=2, 1)
```

---

### Forgetting Return

```python
def add(a, b):
    a + b

print(add(2, 3))
```

---

## Summary

- Arguments make functions flexible
- Return values provide output
- Understanding argument types is essential for real-world coding

Next topic: [Scope and Lifetime of Variables](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-25/notes.md)

