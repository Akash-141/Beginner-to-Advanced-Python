# Day 20: Python Modules and Packages

## 1. What is a Module?
A module is simply a Python file that contains functions, variables, or classes that you can reuse in other programs.

Example:
If you create a file named `math_utils.py`, it becomes a module.

Why modules are useful:
- Code reuse
- Better organization
- Easier maintenance

---

## 2. Importing Modules

### Import the whole module
```python
import math
print(math.sqrt(16))
```

### Import specific items
```python
from math import sqrt
print(sqrt(25))
```

### Import with alias
```python
import math as m
print(m.pi)
```

---

## 3. Creating Your Own Module

Create a file named `my_module.py`:

```python
def greet(name):
    return f"Hello, {name}!"
```

Use it in another file:

```python
import my_module
print(my_module.greet("Akash"))
```

---

## 4. The __name__ Variable

Every Python file has a special variable called `__name__`.

```python
print(__name__)
```

When a file runs directly:
```
__name__ == "__main__"
```

### Common pattern

```python
def main():
    print("Running main function")

if __name__ == "__main__":
    main()
```

This prevents code from running when the file is imported.

---

## 5. What is a Package?

A package is a folder that contains multiple modules.

Example structure:

```
my_package/
    __init__.py
    module1.py
    module2.py
```

The `__init__.py` file tells Python this folder is a package.

---

## 6. Importing from Packages

```python
from my_package import module1
```

or

```python
from my_package.module1 import some_function
```

---

## 7. Best Practices

- Use meaningful module names
- Keep modules focused on one purpose
- Avoid circular imports
- Use packages for large projects

---

## 🎯 Summary

Today you learned:

- What modules are
- How to import modules
- How to create your own module
- The purpose of `__name__`
- What packages are and how to use them

You're now writing more professional Python code. 🚀
