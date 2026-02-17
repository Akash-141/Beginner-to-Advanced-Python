# Day 7: Loops in Python (for and while)

## 1. Why Loops?

Loops allow you to run code multiple times without repeating it manually.

Official documentation:
https://docs.python.org/3/tutorial/controlflow.html#for-statements

---

## 2. The for Loop

A for loop is used to iterate over a sequence like a string, list, or range.

Example with range():

```python
for i in range(5):
    print(i)
```

range(5) generates numbers from 0 to 4.

---

## 3. Looping Through a String

```python
text = "Python"

for letter in text:
    print(letter)
```

---

## 4. The while Loop

A while loop runs as long as a condition is True.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Be careful: If the condition never becomes False, the loop will run forever.

---

## 5. break Statement

break stops the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## 6. continue Statement

continue skips the current iteration and moves to the next one.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 7. Nested Loops

You can put a loop inside another loop.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

## Practice Tasks

1. Print numbers from 1 to 10 using a loop.
2. Print all characters in a word.
3. Use a while loop to count down from 5 to 1.
4. Stop a loop when a number equals 7.
5. Skip even numbers in a loop.

---

## What You Learned Today

- for loops
- while loops
- range()
- break
- continue
- Nested loops
