# Day 12: Logical Operators

## 1. Definition of the Topic

**Logical operators** in Python are used to combine multiple conditions in a single statement.  
They help evaluate whether **multiple expressions together are True or False**.

Python provides three logical operators:

- `and`
- `or`
- `not`

Logical operators are commonly used with **conditional statements (`if`, `elif`, `else`)** to build complex decision-making logic.

---

## 2. Detailed Explanation of the Topic

Logical operators allow programmers to test **multiple conditions at the same time**.

For example, a login system may require:

- correct username **and**
- correct password

Logical operators help express these relationships clearly.

---

### 2.1 The `and` Operator

The `and` operator returns **True only if both conditions are True**.

Syntax:

```python
condition1 and condition2
```

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```

Truth table:

| Condition A | Condition B | A and B |
|--------------|-------------|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

### 2.2 The `or` Operator

The `or` operator returns **True if at least one condition is True**.

Syntax:

```python
condition1 or condition2
```

Example:

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

Truth table:

| Condition A | Condition B | A or B |
|--------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

### 2.3 The `not` Operator

The `not` operator **reverses the boolean value**.

Syntax:

```python
not condition
```

Example:

```python
logged_in = False

if not logged_in:
    print("Please log in")
```

Truth table:

| Condition | not Condition |
|-----------|---------------|
| True | False |
| False | True |

---

### 2.4 Combining Multiple Logical Operators

Logical operators can be combined to form complex conditions.

Example:

```python
age = 25
country = "BD"

if age >= 18 and country == "BD":
    print("Eligible to vote")
```

---

### 2.5 Logical Operators with Numbers

Python treats some values as **True or False** automatically.

False values:

- `0`
- `None`
- `""` (empty string)
- `[]` (empty list)

Example:

```python
value = 0

if not value:
    print("Value is zero or empty")
```

---

### 2.6 Practical Example: Login System

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
```

---

## 3. Do's and Don'ts

### Do's

- Use logical operators to simplify multiple conditions
- Keep conditions readable
- Use parentheses when conditions become complex
- Combine logical operators carefully

### Don'ts

- Do NOT create overly long conditions
- Do NOT mix `and` and `or` without understanding precedence
- Do NOT ignore readability
- Do NOT repeat the same condition unnecessarily

---

## 4. Industry Standards

Professional Python developers follow these best practices.

### Follow PEP 8

- Use spaces around operators
- Keep lines readable
- Avoid overly long conditional statements

Example:

Bad:

```python
if age>=18 and country=="BD" and verified==True:
    print("Allowed")
```

Better:

```python
if age >= 18 and country == "BD" and verified:
    print("Allowed")
```

---

### Use Parentheses for Complex Logic

Example:

```python
age = 20
student = True

if (age >= 18 and student) or age >= 65:
    print("Discount eligible")
```

---

### Write Self-Explanatory Conditions

Example:

```python
is_adult = age >= 18
has_permission = True

if is_adult and has_permission:
    print("Access granted")
```

---

## 5. Mistakes to Avoid

### 5.1 Misusing `and` Instead of `or`

Bad:

```python
day = "Sunday"

if day == "Saturday" and day == "Sunday":
    print("Weekend")
```

Correct:

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

### 5.2 Forgetting Operator Precedence

Example:

```python
a = True
b = False
c = True

print(a or b and c)
```

Python evaluates `and` before `or`.

Better:

```python
print((a or b) and c)
```

---

### 5.3 Overly Complex Conditions

Bad:

```python
if age > 18 and country == "BD" and verified and not banned and active:
    print("Allowed")
```

Better:

```python
is_valid_user = age > 18 and country == "BD" and verified
if is_valid_user and not banned and active:
    print("Allowed")
```

---

## 6. Summary

Today you learned:

- What logical operators are
- How `and`, `or`, and `not` work
- Truth tables for logical operations
- How to combine conditions
- Industry best practices
- Common logical mistakes

Logical operators are essential for building **smart decision-making systems**, such as authentication systems, validations, filters, and business logic.

Next topic: [While loops]()
