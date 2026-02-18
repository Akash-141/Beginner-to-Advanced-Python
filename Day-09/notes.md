# Day 9: Functions in Python

## 1. What is a Function?

A function is a reusable block of code that performs a specific task.

Functions help organize code and avoid repetition.

Official documentation:
https://docs.python.org/3/tutorial/controlflow.html#defining-functions

---

## 2. Defining a Function

You define a function using the def keyword.

```python
def greet():
    print("Hello!")
```

To run the function:

```python
greet()
```

---

## 3. Functions with Parameters

Parameters allow you to pass information into a function.

```python
def greet(name):
    print("Hello", name)

greet("Alice")
```

---

## 4. Returning Values

Functions can return a value using return.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

---

## 5. Multiple Parameters

```python
def multiply(x, y):
    return x * y

print(multiply(4, 6))
```

---

## 6. Default Parameters

You can give parameters default values.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Bob")
```

---

## 7. Why Use Functions?

- Code reusability
- Better organization
- Easier debugging
- Cleaner programs

---

## Practice Tasks

1. Write a function that prints your name.
2. Create a function that adds two numbers.
3. Create a function that multiplies three numbers.
4. Write a function that checks if a number is even.
5. Use a function to calculate the square of a number.

---

## What You Learned Today

- How to define functions
- Calling functions
- Parameters
- return statement
- Default parameters
