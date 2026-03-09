# Day 11: elif and Nested Conditions

## 1. Definition of the Topic

In Python, **elif (else-if)** and **nested conditions** are used when a program must evaluate **multiple conditions** or **conditions inside other conditions**.

- **elif** allows checking multiple conditions sequentially.
- **Nested conditions** allow placing an `if` statement inside another `if` block.

These tools make programs more flexible and allow complex decision-making.

---

## 2. Detailed Explanation of the Topic

### 2.1 The elif Statement

The `elif` statement stands for **else if**.

It allows Python to check **multiple conditions in sequence**. Python evaluates conditions **from top to bottom**, and the first true condition executes.

### Syntax

```python
if condition1:
    # block of code
elif condition2:
    # block of code
elif condition3:
    # block of code
else:
    # default block
```

Example:

```python
score = 82

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")
```

Python stops checking conditions after the **first True condition**.

---

### 2.2 Why Use elif Instead of Multiple if Statements

Bad practice:

```python
score = 85

if score >= 90:
    print("Grade A")

if score >= 80:
    print("Grade B")
```

This prints multiple results if multiple conditions are true.

Correct approach:

```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
```

Only **one block executes**.

---

### 2.3 Nested Conditions

A **nested condition** means placing one `if` statement inside another.

Example:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```

---

### 2.4 Nested if-else Structure

Example:

```python
number = 10

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is negative")
```

---

### 2.5 Combining elif with Nested Conditions

Example:

```python
temperature = 30
raining = False

if temperature > 35:
    print("Too hot outside")
elif temperature > 25:
    if raining:
        print("Warm but rainy")
    else:
        print("Perfect weather")
else:
    print("Cool weather")
```

---

### 2.6 Practical Example: Login Verification

```python
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")
```

---

## 3. Do's and Don'ts

### Do's

- Use `elif` when checking multiple related conditions.
- Keep nested conditions minimal and readable.
- Use proper indentation.
- Place the most specific conditions first.
- Write meaningful variable names.

### Don'ts

- Do NOT use multiple `if` statements when `elif` is required.
- Do NOT create deeply nested structures (more than 3–4 levels).
- Do NOT ignore readability.
- Do NOT repeat the same condition unnecessarily.

---

## 4. Industry Standards

Professional Python developers follow these guidelines:

### Follow PEP 8

- 4-space indentation
- Clear condition structure
- Avoid overly complex nested logic

### Prefer Flat Logic

Bad:

```python
if age >= 18:
    if country == "BD":
        if verified:
            print("Allowed")
```

Better:

```python
if age >= 18 and country == "BD" and verified:
    print("Allowed")
```

### Use Early Return in Functions

Example:

```python
def check_login(user, password):
    if user != "admin":
        return "User not found"
    if password != "1234":
        return "Wrong password"
    return "Login successful"

print(check_login("admin", "1234"))
```

---

## 5. Mistakes to Avoid

### 5.1 Too Many Nested Conditions

Bad:

```python
if a > 0:
    if b > 0:
        if c > 0:
            print("All positive")
```

Better:

```python
if a > 0 and b > 0 and c > 0:
    print("All positive")
```

---

### 5.2 Wrong Condition Order

Bad:

```python
score = 95

if score >= 50:
    print("Pass")
elif score >= 90:
    print("Excellent")
```

Correct:

```python
if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
```

---

### 5.3 Missing Indentation

Bad:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## 6. Summary

Today you learned:

- What `elif` is and when to use it
- How Python checks conditions sequentially
- How nested conditions work
- When nested conditions are useful
- Best practices used in industry
- Common mistakes developers make

Understanding `elif` and nested conditions helps you build **complex decision-making logic**, which is essential for real-world Python programs.

Next topic: [Logical Operators](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-12/notes.md)

