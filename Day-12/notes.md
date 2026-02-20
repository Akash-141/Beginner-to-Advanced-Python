# Day 12: File Handling in Python

## 1. Why File Handling?

File handling allows your program to read from and write to files.

Official documentation:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

---

## 2. Opening a File

Use the open() function.

```python
file = open("example.txt", "r")
```

Common modes:

- "r"  → Read
- "w"  → Write (overwrites file)
- "a"  → Append
- "x"  → Create new file
- "b"  → Binary mode

---

## 3. Reading a File

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

Better method using with:

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 4. Writing to a File

```python
with open("example.txt", "w") as file:
    file.write("Hello World")
```

---

## 5. Appending to a File

```python
with open("example.txt", "a") as file:
    file.write("\nNew Line")
```

---

## 6. Reading Line by Line

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line)
```

---

## Practice Tasks

1. Create a text file and write a sentence into it.
2. Read and print the content of a file.
3. Append a new line to the file.
4. Read the file line by line.
5. Create a new file using mode "x".

---

## What You Learned Today

- open() function
- File modes (r, w, a, x)
- Reading files
- Writing files
- Using with statement
