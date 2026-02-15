# Day 6: Conditional Statements (if, elif, else)

## 1. Why Conditionals?

Conditional statements allow your program to make decisions.

They execute different code depending on whether a condition is True or False.

Official documentation:
https://docs.python.org/3/tutorial/controlflow.html#if-statements

---

## 2. The if Statement

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

The code inside the if block runs only if the condition is True.

---

## 3. if-else

Use else to run code when the condition is False.

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 4. if-elif-else

Use elif when checking multiple conditions.

```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")
```

---

## 5. Comparison Operators

- ==  Equal to
- !=  Not equal to
- >   Greater than
- <   Less than
- >=  Greater than or equal to
- <=  Less than or equal to

Example:

```python
x = 5

if x == 5:
    print("x is 5")
```

---

## 6. Logical Operators

- and  → Both conditions must be True
- or   → At least one condition must be True
- not  → Reverses the condition

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```

---

## 7. Indentation Matters

Python uses indentation (spaces) to define blocks of code.

Incorrect indentation will cause errors.

---

## Practice Tasks

1. Write a program that checks if a number is positive or negative.
2. Check if a number is even or odd.
3. Create a simple grading system.
4. Use logical operators in a condition.
5. Ask the user for input and respond based on the value.

---

## What You Learned Today

- if statements
- else statements
- elif statements
- Comparison operators
- Logical operators
- Importance of indentation
