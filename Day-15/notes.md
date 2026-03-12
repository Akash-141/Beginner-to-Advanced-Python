
# Day 15: Loop Control Statements

## 1. Definition of the Topic

Loop control statements are statements that alter the normal execution flow of loops in Python. They allow programmers to stop a loop early, skip specific iterations, or leave placeholders for future logic. Python provides three primary loop control statements:

- break
- continue
- pass

These statements are commonly used inside `for` loops and `while` loops to create more efficient and controlled iterations.

Official documentation:
https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements

---

## 2. Detailed Explanation of the Topic

In many real programs, loops should not always run until their natural end. Sometimes a loop should:

- stop immediately when a condition is met
- skip certain values
- leave an empty block temporarily during development

Loop control statements solve these problems.

Python includes three main loop control statements:

1. break
2. continue
3. pass

Each one changes how a loop behaves.

---

### 2.1 The break Statement

The `break` statement immediately terminates the loop in which it appears. When Python encounters `break`, it exits the loop and continues executing the program from the next statement after the loop.

Example:

```python
for number in range(1, 10):
    if number == 5:
        break
    print(number)
```

Output:

1
2
3
4

Explanation:

The loop stops completely when `number` becomes 5.

---

### 2.2 The continue Statement

The `continue` statement skips the current iteration and moves to the next cycle of the loop.

Example:

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:

1
2
4
5

Explanation:

When the number becomes 3, the loop skips the print statement and continues with the next iteration.

---

### 2.3 The pass Statement

The `pass` statement does nothing. It is used as a placeholder when a statement is syntactically required but no action is needed yet.

Example:

```python
for number in range(5):
    if number == 2:
        pass
    print(number)
```

Output:

0
1
2
3
4

Explanation:

The `pass` statement allows the code to run without producing any effect.

---

### 2.4 Using break in a While Loop

```python
count = 1

while True:
    print(count)
    if count == 5:
        break
    count += 1
```

Explanation:

The loop runs indefinitely until the `break` statement stops it when the value becomes 5.

---

### 2.5 Practical Example: Searching for a Value

```python
numbers = [10, 25, 30, 45, 50]

for num in numbers:
    if num == 30:
        print("Number found")
        break
```

Explanation:

The loop stops as soon as the number is found, which improves efficiency.

---

### 2.6 Skipping Invalid Data

```python
numbers = [5, -2, 8, -1, 10]

for num in numbers:
    if num < 0:
        continue
    print(num)
```

Explanation:

Negative numbers are skipped and only positive numbers are printed.

---

## 3. Do's and Don'ts

### Do's

- Use `break` when a loop should stop immediately.
- Use `continue` when certain values should be skipped.
- Use `pass` as a temporary placeholder during development.
- Keep loop logic clear and easy to read.

### Don'ts

- Do not overuse break in complicated loops.
- Do not write loops that are difficult to understand.
- Do not leave unnecessary pass statements in finished code.

---

## 4. Industry Standards

Professional Python developers follow the PEP 8 style guide.

PEP 8:
https://peps.python.org/pep-0008/

Recommended practices:

### Keep loop logic simple

Bad:

```python
for i in range(10):
    if i == 3:
        continue
    elif i == 7:
        break
    else:
        print(i)
```

Better:

```python
for i in range(10):
    if i == 7:
        break
    if i == 3:
        continue
    print(i)
```

---

### Use break for efficient searching

```python
items = ["apple", "banana", "mango"]

for item in items:
    if item == "banana":
        print("Item found")
        break
```

This avoids unnecessary iterations.

---

### Use continue for filtering data

```python
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```

This prints only odd numbers.

---

## 5. Mistakes to Avoid

### Infinite Loops

Bad:

```python
while True:
    print("Running forever")
```

Better:

```python
while True:
    user_input = input("Type quit to stop: ")
    if user_input == "quit":
        break
```

---

### Misusing continue

Bad:

```python
for i in range(5):
    if i == 2:
        continue
    else:
        continue
```

Correct:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

### Using pass unnecessarily

Bad:

```python
if True:
    pass
```

Instead, implement the logic when ready.

---

## 6. Summary

In this lesson you learned:

- What loop control statements are
- How break, continue, and pass work
- How to stop loops early
- How to skip unwanted iterations
- Best practices used in professional Python development

Loop control statements are important for writing efficient and readable loops.

Next topic: [Lists]()
