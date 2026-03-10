# Day 13: While Loops

## 1. Definition

A **while loop** in Python is a control flow statement that repeatedly
executes a block of code **as long as a specified condition evaluates to
True**.

Unlike a `for` loop, which usually iterates over a sequence, a `while`
loop continues running **until the condition becomes False**.

Official Python documentation:
https://docs.python.org/3/tutorial/controlflow.html#while-statements

------------------------------------------------------------------------

## 2. Detailed Explanation

A `while` loop checks a condition before each iteration.

**Syntax:**

``` python
while condition:
    # code block
```

How it works:

1.  Python evaluates the condition.
2.  If the condition is **True**, the code block runs.
3.  After execution, Python checks the condition again.
4.  The loop continues until the condition becomes **False**.

If the condition never becomes False, the loop becomes an **infinite
loop**.

While loops are commonly used when: - The number of iterations is
unknown beforehand. - The loop should run until a condition changes. -
You are waiting for user input or system events.

Reference: https://realpython.com/python-while-loop/

------------------------------------------------------------------------

## 3. Easy Code Examples

### Example 1: Basic while loop

``` python
count = 1

while count <= 5:
    print("Count:", count)
    count += 1
```

### Example 2: Using while with user input

``` python
password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted")
```

### Example 3: Infinite loop with break

``` python
while True:
    user_input = input("Type 'exit' to stop: ")
    
    if user_input == "exit":
        break

print("Loop stopped")
```

### Example 4: Using continue in a while loop

``` python
number = 0

while number < 10:
    number += 1
    
    if number % 2 == 0:
        continue
    
    print(number)
```

### Example 5: While loop with condition checking

``` python
balance = 100

while balance > 0:
    print("Balance:", balance)
    balance -= 20
```

------------------------------------------------------------------------

## 4. Do's and Don'ts

### Do's

✔ Ensure the loop condition eventually becomes False.\
✔ Use `break` when you want to stop a loop early.\
✔ Use `continue` to skip unwanted iterations.\
✔ Keep loop logic simple and readable.\
✔ Update loop variables inside the loop.

Good example:

``` python
i = 0

while i < 5:
    print(i)
    i += 1
```

### Don'ts

✘ Don't create infinite loops accidentally.\
✘ Don't write complex conditions that are hard to understand.\
✘ Don't forget to update the loop variable.

Bad example:

``` python
i = 0

while i < 5:
    print(i)
```

------------------------------------------------------------------------

## 5. Industry Standards

Professional Python developers follow these practices:

### Prefer `for` loops when iteration count is known

``` python
for i in range(5):
    print(i)
```

### Use `while` loops for condition-based iteration

Example use cases: - Input validation - Retry logic - Waiting for
external events

### Use meaningful variable names

``` python
attempts = 0

while attempts < 3:
    print("Trying again")
    attempts += 1
```

Reference: https://pep8.org/

------------------------------------------------------------------------

## 6. Common Mistakes to Avoid

### Forgetting to update the condition variable

``` python
x = 1

while x < 10:
    print(x)
```

Correct:

``` python
x = 1

while x < 10:
    print(x)
    x += 1
```

### Using while instead of for unnecessarily

``` python
i = 0

while i < 5:
    print(i)
    i += 1
```

Better:

``` python
for i in range(5):
    print(i)
```

### Writing overly complex conditions

``` python
while a < 10 and b > 5 and c != 3:
    pass
```

Better:

``` python
while is_valid:
    process_data()
```

------------------------------------------------------------------------

## Summary

A **while loop** allows repeated execution of code **while a condition
remains True**.

Key ideas:

-   Condition checked before each iteration
-   Must eventually become False
-   `break` stops a loop
-   `continue` skips to next iteration

Further reading:

Python documentation:
https://docs.python.org/3/tutorial/controlflow.html#while-statements

Real Python guide: https://realpython.com/python-while-loop/

Next topic: [For loops]()
