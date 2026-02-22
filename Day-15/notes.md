# Day 15: Modules and Imports in Python

## 1. What is a Module?

A module is a file containing Python code (functions, variables, classes) that you can reuse in other programs.

Python has built-in modules and you can also create your own.

Official documentation:
https://docs.python.org/3/tutorial/modules.html

---

## 2. Importing a Module

Use the import keyword.

```python
import math

print(math.sqrt(16))
```

---

## 3. Import Specific Items

You can import specific functions from a module.

```python
from math import sqrt

print(sqrt(25))
```

---

## 4. Using Aliases

You can rename a module using as.

```python
import math as m

print(m.pi)
```

---

## 5. Creating Your Own Module

Create a file called mymodule.py:

```python
def greet(name):
    return "Hello " + name
```

Then use it in another file:

```python
import mymodule

print(mymodule.greet("Alice"))
```

---

## 6. The dir() Function

Use dir() to see available attributes in a module.

```python
import math
print(dir(math))
```

---

## Practice Tasks

1. Import the math module and print the value of pi.
2. Import sqrt directly and use it.
3. Use an alias for a module.
4. Create your own module with one function.
5. Import and use your custom module.

---

## What You Learned Today

- What modules are
- import statement
- from ... import ...
- Using aliases
- Creating your own module
- dir() function
