# Day 5: Numbers and Basic Math Operations

## 1. Definition of the Topic

In Python, **numbers** are built-in data types used to store numeric values.

The main numeric types are:

- `int` (Integer) → Whole numbers
- `float` → Decimal numbers
- `complex` → Numbers with real and imaginary parts

**Basic math operations** allow you to perform arithmetic calculations such as addition, subtraction, multiplication, and division.

Official reference:
https://docs.python.org/3/tutorial/introduction.html#numbers

---

## 2. Detailed Explanation of the Topic

Python treats numbers as objects and provides built-in support for mathematical operations.

Python supports:

- Arithmetic operators
- Order of operations
- Built-in math functions
- Type conversion between numeric types

Python follows standard mathematical precedence rules (PEMDAS):

1. Parentheses
2. Exponents
3. Multiplication / Division
4. Addition / Subtraction

---

## 3. Numeric Types

### 3.1 Integer (int)

Whole numbers without decimals.

```python
a = 10
b = -5
print(type(a))
```

---

### 3.2 Float (float)

Numbers with decimal points.

```python
price = 19.99
temperature = -2.5
print(type(price))
```

---

### 3.3 Complex (complex)

Numbers with a real and imaginary part.

```python
c = 2 + 3j
print(type(c))
```

---

## 4. Basic Math Operations

### 4.1 Addition (+)

```python
x = 10
y = 5
print(x + y)
```

---

### 4.2 Subtraction (-)

```python
print(x - y)
```

---

### 4.3 Multiplication (*)

```python
print(x * y)
```

---

### 4.4 Division (/)

Always returns a float.

```python
print(x / y)
```

---

### 4.5 Floor Division (//)

Returns whole number result.

```python
print(x // y)
```

---

### 4.6 Modulus (%)

Returns remainder.

```python
print(x % y)
```

---

### 4.7 Exponent (**)

Power operation.

```python
print(x ** 2)
```

---

## 5. Order of Operations

```python
result = 2 + 3 * 4
print(result)

result_with_parentheses = (2 + 3) * 4
print(result_with_parentheses)
```

---

## 6. Type Conversion Between Numbers

```python
a = 10
b = 3

print(float(a))
print(int(3.9))
```

---

## 7. Do's and Don'ts

### Do's

- Use parentheses for clarity
- Understand division differences (`/` vs `//`)
- Use meaningful variable names
- Convert types carefully
- Test calculations with print()

### Don'ts

- Do NOT assume `/` returns integer
- Do NOT ignore operator precedence
- Do NOT mix incompatible types
- Do NOT rely on implicit conversions
- Do NOT forget about floating-point precision

---

## 8. Industry Standards

According to **PEP 8**:

- Use spaces around operators: `x + y`
- Keep expressions readable
- Avoid overly complex one-line expressions
- Break long calculations into steps

PEP 8 reference:
https://peps.python.org/pep-0008/#other-recommendations

Professional code prioritizes clarity over clever shortcuts.

---

## 9. Mistakes to Avoid

### 9.1 Integer Division Confusion

```python
print(5 / 2)   # 2.5
print(5 // 2)  # 2
```

---

### 9.2 Floating-Point Precision Issues

```python
print(0.1 + 0.2)
```

This may not return exactly 0.3 due to floating-point representation.

---

### 9.3 Mixing Strings and Numbers

```python
age = "21"
# print(age + 5)  # TypeError
```

Always convert before calculation.

---

## Summary

Today you learned:

- Numeric data types (`int`, `float`, `complex`)
- Basic arithmetic operators
- Order of operations
- Type conversion
- Industry best practices
- Common numerical mistakes

Next topic: [Strings and String Operations](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-06/notes.md)
