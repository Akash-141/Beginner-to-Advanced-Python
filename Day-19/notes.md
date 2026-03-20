# Day 19: Sets in Python

## 1. Definition

A **set** in Python is an unordered collection of unique elements. Sets are commonly used when you need to store multiple items but want to automatically remove duplicates and perform mathematical set operations such as union, intersection, and difference.

Key properties:
- Unordered (items do not have a fixed position)
- Mutable (you can add or remove items)
- Contains only unique values
- Defined using curly braces `{}` or the `set()` constructor

Official documentation: https://docs.python.org/3/library/stdtypes.html#set

---

## 2. Detailed Explanation

### What Makes Sets Different

Unlike lists or tuples, sets do not maintain the order of elements. When you print a set, the items may appear in a different order each time. This happens because sets are implemented using **hash tables** for fast lookup.

Because of this design:
- Checking if an item exists in a set is very fast.
- Duplicate values are automatically removed.

### Creating a Set

Sets can be created using curly braces or the `set()` function.

Example:

```python
numbers = {1, 2, 3, 4}
print(numbers)
```

Using `set()`:

```python
numbers = set([1, 2, 3, 4])
print(numbers)
```

### Automatic Removal of Duplicates

If duplicate elements are added during creation, Python keeps only one instance.

```python
values = {1, 2, 2, 3, 3, 4}
print(values)
```

Output will contain only unique values.

### Sets Are Unordered

Since sets do not maintain order, indexing does not work.

```python
colors = {"red", "green", "blue"}
print(colors)
```

Trying this will cause an error:

```python
colors = {"red", "green", "blue"}
print(colors[0])
```

### Membership Testing

Sets are commonly used to check whether an item exists.

```python
fruits = {"apple", "banana", "mango"}

print("apple" in fruits)
print("grape" in fruits)
```

### Iterating Through a Set

You can loop through set elements using a `for` loop.

```python
animals = {"cat", "dog", "tiger"}

for animal in animals:
    print(animal)
```

### Set Operations

Union (combine elements from both sets):

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1 | set2
print(result)
```

Intersection (common elements):

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

result = set1 & set2
print(result)
```

Difference (elements present in first set but not the second):

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

result = set1 - set2
print(result)
```

---

## 3. Easy Short Code Examples

### Example 1: Creating a Set

```python
languages = {"Python", "Java", "C++"}
print(languages)
```

### Example 2: Removing Duplicate Values

```python
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)
```

### Example 3: Membership Check

```python
fruits = {"apple", "banana", "orange"}

if "apple" in fruits:
    print("Apple is in the set")
```

### Example 4: Looping Through a Set

```python
colors = {"red", "blue", "green"}

for color in colors:
    print(color)
```

### Example 5: Basic Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)
```

---

## 4. Do's and Don'ts

### Do's

✔ Use sets when you need **unique values only**  
✔ Use sets for **fast membership testing**  
✔ Use sets when performing **mathematical set operations**  
✔ Use sets to remove duplicates from a list

Example:

```python
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)
```

### Don'ts

✘ Do not rely on order in a set  
✘ Do not use indexing or slicing with sets  
✘ Do not store mutable objects like lists inside a set

Incorrect:

```python
my_set = {[1, 2], [3, 4]}
```

---

## 5. Industry Standards

### Use Sets for Fast Lookups

```python
allowed_users = {"alice", "bob", "charlie"}

username = "alice"

if username in allowed_users:
    print("Access granted")
```

### Remove Duplicates Efficiently

```python
data = [1, 2, 2, 3, 4, 4, 5]
unique_data = list(set(data))
print(unique_data)
```

### Prefer Clear Naming

Examples:
- `unique_ids`
- `allowed_users`
- `visited_nodes`

---

## 6. Mistakes to Avoid

### 1. Trying to Access by Index

```python
my_set = {10, 20, 30}
print(my_set[0])
```

### 2. Expecting Ordered Output

The order of elements in sets is not guaranteed.

### 3. Forgetting That Sets Remove Duplicates

If duplicates are important, use a list instead.

### 4. Storing Mutable Types

Allowed:
- integers
- strings
- tuples

Not allowed:
- lists
- dictionaries
- sets

---

## References

Python Official Documentation  
https://docs.python.org/3/library/stdtypes.html#set

Next topic: [Dictionaries](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-20/notes.md)
