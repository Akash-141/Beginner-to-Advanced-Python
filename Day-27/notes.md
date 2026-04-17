# Day 27: Basic Error Handling

## 1. Definition of the Topic

Error handling in Python is the process of responding to and managing errors (exceptions) that occur during program execution.

It prevents programs from crashing and allows graceful handling of unexpected situations.

Official documentation:
https://docs.python.org/3/tutorial/errors.html

---

## 2. Detailed Explanation of the Topic

### What is an Exception?

An exception is an error that occurs during runtime.

```python
print(10 / 0)  # ZeroDivisionError
```

---

### try and except

Used to catch and handle exceptions.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

### Handling Multiple Exceptions

```python
try:
    num = int("abc")
except ValueError:
    print("Invalid conversion")
```

---

### Using Multiple except Blocks

```python
try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("Division by zero")
```

---

### Using else Block

Executes if no exception occurs.

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", x)
```

---

### Using finally Block

Always executes whether an exception occurs or not.

```python
try:
    x = 10 / 2
finally:
    print("Execution completed")
```

---

### Generic Exception Handling

```python
try:
    x = int("abc")
except Exception as e:
    print("Error:", e)
```

---

## 3. Easy Short Code Examples

### Example 1: Basic try-except

```python
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Error occurred")
```

---

### Example 2: ValueError Handling

```python
try:
    num = int("hello")
except ValueError:
    print("Conversion failed")
```

---

### Example 3: else Block

```python
try:
    result = 10 / 2
except:
    print("Error")
else:
    print(result)
```

---

### Example 4: finally Block

```python
try:
    x = 5
finally:
    print("Done")
```

---

### Example 5: Exception Object

```python
try:
    x = int("xyz")
except Exception as e:
    print(e)
```

---

## 4. Do's and Don'ts

### Do's

- Use try-except to handle expected errors
- Catch specific exceptions when possible
- Use finally for cleanup operations
- Use meaningful error messages

### Don'ts

- Do not use bare except unnecessarily
- Do not ignore exceptions silently
- Do not overuse exception handling
- Do not catch all exceptions blindly

---

## 5. Industry Standards

### Specific Exception Handling

```python
try:
    x = int("10")
except ValueError:
    print("Invalid number")
```

---

### Logging Errors (Basic)

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Logged error:", e)
```

---

### Clean Code Practice

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

---

## 6. Mistakes to Avoid

### Using Bare except

```python
try:
    x = 10 / 0
except:
    print("Error")
```

---

### Ignoring Exceptions

```python
try:
    x = int("abc")
except ValueError:
    pass
```

---

### Wrong Exception Type

```python
try:
    x = int("abc")
except ZeroDivisionError:
    print("Wrong handler")
```

---

## Summary

- Exceptions handle runtime errors
- Use try, except, else, and finally effectively
- Always handle specific exceptions when possible
- Avoid suppressing important errors
