# Day 8: Lists in Python

## 1. What is a List?

A list is a collection of multiple items stored in a single variable.

Lists are written using square brackets [].

```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
```

Official documentation:
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

---

## 2. Accessing List Items

Lists use indexing (starting at 0).

```python
numbers = [10, 20, 30]
print(numbers[0])
print(numbers[1])
```

Negative indexing:

```python
print(numbers[-1])
```

---

## 3. Modifying List Items

Lists are mutable, which means you can change their values.

```python
numbers = [10, 20, 30]
numbers[1] = 99
print(numbers)
```

---

## 4. Adding Items

### append()

Adds an item to the end of the list.

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```

### insert()

Adds an item at a specific position.

```python
numbers.insert(1, 100)
print(numbers)
```

---

## 5. Removing Items

### remove()

Removes a specific value.

```python
numbers.remove(100)
```

### pop()

Removes an item by index.

```python
numbers.pop(0)
```

---

## 6. Looping Through a List

```python
numbers = [1, 2, 3]

for num in numbers:
    print(num)
```

---

## 7. List Length

Use len() to get the number of items in a list.

```python
numbers = [1, 2, 3]
print(len(numbers))
```

---

## Practice Tasks

1. Create a list of five numbers.
2. Print the first and last items.
3. Change one item in the list.
4. Add a new item using append().
5. Remove an item using pop().
6. Loop through the list and print each value.

---

## What You Learned Today

- What lists are
- Indexing (positive and negative)
- Modifying lists
- append() and insert()
- remove() and pop()
- Looping through lists
- len() with lists
