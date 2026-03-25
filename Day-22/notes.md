
# Day 22: Basic Problem Solving with Collections

## 1. Definition of the Topic

Basic problem solving with collections involves using Python data structures such as **lists, tuples, sets, and dictionaries** to solve common programming problems efficiently.

These collections help in organizing, processing, and analyzing data in real-world scenarios.

---

## 2. Detailed Explanation of the Topic

Collections are essential tools for solving problems like:

- Removing duplicates
- Counting occurrences
- Searching data
- Grouping data
- Filtering data

Choosing the right collection is key to writing efficient code.

---

### Using Lists for Problem Solving

Lists are useful for ordered data and iteration.

```python
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(total)
```

---

### Using Sets to Remove Duplicates

Sets automatically remove duplicate values.

```python
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)

print(unique_numbers)
```

---

### Using Dictionaries for Counting

Dictionaries are perfect for counting occurrences.

```python
text = "apple banana apple"
words = text.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)
```

---

### Using Tuples for Fixed Data

Tuples are used for fixed and structured data.

```python
point = (10, 20)
print(point[0], point[1])
```

---

### Combining Collections

Sometimes multiple collections are used together.

```python
numbers = [1, 2, 2, 3, 4]
unique = set(numbers)

result = list(unique)
print(result)
```

---

## 3. Easy Short Code Examples

### Example 1: Find Maximum Number

```python
numbers = [10, 20, 30, 5]
print(max(numbers))
```

### Example 2: Remove Duplicates

```python
data = [1, 1, 2, 3, 3]
print(list(set(data)))
```

### Example 3: Count Frequency

```python
items = ["a", "b", "a", "c", "b", "a"]
freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1

print(freq)
```

### Example 4: Filter Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)
```

### Example 5: Check Membership

```python
names = {"Alice", "Bob", "Charlie"}

print("Alice" in names)
```

---

## 4. Do's and Don'ts

### Do's

- Use lists for ordered data
- Use sets for uniqueness
- Use dictionaries for counting and mapping
- Choose the right data structure

### Don'ts

- Do not use lists when uniqueness is required
- Do not use sets when order matters
- Do not use tuples when data needs modification

---

## 5. Industry Standards

### Efficient Data Handling

```python
numbers = [1, 2, 2, 3]
unique = list(set(numbers))
print(unique)
```

### Clean Counting Pattern

```python
data = ["a", "b", "a"]
count = {}

for item in data:
    count[item] = count.get(item, 0) + 1

print(count)
```

### Readable Code

- Use meaningful variable names
- Break problems into steps
- Keep logic simple

---

## 6. Mistakes to Avoid

### Using Wrong Data Structure

```python
# Using list instead of set for uniqueness
data = [1, 1, 2, 2]
print(data)
```

Correct:

```python
print(set(data))
```

---

### Inefficient Counting

```python
items = ["a", "b", "a"]
# Bad approach using nested loops
```

Better:

```python
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
```

---

### Ignoring Built-in Functions

```python
numbers = [1, 2, 3]
# Instead of manual max calculation
print(max(numbers))
```

---

## Summary

- Collections are powerful tools for solving problems
- Choosing the right structure improves performance
- Practice with real problems to master these concepts
