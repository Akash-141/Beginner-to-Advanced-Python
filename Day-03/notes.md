# Day 3: Python Syntax and Indentation

## 1. Definition of Python Syntax and Indentation

**Python syntax** refers to the rules that define how Python programs must be written so the interpreter can understand them.

**Indentation** in Python means the spaces at the beginning of a line of code. Unlike many other languages that use curly braces `{}`, Python uses indentation to define code blocks.

Official reference:
https://docs.python.org/3/tutorial/introduction.html

---

## 2. Detailed Explanation of the Topic

Python is designed to be clean and readable. Because of this:

- Python executes code line by line
- Semicolons are usually not required
- Indentation is mandatory
- Readability is part of Python’s philosophy

If syntax rules are broken, Python raises a **SyntaxError**.  
If indentation is wrong, Python raises an **IndentationError**.

---

### 2.1 Basic Python Statement

```python
print("Hello, Python")
```

---

### 2.2 Case Sensitivity

Python is case sensitive. Uppercase and lowercase names are different.

```python
name = "Akash"
Name = "Paul"

print(name)
print(Name)
```

---

### 2.3 Statements and New Lines

Recommended:

```python
print("Line 1")
print("Line 2")
```

Allowed but not recommended:

```python
print("Line 1"); print("Line 2")
```

---

### 2.4 Comments in Python

Single-line comment:

```python
# This is a comment
print("Hello")
```

Multi-line comment:

```python
"""
This is a multi-line comment
used for longer explanations
"""
```

Reference:
https://docs.python.org/3/tutorial/introduction.html#comments

---

## 3. Understanding Indentation

Indentation is the leading whitespace before code. It defines blocks such as:

- if statements
- loops
- functions
- classes

---

### 3.1 Correct Indentation Example

```python
age = 18

if age >= 18:
    print("You are an adult")
```

---

### 3.2 Incorrect Indentation Example

```python
age = 18

if age >= 18:
print("You are an adult")
```

This causes:

```
IndentationError: expected an indented block
```

---

### 3.3 Indentation in Loops

```python
for i in range(3):
    print("Number:", i)
```

---

### 3.4 Nested Indentation

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```

---

## 4. Do's and Don'ts

### Do's

- Use **4 spaces** for indentation
- Keep indentation consistent
- Follow PEP 8
- Use comments to explain complex logic
- Use a proper code editor

### Don'ts

- Do NOT mix tabs and spaces
- Do NOT skip indentation after a colon
- Do NOT over-indent
- Do NOT write multiple statements per line
- Do NOT ignore indentation errors

---

## 5. Industry Standards

According to **PEP 8 (Python style guide)**:

- Use 4 spaces per indentation level
- Prefer one statement per line
- Keep code readable and consistent

Reference:
https://peps.python.org/pep-0008/#indentation

Professional teams follow PEP 8 to maintain clean and maintainable code.

---

## 6. Mistakes to Avoid

### Mixing Tabs and Spaces

Always configure your editor to insert spaces only.

---

### Missing Indentation After Colon

Wrong:

```python
if True:
print("Hello")
```

---

### Unexpected Indentation

Wrong:

```python
    print("Hello")
```

---

### Inconsistent Indentation

Keep indentation uniform across the project.

---

## Summary

Today you learned:

- What Python syntax is
- Why Python is case sensitive
- How comments work
- What indentation means
- Why indentation is mandatory
- The industry standard 4-space rule
- Common mistakes to avoid

Next topic: Variables and Data Types
