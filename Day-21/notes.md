
# Day 21: Dictionary Methods

## 1. Definition of the Topic

Dictionary methods are built-in functions in Python that allow you to perform operations on dictionaries such as accessing data, updating values, removing elements, and iterating through key-value pairs.

These methods help make dictionary operations efficient and readable.

Official documentation:
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

---

## 2. Detailed Explanation of the Topic

Common dictionary methods:

- get()
- keys()
- values()
- items()
- update()
- pop()
- popitem()
- clear()
- copy()

---

### get()

```python
student = {"name": "Alice", "age": 20}
print(student.get("name"))
print(student.get("grade"))
```

---

### keys()

```python
student = {"name": "Alice", "age": 20}
print(student.keys())
```

---

### values()

```python
student = {"name": "Alice", "age": 20}
print(student.values())
```

---

### items()

```python
student = {"name": "Alice", "age": 20}
print(student.items())
```

---

### update()

```python
student = {"name": "Alice"}
student.update({"age": 20})
print(student)
```

---

### pop()

```python
student = {"name": "Alice", "age": 20}
removed = student.pop("age")
print(removed)
print(student)
```

---

### popitem()

```python
student = {"name": "Alice", "age": 20}
print(student.popitem())
```

---

### clear()

```python
student = {"name": "Alice", "age": 20}
student.clear()
print(student)
```

---

### copy()

```python
original = {"a": 1, "b": 2}
copy_dict = original.copy()
print(copy_dict)
```

---

## 3. Easy Short Code Examples

```python
user = {"username": "admin"}
print(user.get("username"))

data = {"a": 1, "b": 2}
print(data.keys())
print(data.values())

for key, value in data.items():
    print(key, value)

config = {"theme": "light"}
config.update({"theme": "dark"})
print(config)

numbers = {"one": 1, "two": 2}
numbers.pop("one")
print(numbers)
```

---

## 4. Do's and Don'ts

### Do's
- Use get() to avoid errors
- Use items() for iteration
- Use update() for merging

### Don'ts
- Avoid direct key access without checking
- Do not confuse pop() and popitem()

---

## 5. Industry Standards

```python
user = {"name": "Alice"}
age = user.get("age", 0)
print(age)

data = {"a": 1, "b": 2}
for key, value in data.items():
    print(f"{key}: {value}")
```

---

## 6. Mistakes to Avoid

```python
data = {"a": 1}
# print(data["b"])  # KeyError

a = {"x": 1}
b = a
b["x"] = 2
print(a)
```

---

## Summary

- Dictionary methods simplify data handling
- They help safely access and modify data
- They are widely used in real-world applications

Next topic: [Basic problem solving with collections]()
