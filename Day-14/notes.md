# Day 14: For Loops

## 1. Definition

A **for loop** in Python is a control flow statement used to iterate
over a sequence (such as a list, tuple, string, dictionary, or range).
It allows a block of code to run once for each item in the sequence.

Unlike `while` loops that run based on a condition, `for` loops are
typically used when the number of iterations is known or when iterating
over a collection of items.

Official Python documentation:
https://docs.python.org/3/tutorial/controlflow.html#for-statements

------------------------------------------------------------------------

## 2. Detailed Explanation

A `for` loop works by taking each element from an iterable object and
executing a block of code for that element.

Common iterable objects include:

-   Lists
-   Tuples
-   Strings
-   Dictionaries
-   Sets
-   The `range()` function

### Basic Syntax

``` python
for variable in iterable:
    # code block
```

Steps:

1.  Python retrieves the first item from the iterable.
2.  The item is assigned to the loop variable.
3.  The code block runs.
4.  Python moves to the next item.
5.  The loop ends when all items are processed.

Reference: https://realpython.com/python-for-loop/

------------------------------------------------------------------------

## 3. Easy Code Examples

### Example 1: Basic for loop

``` python
for i in range(5):
    print(i)
```

### Example 2: Iterating over a list

``` python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

### Example 3: Iterating over a string

``` python
word = "python"

for letter in word:
    print(letter)
```

### Example 4: Using break in a for loop

``` python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)
```

### Example 5: Using continue in a for loop

``` python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue
    print(num)
```

### Example 6: Using range with start and stop

``` python
for i in range(1, 6):
    print(i)
```

### Example 7: Loop with index using enumerate

``` python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

------------------------------------------------------------------------

## 4. Do's and Don'ts

### Do's

✔ Use `for` loops when iterating over collections.

✔ Use descriptive variable names.

✔ Use `enumerate()` when you need both index and value.

✔ Keep loop logic simple.

Example:

``` python
students = ["Alice", "Bob", "Charlie"]

for student in students:
    print(student)
```

### Don'ts

✘ Don't modify a list while iterating over it.

✘ Don't use unnecessary nested loops.

✘ Don't use unclear variable names like `x`, `y`, `z` when meaning
matters.

Bad example:

``` python
for x in range(5):
    print(x)
```

Better:

``` python
for number in range(5):
    print(number)
```

------------------------------------------------------------------------

## 5. Industry Standards

Professional Python developers follow these practices:

### Use Pythonic iteration

Instead of:

``` python
for i in range(len(items)):
    print(items[i])
```

Prefer:

``` python
for item in items:
    print(item)
```

### Use enumerate when index is required

``` python
for index, item in enumerate(items):
    print(index, item)
```

### Avoid deep nesting

Complex nested loops reduce readability and increase bugs.

Reference: https://peps.python.org/pep-0008/

------------------------------------------------------------------------

## 6. Common Mistakes to Avoid

### Using range(len()) unnecessarily

Bad:

``` python
items = ["a", "b", "c"]

for i in range(len(items)):
    print(items[i])
```

Better:

``` python
for item in items:
    print(item)
```

### Forgetting indentation

Bad:

``` python
for i in range(5):
print(i)
```

### Modifying iterable during iteration

Bad:

``` python
numbers = [1,2,3,4]

for num in numbers:
    numbers.remove(num)
```

This can cause unexpected behavior.

------------------------------------------------------------------------

## Summary

A **for loop** is one of the most commonly used structures in Python. It
allows clean and readable iteration over sequences.

Key ideas:

-   Used for iterating over collections
-   Works with lists, tuples, strings, dictionaries, and ranges
-   Supports `break` and `continue`
-   Pythonic loops prefer direct iteration rather than index-based
    access

Further reading:

Python documentation:
https://docs.python.org/3/tutorial/controlflow.html#for-statements

Real Python guide: https://realpython.com/python-for-loop/

Next topic: [Loop control statements](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-15/notes.md)

