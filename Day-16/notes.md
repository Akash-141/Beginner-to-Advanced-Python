
# Day 16: Lists in Python

## 1. Definition of the Topic

A **list** in Python is a built-in data structure used to store **multiple values in a single variable**.
Lists are **ordered**, **mutable**, and **allow duplicate values**.

Lists are one of the most widely used data structures in Python and are commonly used to store collections of data such as numbers, text, or objects.

Official Documentation:
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

---

## 2. Detailed Explanation of the Topic

Lists are created using **square brackets []**, and each item in the list is separated by a comma.

Example structure:

```python
my_list = [item1, item2, item3]
```

Important properties of Python lists:

- Lists maintain the **order** of items
- Lists are **mutable**, meaning items can be modified
- Lists allow **duplicate elements**
- Lists can contain **multiple data types**
- Lists support **indexing**

Lists are heavily used in real-world programming tasks like:

- storing user data
- processing datasets
- handling sequences of values
- implementing algorithms

---

### 2.1 Creating a List

Lists are defined using square brackets.

Example:

```python
numbers = [10, 20, 30, 40]
print(numbers)
```

---

### 2.2 Lists with Different Data Types

Python lists can store different types of data.

Example:

```python
data = [10, "Python", 3.14, True]
print(data)
```

---

### 2.3 Accessing List Elements

Elements inside a list can be accessed using **index numbers**.

Indexing starts from **0**.

Example:

```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(fruits[1])
```

---

### 2.4 Negative Indexing

Python also supports **negative indexing**, which accesses elements from the end of the list.

Example:

```python
fruits = ["apple", "banana", "mango"]
print(fruits[-1])
```

Explanation:

`-1` refers to the last element of the list.

---

### 2.5 Modifying List Values

Lists are mutable, meaning their values can be changed.

Example:

```python
numbers = [1, 2, 3]
numbers[1] = 10
print(numbers)
```

---

### 2.6 Getting the Length of a List

The built-in `len()` function returns the number of elements in a list.

Example:

```python
items = ["pen", "book", "eraser"]
print(len(items))
```

---

### 2.7 Nested Lists

A list can contain another list inside it.

Example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0])
print(matrix[1][2])
```

Nested lists are commonly used to represent **tables, grids, and matrices**.

---

### 2.8 Iterating Through a List

Lists are frequently used with loops.

Example:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

---

## 3. Do's and Don'ts

### Do's

- Use lists when you need an **ordered collection of items**
- Use descriptive variable names
- Keep list formatting readable
- Use loops to process list elements

### Don'ts

- Do not mix unrelated data unnecessarily
- Do not use confusing variable names
- Do not create excessively large lists without a reason

---

## 4. Industry Standards

Professional developers follow the **PEP 8 style guide**.

PEP 8:
https://peps.python.org/pep-0008/

Best practices include:

### Use meaningful variable names

Bad:

```python
x = [1, 2, 3]
```

Better:

```python
scores = [1, 2, 3]
```

---

### Maintain readable spacing

Bad:

```python
numbers=[1,2,3,4,5]
```

Better:

```python
numbers = [1, 2, 3, 4, 5]
```

---

### Use lists to group related data

Example:

```python
students = ["Ali", "Sara", "John"]

for student in students:
    print(student)
```

---

## 5. Mistakes to Avoid

### Index Out of Range

Bad:

```python
numbers = [10, 20, 30]
print(numbers[5])
```

This causes:

`IndexError: list index out of range`

---

### Treating Non‑Lists as Lists

Bad:

```python
numbers = 10
print(numbers[0])
```

Correct:

```python
numbers = [10, 20, 30]
print(numbers[0])
```

---

### Modifying Invalid Index

Bad:

```python
items = ["pen", "book"]
items[5] = "pencil"
```

Correct:

```python
items = ["pen", "book"]
items[1] = "pencil"
```

---

## 6. Summary

In this lesson you learned:

- What lists are
- How to create lists
- How to access elements using indexes
- How to modify list items
- How to measure list length
- How nested lists work
- How lists are used with loops

Lists are one of the **most fundamental and powerful data structures in Python**.

Next topic: [List methods](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-17/notes.md)
