# Day 6: Strings and String Operations

## 1. What is a String in Python?

A **string** in Python is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`).

Strings are used to store textual data such as names, messages, sentences, file paths, and symbols.

In Python, strings are:

- **Ordered** → characters have a defined sequence
- **Immutable** → cannot be changed after creation
- **Indexed** → each character has a position (starting from 0)
- **Iterable** → you can loop through each character

Official reference:  
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

---

## 2. Why Strings Matter

Strings are one of the most frequently used data types in Python. Almost every real-world application deals with text:

- Web development (user input, HTML, JSON)
- Automation (file names, messages, logs)
- Data science (cleaning and processing text)
- APIs and backend services

Because strings are **immutable**:
- You cannot change individual characters directly
- Any operation that “modifies” a string actually creates a **new** string

Python provides powerful tools for working with strings:
- Indexing and slicing
- Concatenation and repetition
- Many built-in string methods
- Modern string formatting techniques

---

## 3. Creating Strings

You can create strings in several ways:

```python
name = "Akash"
city = 'Dhaka'
paragraph = """This is a
multi-line
string"""

print(name)
print(city)
print(paragraph)
```

**Notes:**
- Single and double quotes work the same way.
- Triple quotes are useful for multi-line text or documentation.
- You can include quotes inside a string by mixing quote types or using escape characters (`\'` or `\"`).

---

## 4. String Indexing

Every character in a string has a position called an **index**.

- Indexing starts at `0` for the first character
- Negative indexes count from the end (`-1` is the last character)

```python
text = "Python"

print(text[0])    # P
print(text[3])    # h
print(text[-1])   # n
print(text[-2])   # o
```

Trying to access an index that does not exist raises an `IndexError`.

---

## 5. String Slicing

Slicing lets you extract a portion (substring) of a string.

**Syntax:** `string[start:end:step]`

- `start` → starting index (inclusive)
- `end` → ending index (exclusive)
- `step` → optional step size

```python
text = "Programming"

print(text[0:6])     # Progra
print(text[3:])      # gramming
print(text[:5])      # Progr
print(text[::2])     # Pormig  (every second character)
print(text[::-1])    # gnimmargorP  (reversed string)
```

Slicing is one of the most useful features when working with text.

---

## 6. String Concatenation

You can join strings together using the `+` operator.

```python
first = "Hello"
second = "World"
result = first + " " + second
print(result)                # Hello World
```

**Important:** You can only concatenate strings with other strings. Mixing a string and a number causes a `TypeError`.

```python
age = 21
# print("Age: " + age)       # TypeError
print("Age: " + str(age))    # Correct
```

---

## 7. String Repetition

You can repeat a string using the `*` operator.

```python
print("Ha" * 3)              # HaHaHa
print("-" * 20)              # --------------------
```

This is useful for creating visual separators or simple patterns.

---

## 8. Useful String Methods

Python comes with many built-in methods that make working with strings easy.

```python
text = "Python"
print(text.upper())          # PYTHON
print(text.lower())          # python
print(text.title())          # Python

text = "   hello   "
print(text.strip())          # hello   (removes leading/trailing spaces)

text = "I like Java"
print(text.replace("Java", "Python"))   # I like Python

sentence = "Python is powerful"
words = sentence.split()     # ['Python', 'is', 'powerful']
print(words)

text = "Hello World"
print(text.find("World"))    # 6
print(text.startswith("Hello"))  # True
print(text.endswith("World"))    # True
```

**Remember:** String methods return a **new** string. The original string remains unchanged.

---

## 9. String Formatting

There are several ways to insert values into strings. The modern and recommended way is **f-strings**.

```python
name = "Akash"
age = 21

# f-string (recommended)
print(f"My name is {name} and I am {age} years old")

# .format() method
print("My name is {} and I am {} years old".format(name, age))

# Older % formatting (less common now)
print("My name is %s and I am %d years old" % (name, age))
```

**f-strings** (available since Python 3.6) are preferred because they are readable, concise, and efficient.

---

## 10. Do’s and Don’ts

### Do’s

- Prefer **f-strings** for formatting
- Use meaningful variable names
- Use built-in string methods instead of writing your own logic
- Clean user input with methods like `.strip()`
- Remember that strings are immutable
- Use slicing for extracting parts of text

### Don’ts

- Do **not** try to change individual characters directly (`text[0] = "J"`)
- Do **not** overuse `+` for building very large strings in loops (use `join()` instead)
- Do **not** ignore case sensitivity (`"python" != "Python"`)
- Do **not** assume that user input is clean or correctly formatted
- Do **not** mix strings and numbers without conversion

---

## 11. Industry Standards (PEP 8)

According to **PEP 8**:

- Prefer f-strings (Python 3.6+)
- Keep string formatting readable
- Use descriptive variable names
- Avoid overly complex expressions inside f-strings

PEP 8 reference:  
https://peps.python.org/pep-0008/

Professional Python code favors clarity and modern features like f-strings.

---

## 12. Common Mistakes to Avoid

### Trying to Modify a String Directly

```python
text = "Python"
# text[0] = "J"          # TypeError: 'str' object does not support item assignment
```

### Case Sensitivity

```python
print("python" == "Python")   # False
```

### Mixing Strings and Numbers

```python
age = "21"
# print("Age: " + age + 5)    # TypeError
print("Age: " + age + str(5)) # Correct
# or better:
print(f"Age: {age}")
```

### Forgetting That Methods Return New Strings

```python
text = "hello"
text.upper()
print(text)                   # still "hello"

text = text.upper()
print(text)                   # "HELLO"
```

---

## Practice Tasks

1. Create a string with your full name and print the first and last characters using indexing.
2. Extract the first 5 characters of a string using slicing.
3. Concatenate your first name and last name with a space in between.
4. Use at least five different string methods on one string and print the results.
5. Create a message using an f-string that includes your name and age.
6. Reverse a string using slicing.

---

## What You Learned Today

- How to create strings (single, double, and triple quotes)
- String indexing and negative indexing
- String slicing (including step and reversing)
- Concatenation and repetition
- Important built-in string methods
- Modern string formatting with f-strings
- Best practices and common mistakes related to strings

Next topic: [Input and output](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-07/notes.md)
