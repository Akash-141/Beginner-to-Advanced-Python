
# Day 17: List Methods

## 1. Definition of the Topic

List methods are built‑in functions provided by Python that allow developers to modify and interact with lists efficiently. Because lists are mutable data structures, these methods can change the content of a list directly.

List methods are commonly used to:

- Add elements to a list
- Remove elements
- Rearrange items
- Search or analyze list content

Official Python documentation:
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

---

## 2. Detailed Explanation of the Topic

Python provides several built‑in methods that operate directly on list objects. These methods help simplify common programming tasks such as inserting elements, deleting items, sorting data, or copying lists.

Common list methods include:

append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()

Understanding these methods is essential because lists are one of the most widely used data structures in Python programming.

---

### append()

The append() method adds a single element to the end of the list.

Example:

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```

---

### extend()

extend() adds elements from another iterable to the list.

Example:

```python
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)
```

---

### insert()

insert() adds an element at a specific position.

Example:

```python
fruits = ["apple", "banana"]
fruits.insert(1, "mango")
print(fruits)
```

---

### remove()

remove() deletes the first occurrence of a value.

Example:

```python
items = ["pen", "book", "eraser"]
items.remove("book")
print(items)
```

---

### pop()

pop() removes and returns an element from the list.

Example:

```python
numbers = [10, 20, 30]
last_item = numbers.pop()
print(last_item)
print(numbers)
```

---

### clear()

clear() removes all elements from a list.

Example:

```python
data = [1, 2, 3]
data.clear()
print(data)
```

---

### index()

index() returns the index position of a value.

Example:

```python
fruits = ["apple", "banana", "mango"]
print(fruits.index("banana"))
```

---

### count()

count() returns the number of times a value appears in a list.

Example:

```python
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))
```

---

### sort()

sort() arranges list elements in ascending order.

Example:

```python
numbers = [5, 1, 4, 2]
numbers.sort()
print(numbers)
```

---

### reverse()

reverse() reverses the order of elements.

Example:

```python
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)
```

---

### copy()

copy() creates a shallow copy of a list.

Example:

```python
original = [1, 2, 3]
duplicate = original.copy()
print(duplicate)
```

---

## 3. Do's and Don'ts

### Do's

- Use append() when adding a single item.
- Use extend() when combining lists.
- Use copy() if you need a separate list object.
- Keep list operations readable.

### Don'ts

- Do not assume remove() deletes all duplicates.
- Do not modify lists unexpectedly when sharing references.
- Do not chain too many operations on one line.

---

## 4. Industry Standards

Professional developers follow the PEP 8 style guide when writing Python code.

PEP 8:
https://peps.python.org/pep-0008/

Best practices:

Use clear variable names.

Bad:

```python
x = [1,2,3]
```

Better:

```python
scores = [1, 2, 3]
```

Keep operations readable.

Bad:

```python
numbers.append(4); numbers.append(5)
```

Better:

```python
numbers.append(4)
numbers.append(5)
```

Avoid modifying lists while iterating.

Bad:

```python
for n in numbers:
    numbers.remove(n)
```

Better:

```python
numbers = [n for n in numbers if n != 0]
```

---

## 5. Mistakes to Avoid

Confusing append() and extend().

Bad:

```python
numbers = [1, 2]
numbers.append([3, 4])
print(numbers)
```

Correct:

```python
numbers = [1, 2]
numbers.extend([3, 4])
```

Using pop() on an empty list.

Bad:

```python
items = []
items.pop()
```

Forgetting that sort() modifies the list.

Bad:

```python
numbers = [3, 1, 2]
sorted_numbers = numbers.sort()
print(sorted_numbers)
```

Correct:

```python
numbers = [3, 1, 2]
numbers.sort()
print(numbers)
```

---

## 6. Summary

In this lesson you learned:

- What list methods are
- How to add elements to lists
- How to remove elements
- How to search lists
- How to sort and reverse lists
- Best practices used in professional Python development

List methods are essential tools for working with collections of data in Python programs.

Next topic: [Tuples](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-18/notes.md)
