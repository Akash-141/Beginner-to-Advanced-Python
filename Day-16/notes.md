# Day 16: Working with Files in Python

## 1. What is File Handling?

File handling allows you to create, read, update, and delete files using Python.

Official documentation:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

---

## 2. Opening a File

Use the open() function.

```python
file = open("example.txt", "r")
```

Modes:
- "r"  -> Read
- "w"  -> Write (overwrites file)
- "a"  -> Append
- "x"  -> Create (fails if file exists)
- "b"  -> Binary mode

---

## 3. Reading a File

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

Better way (recommended):

```python
with open("example.txt", "r") as file:
    print(file.read())
```

---

## 4. Writing to a File

```python
with open("example.txt", "w") as file:
    file.write("Hello, world!")
```

---

## 5. Appending to a File

```python
with open("example.txt", "a") as file:
    file.write("\nNew line added.")
```

---

## 6. Why Use 'with'?

The with statement automatically closes the file after use.
It is safer and cleaner.

---

## Practice Tasks

1. Create a file and write your name into it.
2. Read the file and print its content.
3. Append a new line to the file.
4. Try opening a file in different modes.
5. Experiment with reading line by line using readlines().

---

## What You Learned Today

- open() function
- File modes (r, w, a, x)
- Reading files
- Writing files
- Using with statement
