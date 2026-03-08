# Day 10: Conditional Statements (if, else)

## 1. Definition of the Topic

**Conditional statements** allow a Python program to make decisions based on conditions.

They control the flow of execution depending on whether a condition is **True** or **False**.

Python provides the following decision-making keywords:

- `if`
- `else`
- `elif` (else-if)

These are fundamental for building logical, interactive, and real-world programs.

---

## 2. Detailed Explanation of the Topic

Programs often need to behave differently depending on input or data. Conditional statements make this possible.

### Basic Syntax

```python
if condition:
    # code runs if condition is True
else:
    # code runs if condition is False
```

The condition must evaluate to a boolean value (`True` or `False`).

---

### 2.1 The if Statement

The `if` statement runs a block of code only when the condition is True.

Example:

```python
age = 18

if age >= 18:
    print("You are eligible to vote")
```

If the condition is False, nothing happens.

---

### 2.2 The else Statement

The `else` block runs when the `if` condition is False.

Example:

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

Only one block will execute.

---

### 2.3 The elif Statement

`elif` allows checking multiple conditions.

Example:

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")
```

Python checks conditions from top to bottom.

---

### 2.4 Using Comparison Operators

Common operators used in conditions:

- `==` equal to  
- `!=` not equal  
- `>` greater than  
- `<` less than  
- `>=` greater than or equal  
- `<=` less than or equal  

Example:

```python
num = 10

if num == 10:
    print("Number is ten")
```

---

### 2.5 Using Logical Operators

You can combine conditions using:

- `and`
- `or`
- `not`

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
```

---

### 2.6 Nested if Statements

You can place an `if` inside another `if`.

Example:

```python
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
```

---

### 2.7 Short if (Ternary Operator)

Python supports one-line conditional expressions.

Example:

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

---

## 3. Do's and Don'ts

### ✅ Do's

- Use proper indentation (4 spaces)
- Keep conditions simple and readable
- Use meaningful variable names
- Order conditions logically (most specific first)
- Use `elif` instead of multiple separate `if`s when appropriate

### ❌ Don'ts

- Do NOT forget the colon `:` after conditions
- Do NOT mix tabs and spaces
- Do NOT write overly complex conditions in one line
- Do NOT duplicate condition checks unnecessarily
- Do NOT ignore edge cases

---

## 4. Industry Standards

Professional Python developers follow these practices:

### ✔ Follow PEP 8

- 4-space indentation
- Clear spacing around operators
- Readable condition formatting

### ✔ Keep Conditions Readable

Bad:

```python
if age>=18 and has_id==True and country=="BD":
    print("Allowed")
```

Good:

```python
if age >= 18 and has_id and country == "BD":
    print("Allowed")
```

### ✔ Prefer Early Returns in Functions

Example:

```python
def check_even(number):
    if number % 2 != 0:
        return "Odd"
    return "Even"

print(check_even(4))
```

---

## 5. Mistakes to Avoid

### ❌ 5.1 Missing Colon

```python
# if age >= 18   ❌ SyntaxError
#     print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

### ❌ 5.2 Wrong Indentation

```python
age = 20

if age >= 18:
print("Adult")  # ❌ IndentationError
```

---

### ❌ 5.3 Using = Instead of ==

```python
# if age = 18:  ❌ SyntaxError
#     print("Equal")
```

Correct:

```python
if age == 18:
    print("Equal")
```

---

### ❌ 5.4 Overusing Nested if

Bad:

```python
if age >= 18:
    if age < 60:
        print("Working age")
```

Better:

```python
if 18 <= age < 60:
    print("Working age")
```

---

## 6. Summary

Today you learned:

- What conditional statements are
- How `if`, `else`, and `elif` work
- How to use comparison and logical operators
- Nested conditions
- Ternary operator
- Industry best practices
- Common beginner mistakes

Conditional statements are the **brain of decision-making** in Python programs.

Next topic: [elif and nested conditions](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-11/notes.md)

