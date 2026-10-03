# Day 5: Numbers and Basic Math Operations

## 1. What are Numbers and Math Operations in Python?

In Python, **numbers** are built-in data types used to store numeric values.

The main numeric types are:

- `int` (Integer) → Whole numbers (positive, negative, or zero)
- `float` → Decimal (floating-point) numbers
- `complex` → Numbers with a real part and an imaginary part

**Basic math operations** allow you to perform arithmetic calculations such as addition, subtraction, multiplication, division, and more.

Official reference:  
https://docs.python.org/3/tutorial/introduction.html#numbers

---

## 2. How Python Handles Numbers

Python treats numbers as objects and provides strong built-in support for mathematical operations.

Python supports:

- Arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- Standard mathematical order of operations (precedence)
- Built-in functions for type conversion
- Automatic handling of large integers (no overflow like in some other languages)

Python follows the standard mathematical precedence rules, often remembered as **PEMDAS**:

1. **P**arentheses
2. **E**xponents
3. **M**ultiplication / **D**ivision (from left to right)
4. **A**ddition / **S**ubtraction (from left to right)

---

## 3. Numeric Types in Detail

### 3.1 Integer (`int`)

Whole numbers without any decimal part. Integers can be positive, negative, or zero, and Python can handle extremely large integers without problem.

```python
a = 10
b = -5
big_number = 10**50          # Python handles this easily
print(type(a))               # <class 'int'>
```

---

### 3.2 Float (`float`)

Numbers that contain a decimal point. Floats are used when you need fractional values.

```python
price = 19.99
temperature = -2.5
pi_approx = 3.14159
print(type(price))           # <class 'float'>
```

---

### 3.3 Complex (`complex`)

Numbers that have a real part and an imaginary part (written with `j`).

```python
c = 2 + 3j
print(type(c))               # <class 'complex'>
print(c.real)                # 2.0
print(c.imag)                # 3.0
```

Complex numbers are less common in everyday programming but are useful in scientific and engineering applications.

---

## 4. Basic Math Operations

Here are the most important arithmetic operators in Python:

### 4.1 Addition (`+`)

```python
x = 10
y = 5
print(x + y)                 # 15
```

### 4.2 Subtraction (`-`)

```python
print(x - y)                 # 5
```

### 4.3 Multiplication (`*`)

```python
print(x * y)                 # 50
```

### 4.4 Division (`/`)

Always returns a **float**, even if the result is a whole number.

```python
print(x / y)                 # 2.0
print(7 / 2)                 # 3.5
```

### 4.5 Floor Division (`//`)

Returns the whole-number (integer) part of the division. It discards the decimal part.

```python
print(x // y)                # 2
print(7 // 2)                # 3
```

### 4.6 Modulus (`%`)

Returns the **remainder** after division.

```python
print(x % y)                 # 0
print(7 % 2)                 # 1
```

### 4.7 Exponentiation (`**`)

Raises a number to a power.

```python
print(x ** 2)                # 100
print(2 ** 3)                # 8
print(9 ** 0.5)              # 3.0 (square root)
```

---

## 5. Order of Operations (Precedence)

Python evaluates expressions following mathematical precedence. Use parentheses to control the order clearly.

```python
result = 2 + 3 * 4
print(result)                # 14  (multiplication first)

result_with_parentheses = (2 + 3) * 4
print(result_with_parentheses)  # 20
```

**Tip:** When in doubt, use parentheses. They make your intention clear to both Python and other programmers.

---

## 6. Type Conversion Between Numbers

You can convert between numeric types using built-in functions:

```python
a = 10
b = 3.9

print(float(a))              # 10.0
print(int(b))                # 3   (truncates the decimal part)
print(complex(a))            # (10+0j)
```

**Important notes:**
- `int()` truncates toward zero (it does not round).
- Converting a float to int loses the fractional part.
- You cannot convert a complex number directly to int or float without taking the real part first.

---

## 7. Do’s and Don’ts

### Do’s

- Use parentheses to make the order of operations clear
- Understand the difference between `/` (true division) and `//` (floor division)
- Use meaningful variable names for numbers
- Convert types explicitly when needed
- Test your calculations with `print()` while learning
- Prefer readability over very complex one-line expressions

### Don’ts

- Do **not** assume that `/` will return an integer
- Do **not** ignore operator precedence
- Do **not** mix incompatible types (e.g., string + number)
- Do **not** rely only on implicit type conversions
- Do **not** forget that floating-point numbers have limited precision

---

## 8. Industry Standards (PEP 8)

According to **PEP 8**:

- Put spaces around operators: `x + y` instead of `x+y`
- Keep mathematical expressions readable
- Avoid writing overly complex one-line calculations
- Break long calculations into smaller, clearer steps

PEP 8 reference:  
https://peps.python.org/pep-0008/#other-recommendations

Professional Python code prioritizes clarity over clever shortcuts.

---

## 9. Common Mistakes to Avoid

### 9.1 Integer Division Confusion

```python
print(5 / 2)     # 2.5   ← true division (float)
print(5 // 2)    # 2     ← floor division (int)
```

Many beginners expect `/` to behave like integer division. Remember the difference.

---

### 9.2 Floating-Point Precision Issues

```python
print(0.1 + 0.2)   # 0.30000000000000004
```

This happens because computers store floating-point numbers in binary, which cannot represent some decimal values exactly. For most everyday calculations this is fine, but be careful in financial or high-precision work.

---

### 9.3 Mixing Strings and Numbers

```python
age = "21"
# print(age + 5)          # TypeError
print(int(age) + 5)       # 26  ← correct way
```

Always convert the string to a number before performing arithmetic.

---

### 9.4 Forgetting Parentheses

```python
# Unclear
result = 10 + 5 * 2 - 3

# Clearer
result = 10 + (5 * 2) - 3
```

---

## Practice Tasks

1. Create two variables (one `int` and one `float`) and perform all seven basic math operations with them.
2. Calculate the area of a rectangle using variables for length and width.
3. Use floor division and modulus to find how many full weeks and leftover days are in 100 days.
4. Experiment with operator precedence by writing expressions with and without parentheses.
5. Convert a float to an integer and observe what happens to the decimal part.

---

## What You Learned Today

- The three main numeric types: `int`, `float`, and `complex`
- All basic arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- How Python follows mathematical order of operations (PEMDAS)
- How to convert between numeric types
- Industry best practices for writing clear math expressions
- Common numerical mistakes and how to avoid them

Next topic: [Strings and String Operations](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-06/notes.md)
