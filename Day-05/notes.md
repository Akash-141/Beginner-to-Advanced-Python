# Day 5: Strings in Python

## 1. What is a String?

A string is text data in Python.

Strings are written using single quotes or double quotes:

```python
name = "Alice"
message = 'Hello World'
```

Official documentation:
https://docs.python.org/3/tutorial/introduction.html#strings

---

## 2. Printing Strings

```python
print("Hello")
```

You can also print variables:

```python
name = "Alice"
print(name)
```

---

## 3. String Concatenation

You can join strings using +

```python
first = "Hello"
second = "World"
result = first + " " + second
print(result)
```

---

## 4. String Repetition

You can repeat strings using *

```python
print("Hi " * 3)
```

---

## 5. String Indexing

Strings are ordered. Each character has a position (index).

Indexing starts at 0.

```python
text = "Python"
print(text[0])  # P
print(text[1])  # y
```

You can also use negative indexing:

```python
print(text[-1])  # n
```

---

## 6. String Length

Use len() to find the length of a string.

```python
text = "Python"
print(len(text))
```

---

## 7. Basic String Methods

### Uppercase

```python
text = "python"
print(text.upper())
```

### Lowercase

```python
text = "PYTHON"
print(text.lower())
```

### Replace

```python
text = "Hello World"
print(text.replace("World", "Python"))
```

---

## Practice Tasks

1. Create a string with your name and print it.
2. Join two strings together.
3. Print the first character of a word.
4. Print the last character using negative indexing.
5. Find the length of a sentence.
6. Convert a string to uppercase.
7. Replace one word in a sentence.

---

## What You Learned Today

- What strings are
- How to print text
- Concatenation (+)
- Repetition (*)
- Indexing
- len() function
- Basic string methods
