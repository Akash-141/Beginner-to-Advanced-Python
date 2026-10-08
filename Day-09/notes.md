# Day 9: Type Casting

## 1. What is Type Casting?

**Type casting** (also called type conversion) is the process of converting a value from one data type into another.

In Python, you perform type casting explicitly using built-in functions such as:

- `int()`
- `float()`
- `str()`
- `bool()`
- `list()`
- `tuple()`
- `set()`

Python is a dynamically typed language, which means it automatically detects the type of a variable when you assign a value. However, Python does **not** automatically convert incompatible types during operations. That is why we often need to cast types ourselves.

---

## 2. Why Type Casting is Necessary

Python will raise an error if you try to perform operations between incompatible types.

Example of a problem:

```python
num = "10"
# print(num + 5)   # TypeError: can only concatenate str (not "int") to str
```

Here `"10"` is a string and `5` is an integer. They cannot be added directly.

**Solution with type casting:**

```python
num = "10"
converted_num = int(num)
print(converted_num + 5)   # 15
```

Type casting is especially important when:
- Working with user input (`input()` always returns a string)
- Combining numbers and text
- Preparing data for calculations or storage
- Converting between collections (list, tuple, set)

---

## 3. Common Type Casting Functions

### 3.1 Converting to Integer (`int()`)

The `int()` function converts a value to an integer. When converting a float, it **truncates** (removes) the decimal part — it does not round.

```python
x = 5.9
print(int(x))          # 5

age = "21"
print(int(age))        # 21
```

**Invalid conversion** raises a `ValueError`:

```python
# print(int("hello"))  # ValueError: invalid literal for int()
```

---

### 3.2 Converting to Float (`float()`)

The `float()` function converts a value to a floating-point number.

```python
num = 10
print(float(num))      # 10.0

price = "19.99"
print(float(price))    # 19.99
```

---

### 3.3 Converting to String (`str()`)

The `str()` function converts almost any value into a string. This is very useful when you want to combine numbers with text.

```python
number = 100
print(str(number))     # "100"

age = 25
print("I am " + str(age) + " years old")
```

Using an f-string is usually cleaner:

```python
print(f"I am {age} years old")
```

---

### 3.4 Converting to Boolean (`bool()`)

In Python, the following values are considered **False**:

- `0`
- `0.0`
- `""` (empty string)
- `None`
- Empty collections (`[]`, `()`, `{}`, `set()`)

Everything else is considered **True**.

```python
print(bool(0))         # False
print(bool(1))         # True
print(bool(""))        # False
print(bool("Python"))  # True
print(bool("False"))   # True  (non-empty string)
```

---

### 3.5 Converting Between Collections

You can convert between lists, tuples, sets, and even strings.

```python
numbers = [1, 2, 3, 3]
print(set(numbers))    # {1, 2, 3}  (duplicates removed)

text = "hello"
print(list(text))      # ['h', 'e', 'l', 'l', 'o']

values = (1, 2, 3)
print(list(values))    # [1, 2, 3]
```

---

## 4. Type Casting with User Input

Remember that `input()` **always returns a string**. You must cast it if you need a number.

```python
age = input("Enter your age: ")
print(type(age))               # <class 'str'>

age = int(input("Enter your age: "))
print("Next year you will be", age + 1)
```

For decimal values:

```python
height = float(input("Enter your height: "))
print(f"Your height is {height} meters")
```

---

## 5. Do’s and Don’ts

### Do’s

- Always check or know the original data type before casting
- Use `int()` or `float()` when you need numeric values from user input
- Use `str()` when combining numbers with text
- Handle potential errors with `try-except`
- Understand how boolean conversion works (especially with strings)
- Prefer f-strings for clean output instead of heavy string concatenation

### Don’ts

- Do **not** assume that a string containing digits behaves like a number
- Do **not** try to cast invalid strings (e.g., `"hello"`) to numbers
- Do **not** ignore possible `ValueError` exceptions
- Do **not** overuse casting when it is not needed
- Do **not** forget that `int("12.5")` will fail (convert to float first)

---

## 6. Industry Standards and Best Practices

Professional Python developers usually:

- Validate input before casting
- Use `try-except` blocks for safe conversions
- Avoid unnecessary type conversions
- Write clear and readable conversion logic
- Prefer explicit casting over relying on implicit behavior

**Safe conversion example:**

```python
user_input = "25"

try:
    age = int(user_input)
    print(f"Next year you will be {age + 1}")
except ValueError:
    print("Invalid input. Please enter a number.")
```

This pattern prevents the program from crashing when the user enters invalid data.

---

## 7. Common Mistakes to Avoid

### 7.1 Forgetting That `input()` Returns a String

```python
age = input("Enter age: ")
# print(age + 1)          # TypeError

# Correct way
age = int(input("Enter age: "))
print(age + 1)
```

### 7.2 Invalid Numeric Conversion

```python
# int("12.5")             # ValueError

# Correct way
print(int(float("12.5"))) # 12
```

### 7.3 Misunderstanding Boolean Conversion

```python
print(bool("False"))      # True  (because it is a non-empty string)
print(bool(""))           # False
```

### 7.4 Truncation vs Rounding

```python
print(int(5.9))           # 5  (truncates, does not round)
```

If you need proper rounding, use the `round()` function first.

---

## 8. Practice Tasks

1. Ask the user for their age, convert it to an integer, and print how old they will be in 5 years.
2. Convert the string `"3.14"` into a float and then into an integer. Observe the result.
3. Create a list with duplicate numbers and convert it to a set to remove duplicates.
4. Convert a number to a string and concatenate it with a message using both `+` and an f-string.
5. Test `bool()` with different values: `0`, `1`, `""`, `"Hello"`, `None`, and `[]`.
6. Write a small program that safely converts user input to an integer using `try-except`.

---

## 9. What You Learned Today

- What type casting (type conversion) is and why it is needed
- How to use `int()`, `float()`, `str()`, and `bool()`
- How to convert between collections (`list`, `tuple`, `set`)
- Why `input()` always returns a string and how to handle it
- Best practices for safe and readable type conversion
- Common beginner mistakes and how to avoid them

Type casting is essential for handling user input, performing calculations, and building real-world Python applications.

Next topic: [Conditional statements (if, else)](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-10/notes.md)
