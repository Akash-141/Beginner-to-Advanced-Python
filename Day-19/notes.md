# Day 19: Context Managers and Advanced File Handling

## 1. What is a Context Manager?
A context manager is a Python construct that properly manages resources like files, network connections, or locks.

It ensures:
- Resources are opened correctly
- Resources are always closed properly
- Cleaner and safer code

The most common context manager is the `with` statement.

---

## 2. Basic Example of Context Manager

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Why use `with`?
Without `with`, you must manually close files:

```python
file = open("example.txt", "r")
content = file.read()
file.close()
```

If an error occurs, the file might never close. The `with` statement prevents this problem.

---

## 3. How Context Managers Work

A context manager has two main methods:

- `__enter__()` → runs when entering the block  
- `__exit__()` → runs when leaving the block  

---

## 4. Creating a Custom Context Manager (Class Based)

```python
class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

with MyContext():
    print("Inside the block")
```

---

## 5. Context Manager Using contextlib

Python provides a simpler way using `contextlib`.

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Start")
    yield
    print("End")

with my_context():
    print("Inside block")
```

---

## 6. Best Practices for File Handling

✅ Always use `with` when working with files  
✅ Handle exceptions when reading files  
✅ Use correct file modes (`r`, `w`, `a`, `rb`, etc.)  
✅ Avoid loading huge files fully into memory  

---

## 7. Reading Large Files Efficiently

```python
with open("bigfile.txt", "r") as f:
    for line in f:
        print(line.strip())
```

This reads line by line instead of loading the entire file.

---

## 🎯 Summary

Today you learned:

- What context managers are  
- Why `with` is important  
- How to build custom context managers  
- Best practices for file handling  
- Efficient large file reading  

Great progress! 🚀
