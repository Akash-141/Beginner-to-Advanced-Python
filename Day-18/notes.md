
# Day 18: Tuples in Python

## 1. Definition of the Topic

A **tuple** in Python is a built-in data structure used to store multiple values in a single variable.  
Tuples are **ordered**, **immutable**, and **allow duplicate values**.

The key difference between **lists and tuples** is that tuples **cannot be modified after they are created**.

Tuples are commonly used when data should remain **constant and protected from modification**.

Official Python Documentation:  
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

---

## 2. Detailed Explanation of the Topic

Tuples are created using **parentheses `()`** and items are separated by commas.

Example structure:

```python
my_tuple = (item1, item2, item3)
```

Key characteristics of tuples:

- **Ordered** → items maintain their position
- **Immutable** → values cannot be changed
- **Allow duplicates**
- **Support indexing**
- **Can store multiple data types**

Because tuples are immutable, they are often used for:

- configuration values
- database records
- coordinates
- fixed collections of data

Python documentation reference:  
https://docs.python.org/3/library/stdtypes.html#tuple

---

### 2.1 Creating a Tuple

Example:

```python
numbers = (10, 20, 30)
print(numbers)
```

---

### 2.2 Tuple with Multiple Data Types

Tuples can contain different data types.

Example:

```python
data = (10, "Python", 3.14, True)
print(data)
```

---

### 2.3 Accessing Tuple Elements

Elements in a tuple can be accessed using **index numbers**.

Example:

```python
fruits = ("apple", "banana", "mango")
print(fruits[0])
print(fruits[2])
```

Indexing starts from **0**.

---

### 2.4 Negative Indexing

Python supports **negative indexing**, which starts from the end of the tuple.

Example:

```python
fruits = ("apple", "banana", "mango")
print(fruits[-1])
```

Explanation:

`-1` refers to the last element.

---

### 2.5 Tuple Length

The `len()` function returns the number of items in a tuple.

Example:

```python
items = ("pen", "book", "eraser")
print(len(items))
```

---

### 2.6 Nested Tuples

Tuples can contain other tuples.

Example:

```python
matrix = (
    (1, 2, 3),
    (4, 5, 6)
)

print(matrix[0])
print(matrix[1][2])
```

Nested tuples are often used to represent **fixed structured data**.

---

### 2.7 Iterating Through a Tuple

Tuples can be used with loops.

Example:

```python
numbers = (10, 20, 30)

for number in numbers:
    print(number)
```

---

### 2.8 Tuple Packing and Unpacking

Python allows grouping values into a tuple (packing) and assigning them to variables (unpacking).

Example:

```python
person = ("Alice", 25, "Engineer")

name, age, profession = person

print(name)
print(age)
print(profession)
```

---

## 3. Do's and Don'ts

### Do's

- Use tuples for **fixed data that should not change**
- Use tuples when returning **multiple values from functions**
- Use meaningful variable names
- Use tuples for **structured records**

### Don'ts

- Do not try to modify tuple elements
- Do not use tuples when frequent modifications are required
- Do not confuse tuples with lists

---

## 4. Industry Standards

Professional developers follow the **PEP 8 style guide** when writing Python code.

PEP 8:
https://peps.python.org/pep-0008/

Best practices include:

### Use tuples for fixed collections

Example:

```python
coordinates = (10.5, 20.3)
print(coordinates)
```

---

### Use tuple unpacking for readability

Example:

```python
point = (5, 10)
x, y = point
print(x)
print(y)
```

---

### Prefer tuples for constant values

Example:

```python
RGB_RED = (255, 0, 0)
```

This communicates that the values should not change.

---

## 5. Mistakes to Avoid

### Trying to Modify Tuples

Bad:

```python
numbers = (1, 2, 3)
numbers[1] = 10
```

This causes:

`TypeError: 'tuple' object does not support item assignment`

---

### Forgetting the Comma in Single-Item Tuple

Bad:

```python
single = (5)
```

Correct:

```python
single = (5,)
```

---

### Confusing Lists and Tuples

Bad:

```python
data = (1, 2, 3)
data.append(4)
```

Correct:

```python
data = [1, 2, 3]
data.append(4)
```

---

## 6. Summary

In this lesson you learned:

- What tuples are
- How to create tuples
- How to access tuple elements
- How tuple unpacking works
- Differences between lists and tuples
- Best practices used in real Python programs

Tuples are important for representing **fixed, structured, and immutable data** in Python programs.

Next topic: [Sets](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-19/notes.md)
