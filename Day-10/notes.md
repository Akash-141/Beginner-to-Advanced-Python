# Day 10: Dictionaries in Python

## 1. What is a Dictionary?

A dictionary is a collection of key-value pairs.

Dictionaries are written using curly braces {}.

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

Official documentation:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

---

## 2. Accessing Values

You access values using their keys.

```python
print(person["name"])
print(person["age"])
```

---

## 3. Adding or Updating Items

You can add new key-value pairs or update existing ones.

```python
person["email"] = "alice@example.com"
person["age"] = 26
print(person)
```

---

## 4. Removing Items

### pop()

Removes a key and returns its value.

```python
person.pop("city")
```

### del

```python
del person["age"]
```

---

## 5. Looping Through a Dictionary

### Loop through keys

```python
for key in person:
    print(key)
```

### Loop through values

```python
for value in person.values():
    print(value)
```

### Loop through both keys and values

```python
for key, value in person.items():
    print(key, value)
```

---

## 6. Dictionary Length

Use len() to find how many key-value pairs exist.

```python
print(len(person))
```

---

## Practice Tasks

1. Create a dictionary with three key-value pairs.
2. Print one value using its key.
3. Add a new key-value pair.
4. Update an existing value.
5. Remove a key.
6. Loop through the dictionary and print keys and values.

---

## What You Learned Today

- What dictionaries are
- Key-value pairs
- Accessing values
- Adding and updating items
- Removing items
- Looping through dictionaries
- len() with dictionaries
