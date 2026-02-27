# Day 4: Variables and Data Types in Python

## 1. Definition of Variables and Data Types

A **variable** in Python is a named container used to store data values.

A **data type** defines the kind of value a variable holds and what operations can be performed on it.

Official reference:
https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator

---

## 2. Detailed Explanation of the Topic

Python is dynamically typed, which means:

- You do NOT need to declare the variable type explicitly
- Python automatically detects the data type
- Variables can change type during execution

Variables are created when you assign a value using the equals sign `=`.

---

### 2.1 Creating Variables

```python
name = "Akash"
age = 21
height = 5.8
```

Python automatically assigns the correct data type.

---

### 2.2 Rules for Naming Variables

✅ Valid:

```python
user_name = "Akash"
_age = 21
totalScore = 95
```

❌ Invalid:

```python
2name = "Akash"   # cannot start with number
user-name = "Akash"  # hyphen not allowed
class = "Python"  # reserved keyword
```

Reference:
https://docs.python.org/3/reference/lexical_analysis.html#identifiers

---

## 3. Common Built-in Data Types

### 3.1 Integer (int)

Whole numbers without decimals.

```python
age = 25
print(type(age))
```

---

### 3.2 Float (float)

Numbers with decimal points.

```python
price = 19.99
print(type(price))
```

---

### 3.3 String (str)

Text data enclosed in quotes.

```python
message = "Hello, Python"
print(type(message))
```

---

### 3.4 Boolean (bool)

Represents True or False.

```python
is_logged_in = True
print(type(is_logged_in))
```

---

## 4. Type Conversion (Casting)

Python allows converting one data type to another.

```python
age = 21
age_str = str(age)

print(type(age))
print(type(age_str))
```

---

## 5. Multiple Assignment

Python allows assigning multiple variables in one line.

```python
x, y, z = 10, 20, 30
print(x, y, z)
```

---

## 6. Do's and Don'ts

### Do's

- Use meaningful variable names
- Follow snake_case naming style
- Keep variable names readable
- Use built-in types properly
- Check types using `type()` when learning

### Don'ts

- Do NOT start variable names with numbers
- Do NOT use Python keywords as variable names
- Do NOT use unclear names like `a`, `b`, `x1`
- Do NOT overuse type conversions
- Do NOT mix unrelated data in one variable

---

## 7. Industry Standards

According to **PEP 8**:

- Use **snake_case** for variable names
- Use lowercase letters
- Separate words with underscores
- Keep names descriptive but concise

PEP 8 reference:
https://peps.python.org/pep-0008/#naming-conventions

Professional Python code always follows these conventions.

---

## 8. Mistakes to Avoid

### Mixing Data Types Unintentionally

```python
age = "21"
result = age + 5  # TypeError
```

Always ensure compatible types.

---

### Using Poor Variable Names

Bad:

```python
x = 25
```

Better:

```python
user_age = 25
```

---

### Forgetting Python is Dynamically Typed

```python
value = 10
value = "ten"  # type changed
```

Be careful when reassigning variables.

---

## Summary

Today you learned:

- What variables are
- What data types are
- How Python assigns types automatically
- Common built-in data types
- Type conversion
- Industry naming standards
- Common mistakes to avoid

