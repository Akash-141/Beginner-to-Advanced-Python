# Day 25: Scope and Lifetime of Variables

## 1. Definition of the Topic

Scope refers to the region of a program where a variable is accessible.

Lifetime refers to the duration for which a variable exists in memory during program execution.

Understanding these concepts helps write clean, predictable, and maintainable Python code.

Official documentation:
https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

---

## 2. Detailed Explanation of the Topic

### Local Scope

Variables defined inside a function are accessible only within that function.

```python
def my_function():
    x = 10
    print(x)

my_function()
# print(x)  # This will cause an error
```

---

### Global Scope

Variables defined outside functions can be accessed anywhere in the program.

```python
x = 20

def show():
    print(x)

show()
print(x)
```

---

### Enclosing Scope (Nested Functions)

Variables in an outer function are accessible inside inner functions.

```python
def outer():
    x = "outer"

    def inner():
        print(x)

    inner()

outer()
```

---

### The global Keyword

Used to modify a global variable inside a function.

```python
x = 5

def change():
    global x
    x = 10

change()
print(x)
```

---

### The nonlocal Keyword

Used to modify variables in the enclosing (outer) function.

```python
def outer():
    x = 5

    def inner():
        nonlocal x
        x = 10

    inner()
    print(x)

outer()
```

---

### Lifetime of Variables

- Local variables exist only during function execution.
- Global variables exist throughout the program execution.

```python
def test():
    x = 100
    print(x)

test()
# x is destroyed after function execution
```

---

## 3. Easy Short Code Examples

### Example 1: Local Scope

```python
def func():
    a = 1
    print(a)

func()
```

---

### Example 2: Global Scope

```python
b = 2

def func():
    print(b)

func()
```

---

### Example 3: Using global

```python
c = 3

def update():
    global c
    c = 4

update()
print(c)
```

---

### Example 4: Using nonlocal

```python
def outer():
    d = 5

    def inner():
        nonlocal d
        d = 6

    inner()
    print(d)

outer()
```

---

### Example 5: Lifetime Example

```python
def temp():
    x = 50
    print(x)

temp()
```

---

## 4. Do's and Don'ts

### Do's

- Use local variables whenever possible
- Keep scope limited for clarity
- Use global only when absolutely necessary
- Use nonlocal carefully in nested functions

### Don'ts

- Do not overuse global variables
- Do not modify global variables without reason
- Do not reuse variable names across scopes unnecessarily
- Do not ignore scope rules

---

## 5. Industry Standards

### Prefer Local Scope

```python
def calculate():
    result = 10 + 20
    return result
```

---

### Avoid Global State

```python
# Not recommended
count = 0

def increment():
    global count
    count += 1
```

---

### Controlled Scope Usage

```python
def outer():
    value = 10

    def inner():
        return value + 5

    return inner()
```

---

## 6. Mistakes to Avoid

### Accessing Local Variables Outside Scope

```python
def func():
    x = 10

# print(x)
```

---

### Forgetting global Keyword

```python
x = 5

def change():
    x = 10  # creates a new local variable

change()
print(x)
```

---

### Incorrect nonlocal Usage

```python
def outer():
    x = 5

    def inner():
        # nonlocal y  # Error: y does not exist
        pass
```

---

## Summary

- Scope defines where variables can be accessed
- Lifetime defines how long variables exist
- Prefer local variables for safer and cleaner code
- Use global and nonlocal only when necessary

Next topic: [Lambda functions]()

