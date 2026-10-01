# Day 3: Python Syntax and Indentation

## 1. What is Python Syntax and Indentation?

**Python syntax** refers to the set of rules that define how Python code must be written so the interpreter can understand and execute it correctly.

**Indentation** means the spaces (or tabs) at the beginning of a line of code. Unlike most other programming languages that use curly braces `{}` to define blocks of code, Python uses indentation to define code blocks.

This design choice makes Python code look clean and forces developers to write more readable programs.

Official reference:  
https://docs.python.org/3/tutorial/introduction.html

---

## 2. Key Characteristics of Python Syntax

Python is intentionally designed to be clean and readable. Because of this philosophy:

- Code is executed **line by line**
- Semicolons (`;`) are usually **not required**
- **Indentation is mandatory** (not optional)
- Readability is considered part of good Python style
- The language follows the principle: “There should be one obvious way to do it”

### What happens when rules are broken?

- If syntax rules are broken → Python raises a **SyntaxError**
- If indentation is wrong → Python raises an **IndentationError**

These errors stop the program from running until you fix them.

---

### 2.1 Basic Python Statement

The simplest form of a Python statement is a single line of code:

```python
print("Hello, Python")
```

Each complete instruction is called a **statement**.

---

### 2.2 Case Sensitivity

Python is **case-sensitive**. This means that uppercase and lowercase letters are treated as completely different.

```python
name = "Akash"
Name = "Paul"

print(name)   # Output: Akash
print(Name)   # Output: Paul
```

`name` and `Name` are two different variables. Mixing up the case is a very common beginner mistake.

---

### 2.3 Statements and New Lines

**Recommended style** (one statement per line):

```python
print("Line 1")
print("Line 2")
```

**Allowed but not recommended** (multiple statements on one line):

```python
print("Line 1"); print("Line 2")
```

Although the second version works, it reduces readability. Most professional Python code prefers one statement per line.

---

### 2.4 Comments in Python

Comments are notes that the Python interpreter **ignores**. They are written for humans to understand the code better.

**Single-line comment:**

```python
# This is a single-line comment
print("Hello")
```

**Multi-line comment** (technically a multi-line string, but commonly used as a comment):

```python
"""
This is a multi-line comment
used for longer explanations
or documentation
"""
```

You can also use multiple single-line comments:

```python
# This is line 1 of the comment
# This is line 2 of the comment
```

Reference:  
https://docs.python.org/3/tutorial/introduction.html#comments

---

## 3. Understanding Indentation in Depth

Indentation is the **leading whitespace** before a line of code. In Python, indentation is used to define **blocks** of code such as:

- `if` statements
- `for` and `while` loops
- Function definitions
- Class definitions
- `try` / `except` blocks

Whenever a line ends with a colon (`:`), the next line **must** be indented.

---

### 3.1 Correct Indentation Example

```python
age = 18

if age >= 18:
    print("You are an adult")
```

The `print` statement is indented, so Python knows it belongs inside the `if` block.

---

### 3.2 Incorrect Indentation Example

```python
age = 18

if age >= 18:
print("You are an adult")   # Missing indentation
```

This will raise:

```
IndentationError: expected an indented block
```

---

### 3.3 Indentation in Loops

```python
for i in range(3):
    print("Number:", i)
```

Everything indented under the `for` line belongs to the loop body and will run multiple times.

---

### 3.4 Nested Indentation

You can have blocks inside other blocks. Each new level needs additional indentation:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("You must be 18 or older")
```

Each deeper level is indented further (usually by another 4 spaces).

---

## 4. Do’s and Don’ts

### Do’s

- Use **exactly 4 spaces** for each indentation level
- Keep indentation consistent throughout the entire file
- Follow **PEP 8** style guidelines
- Use comments to explain complex or non-obvious logic
- Use a modern code editor (VS Code, PyCharm, etc.) that helps with indentation
- Configure your editor to convert tabs into spaces

### Don’ts

- Do **not** mix tabs and spaces in the same file
- Do **not** skip indentation after a colon (`:`)
- Do **not** over-indent or under-indent randomly
- Do **not** write multiple statements on one line unless necessary
- Do **not** ignore IndentationError messages — fix them immediately

---

## 5. Industry Standards (PEP 8)

According to **PEP 8** (the official Python style guide):

- Use **4 spaces** per indentation level
- Prefer **one statement per line**
- Keep code readable and consistent
- Never mix tabs and spaces

Reference:  
https://peps.python.org/pep-0008/#indentation

Almost every professional Python team and open-source project follows PEP 8. Learning these rules early will make your code look professional and easier for others to read.

---

## 6. Common Mistakes to Avoid

### Mixing Tabs and Spaces

This is one of the most frustrating errors for beginners. Always configure your editor to insert **spaces** instead of tabs.

### Missing Indentation After a Colon

```python
# Wrong
if True:
print("Hello")
```

### Unexpected Indentation

```python
# Wrong – this line is indented without a reason
    print("Hello")
```

### Inconsistent Indentation Levels

```python
# Wrong
if True:
    print("Level 1")
      print("Wrong level")   # Different number of spaces
```

Always keep the same number of spaces at each level.

---

## Practice Tasks

1. Write a simple `if` statement that checks whether a number is positive and prints a message.
2. Create a `for` loop that prints numbers from 0 to 4 with proper indentation.
3. Write a nested `if` example (one `if` inside another).
4. Intentionally create an IndentationError and then fix it.
5. Add both single-line and multi-line comments to one of your programs.

---

## What You Learned Today

- What Python syntax is and why it matters
- Why Python is case-sensitive
- How to write single-line and multi-line comments
- What indentation means and why it is mandatory in Python
- How indentation defines code blocks (`if`, loops, etc.)
- The industry standard of using 4 spaces
- Common indentation mistakes and how to avoid them
- The importance of following PEP 8

Next topic: [Variables and Data Types](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-04/notes.md)
