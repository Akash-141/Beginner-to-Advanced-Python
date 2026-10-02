# Day 4: Variables and Data Types in Python

## 1. What are Variables and Data Types?

A **variable** in Python is a named container used to store data values in memory. Think of it as a labeled box that holds a value so you can use it later in your program.

A **data type** defines the kind of value a variable holds (number, text, true/false, etc.) and determines what operations you can perform on that value.

Official reference:  
https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator

---

## 2. How Variables Work in Python

Python is a **dynamically typed** language. This means:

- You do **not** need to declare the type of a variable in advance
- Python automatically detects the data type when you assign a value
- The same variable can change its type later in the program

Variables are created the moment you assign a value using the equals sign `=`.

```python
name = "Akash"      # Python knows this is a string
age = 21            # Python knows this is an integer
height = 5.8        # Python knows this is a float
```

You can check the type of any variable using the built-in `type()` function:

```python
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>
```

---

### 2.1 Creating Variables

```python
name = "Akash"
age = 25
height = 5.11
is_student = True
```

Python automatically assigns the correct data type based on the value you provide.

---

### 2.2 Rules for Naming Variables

Variable names must follow these rules:

**Valid examples:**

```python
user_name = "Akash"
_age = 21
total_score = 95
firstName = "Akash"   # works, but not recommended style
```

**Invalid examples:**

```python
2name = "Akash"       # cannot start with a number
user-name = "Akash"   # hyphen is not allowed
class = "Python"      # 'class' is a reserved keyword
```

**Quick rules summary:**
- Must start with a letter (a-z, A-Z) or an underscore `_`
- Can contain letters, numbers, and underscores
- Cannot be a Python reserved keyword (`if`, `for`, `class`, `True`, etc.)
- Are case-sensitive (`age` and `Age` are different)

Reference:  
https://docs.python.org/3/reference/lexical_analysis.html#identifiers

---

## 3. Common Built-in Data Types

Python has several built-in data types. Here are the most important ones for beginners:

### 3.1 Integer (`int`)

Whole numbers without decimal points (positive or negative).

```python
age = 25
temperature = -5
print(type(age))          # <class 'int'>
```

---

### 3.2 Float (`float`)

Numbers that contain a decimal point.

```python
price = 19.99
pi = 3.14159
print(type(price))        # <class 'float'>
```

---

### 3.3 String (`str`)

Text data. Strings must be enclosed in single quotes `'...'` or double quotes `"..."`.

```python
message = "Hello, Python"
name = 'Akash'
print(type(message))      # <class 'str'>
```

You can also use triple quotes for multi-line strings:

```python
long_text = """This is a
multi-line
string"""
```

---

### 3.4 Boolean (`bool`)

Represents one of two values: `True` or `False` (note the capital first letter).

```python
is_logged_in = True
has_permission = False
print(type(is_logged_in)) # <class 'bool'>
```

Booleans are very useful in conditions and decision-making.

---

### 3.5 Other Useful Types (Preview)

- **List** → ordered collection: `numbers = [1, 2, 3]`
- **Tuple** → immutable collection: `point = (10, 20)`
- **Dictionary** → key-value pairs: `person = {"name": "Akash", "age": 21}`
- **NoneType** → represents “no value”: `result = None`

You will learn these in more detail in later lessons.

---

## 4. Type Conversion (Casting)

Sometimes you need to convert a value from one data type to another. This is called **type conversion** or **casting**.

```python
age = 21
age_str = str(age)        # Convert integer to string

print(type(age))          # <class 'int'>
print(type(age_str))      # <class 'str'>
```

Common conversion functions:

| Function   | Converts to | Example                  |
|------------|-------------|--------------------------|
| `int()`    | Integer     | `int("25")` → `25`       |
| `float()`  | Float       | `float("3.14")` → `3.14` |
| `str()`    | String      | `str(100)` → `"100"`     |
| `bool()`   | Boolean     | `bool(1)` → `True`       |

**Be careful:** Converting incompatible values will raise an error.

```python
int("hello")   # ValueError
```

---

## 5. Multiple Assignment

Python allows you to assign values to multiple variables in a single line:

```python
x, y, z = 10, 20, 30
print(x, y, z)          # 10 20 30
```

You can also assign the same value to multiple variables:

```python
a = b = c = 0
print(a, b, c)          # 0 0 0
```

This feature is useful and makes code more concise.

---

## 6. Do’s and Don’ts

### Do’s

- Use **meaningful** and descriptive variable names
- Follow **snake_case** naming style (`user_age`, `total_score`)
- Keep names readable and consistent
- Use the built-in data types correctly
- Check types with `type()` while learning
- Convert types explicitly when needed

### Don’ts

- Do **not** start variable names with numbers
- Do **not** use Python reserved keywords as variable names
- Do **not** use unclear names like `a`, `b`, `x1`, `temp`
- Do **not** overuse type conversions
- Do **not** mix completely unrelated data in one variable
- Do **not** rely on dynamic typing without understanding it

---

## 7. Industry Standards (PEP 8)

According to **PEP 8** (the official Python style guide):

- Use **snake_case** for variable and function names
- Use lowercase letters
- Separate words with underscores
- Keep names descriptive but not too long
- Avoid single-letter names except in very short loops

PEP 8 reference:  
https://peps.python.org/pep-0008/#naming-conventions

Professional Python projects and teams almost always follow these naming conventions.

---

## 8. Common Mistakes to Avoid

### Mixing Data Types Unintentionally

```python
age = "21"          # This is a string, not a number
result = age + 5    # TypeError: can only concatenate str to str
```

Always make sure the types are compatible before performing operations.

---

### Using Poor Variable Names

**Bad:**

```python
x = 25
y = "Akash"
```

**Better:**

```python
user_age = 25
user_name = "Akash"
```

---

### Forgetting That Python is Dynamically Typed

```python
value = 10
value = "ten"       # Type changed from int to str
```

This is allowed, but it can make your code harder to understand and debug. Be intentional when reassigning variables.

---

### Forgetting Quotes for Strings

```python
name = Akash        # NameError (Akash is treated as a variable)
name = "Akash"      # Correct
```

---

## Practice Tasks

1. Create variables for your name, age, height, and whether you are a student. Print each variable and its type.
2. Convert an integer to a string and a string (containing a number) to an integer.
3. Use multiple assignment to create three variables in one line.
4. Try to create a variable with an invalid name and observe the error.
5. Write a small program that stores a price as a float and prints a message using that price.

---

## What You Learned Today

- What variables are and how they store data
- What data types are and why they matter
- How Python automatically detects types (dynamic typing)
- The most common built-in data types: `int`, `float`, `str`, `bool`
- How to convert between data types
- How to assign multiple variables at once
- Industry naming standards (snake_case + PEP 8)
- Common mistakes and how to avoid them

Next topic: [Numbers and Basic Math Operations](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-05/notes.md)
