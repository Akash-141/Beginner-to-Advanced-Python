# Day 3: Variables and Data Types in Python

## 1. What is a Variable?

A variable is a container used to store data.

Think of it like a labeled box. The label is the variable name, and the content inside the box is the value.

Example:

```python
name = "Akash"
```

Here:
- `name` is the variable
- `"Akash"` is the value stored inside it

---

## 2. Rules for Naming Variables

- Must start with a letter or underscore
- Cannot start with a number
- Can contain letters, numbers, and underscores
- Case-sensitive (age and Age are different)

Correct examples:

```python
age = 20
student_name = "Rahim"
_total = 500
```

Incorrect examples:

```python
2name = "Wrong"
student-name = "Wrong"
```

Reference:
https://docs.python.org/3/tutorial/introduction.html

---

## 3. What is a Data Type?

A data type tells Python what kind of value is stored in a variable.

Python automatically detects the data type when you assign a value.

---

## 4. Basic Data Types in Python

### String (str)

Used to store text.

```python
city = "Dhaka"
```

---

### Integer (int)

Used to store whole numbers.

```python
age = 25
```

---

### Float (float)

Used to store decimal numbers.

```python
price = 99.99
```

---

### Boolean (bool)

Represents True or False.

```python
is_student = True
```

---

## 5. Checking Data Type

You can check the type using the type() function.

```python
age = 25
print(type(age))
```

---

## 6. Reassigning Variables

Variables can be changed.

```python
score = 10
score = 20
print(score)
```

---

## 7. Dynamic Typing

Python is dynamically typed. You do not need to declare the type manually.

```python
x = 10
x = "Now I am text"
```

Official documentation:
https://docs.python.org/3/reference/datamodel.html

---

## Practice Tasks

1. Create a variable to store your name.
2. Create a variable to store your age.
3. Create a variable to store your GPA.
4. Create a boolean variable to represent whether you are a student.
5. Print all variables and their types.

---

## What You Learned Today

- What variables are
- Rules for naming variables
- Basic data types (str, int, float, bool)
- How to check data types
- What dynamic typing means
