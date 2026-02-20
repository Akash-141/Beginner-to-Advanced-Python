# Day 11: Tuples and Sets in Python

## 1. Tuples

A tuple is a collection of items similar to a list, but it cannot be changed after creation (immutable).

Tuples are written using parentheses ().

```python
numbers = (1, 2, 3, 4)
names = ("Alice", "Bob", "Charlie")
```

Official documentation (Tuples):
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

---

## 2. Accessing Tuple Items

Tuples use indexing just like lists.

```python
numbers = (10, 20, 30)
print(numbers[0])
print(numbers[-1])
```

---

## 3. Why Use Tuples?

- Data should not change
- Slightly faster than lists
- Safe from accidental modification

---

## 4. Sets

A set is a collection of unique items.

Sets are written using curly braces {}.

```python
numbers = {1, 2, 3, 4}
```

Official documentation (Sets):
https://docs.python.org/3/tutorial/datastructures.html#sets

---

## 5. Set Characteristics

- No duplicate values
- Unordered
- Mutable (you can add/remove items)

Example:

```python
numbers = {1, 2, 2, 3}
print(numbers)  # Duplicates removed
```

---

## 6. Adding and Removing Set Items

### add()

```python
numbers.add(5)
```

### remove()

```python
numbers.remove(1)
```

---

## 7. Looping Through a Set

```python
for num in numbers:
    print(num)
```

---

## Practice Tasks

1. Create a tuple with five values.
2. Print the first and last item of the tuple.
3. Create a set with duplicate values and print it.
4. Add a new value to a set.
5. Remove a value from a set.
6. Loop through a set and print each item.

---

## What You Learned Today

- What tuples are
- Tuple indexing
- Immutable data
- What sets are
- Unique values in sets
- Adding and removing items from sets
