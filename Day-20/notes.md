
# Day 20: Dictionaries in Python

## 1. Definition

A **dictionary** in Python is a built‑in data structure used to store data in **key–value pairs**.  
Each key in a dictionary maps to a specific value, allowing fast lookup and structured data storage.

Dictionaries are:

- Mutable (can be modified after creation)
- Unordered (prior to Python 3.7 order was not guaranteed)
- Indexed by **keys**, not numeric positions
- Defined using **curly braces `{}`**

Example:

```python
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student)
```

Official documentation:  
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

---

# 2. Detailed Explanation

## Dictionary Structure

A dictionary stores information in **key:value format**.

Example:

```python
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

print(person)
```

- **Keys** must be unique
- **Values** can be any data type

---

## Accessing Dictionary Values

Values are accessed using their keys.

```python
student = {"name": "Alice", "age": 20}

print(student["name"])
print(student["age"])
```

---

## Adding New Key-Value Pairs

Dictionaries are mutable, meaning new items can be added.

```python
car = {"brand": "Toyota", "year": 2022}

car["color"] = "Red"

print(car)
```

---

## Updating Values

You can update a value by assigning a new value to an existing key.

```python
user = {"username": "admin", "status": "active"}

user["status"] = "inactive"

print(user)
```

---

## Checking if a Key Exists

```python
student = {"name": "Alice", "age": 20}

print("name" in student)
print("grade" in student)
```

---

## Iterating Through Dictionaries

Loop through keys:

```python
person = {"name": "Tom", "age": 30, "city": "Paris"}

for key in person:
    print(key)
```

Loop through values:

```python
person = {"name": "Tom", "age": 30, "city": "Paris"}

for value in person.values():
    print(value)
```

Loop through key-value pairs:

```python
person = {"name": "Tom", "age": 30, "city": "Paris"}

for key, value in person.items():
    print(key, value)
```

---

# 3. Easy Short Code Examples

## Example 1: Creating a Dictionary

```python
book = {"title": "Python Basics", "pages": 300}
print(book)
```

## Example 2: Accessing Values

```python
user = {"name": "Sarah", "age": 28}

print(user["name"])
```

## Example 3: Adding Data

```python
product = {"name": "Laptop", "price": 1000}

product["stock"] = 50
print(product)
```

## Example 4: Updating Data

```python
settings = {"theme": "light"}

settings["theme"] = "dark"
print(settings)
```

## Example 5: Iterating Dictionary

```python
student = {"name": "Anna", "age": 21, "grade": "A"}

for key, value in student.items():
    print(key, value)
```

---

# 4. Do's and Don'ts

## Do's

✔ Use dictionaries when working with **structured data**  
✔ Use meaningful keys  
✔ Use dictionaries for **fast data lookup**  
✔ Use them to represent real-world objects

Example:

```python
user = {
    "id": 101,
    "username": "john_doe",
    "email": "john@email.com"
}
```

## Don'ts

✘ Do not use mutable objects as keys (like lists)  
✘ Do not create overly complex nested dictionaries without structure  
✘ Do not assume numeric indexing like lists

Incorrect:

```python
my_dict = {[1,2]: "value"}
```

---

# 5. Industry Standards

## Use Dictionaries for Data Representation

Dictionaries are widely used in:

- APIs
- JSON data
- Configuration files
- Database-like structures

Example:

```python
api_response = {
    "status": "success",
    "data": {"user_id": 101, "name": "Alice"}
}
```

---

## Use Clear Naming Conventions

Good dictionary variable names:

- `user_data`
- `config_settings`
- `api_response`
- `product_info`

---

# 6. Mistakes to Avoid

## 1. Using Duplicate Keys

Python automatically keeps the **last occurrence**.

```python
data = {"a": 1, "a": 2}
print(data)
```

---

## 2. Accessing Non‑existent Keys

```python
user = {"name": "Tom"}
print(user["age"])
```

This will raise a **KeyError**.

---

## 3. Confusing Dictionaries with Lists

Lists use indexes:

```python
my_list = [10,20,30]
print(my_list[0])
```

Dictionaries use keys:

```python
my_dict = {"a": 10, "b": 20}
print(my_dict["a"])
```

---

# References

Python Official Documentation  
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

Next topic: [Dictionary methods](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-21/notes.md)
