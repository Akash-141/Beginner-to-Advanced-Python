# Day 4: Numbers and Basic Mathematical Operations

## 1. Numbers in Python

Python mainly uses two numeric types for basic math:

- int → Whole numbers (e.g., 5, 100, -3)
- float → Decimal numbers (e.g., 3.14, 0.5, -2.7)

Example:

```python
a = 10
b = 3.5

print(type(a))
print(type(b))
```

Official documentation:
https://docs.python.org/3/tutorial/introduction.html#numbers

---

## 2. Arithmetic Operators

Python supports standard mathematical operations.

### Addition (+)

```python
result = 5 + 3
print(result)
```

### Subtraction (-)

```python
result = 10 - 4
print(result)
```

### Multiplication (*)

```python
result = 6 * 2
print(result)
```

### Division (/)

```python
result = 10 / 2
print(result)
```

Important:
Division (/) always returns a float.

---

## 3. Floor Division (//)

Floor division removes the decimal part and returns the largest whole number less than or equal to the result.

```python
result = 10 // 3
print(result)
```

---

## 4. Modulus (%)

Modulus returns the remainder after division.

```python
result = 10 % 3
print(result)
```

---

## 5. Exponentiation (**)

Used for powers.

```python
result = 2 ** 3
print(result)
```

---

## 6. Order of Operations

Python follows standard mathematical rules:

1. Parentheses ()
2. Exponentiation **
3. Multiplication, Division, Floor Division, Modulus
4. Addition and Subtraction

Example:

```python
result = 2 + 3 * 4
print(result)
```

Using parentheses:

```python
result = (2 + 3) * 4
print(result)
```

---

## 7. Mixing Integers and Floats

When you mix int and float, the result becomes float.

```python
x = 5 + 2.0
print(x)
print(type(x))
```

---

## Practice Tasks

1. Add two numbers and print the result.
2. Subtract two numbers.
3. Multiply two numbers.
4. Divide two numbers.
5. Find the remainder of 17 divided by 5.
6. Calculate 3 raised to the power 4.
7. Try a complex expression using parentheses.

---

## What You Learned Today

- int and float data types
- Arithmetic operators (+, -, *, /)
- Floor division (//)
- Modulus (%)
- Exponentiation (**)
- Order of operations
