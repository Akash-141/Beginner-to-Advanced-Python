# Day 1: Introduction to Python and Programming

## 1. What is Programming?

Programming is the process of giving a computer a set of precise instructions so it can perform specific tasks.

A computer does not understand natural human language. It only follows clear, exact, and unambiguous instructions written in a programming language.

A **program** is simply a collection of these instructions that work together to achieve a goal — whether it’s calculating numbers, displaying text, processing data, or controlling other systems.

In short:
- You write instructions in a programming language.
- The computer executes those instructions.
- The result is the output you see or the action the computer performs.

---

## 2. What is Python?

Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility.

It was created by **Guido van Rossum** and first released in **1991**. Python emphasizes code readability and allows developers to express concepts in fewer lines of code compared to many other languages.

Official description from the Python Software Foundation:

> Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

Source:  
https://www.python.org/doc/essays/blurb/

**Key characteristics of Python:**
- **Interpreted** — Code is executed line by line (no separate compilation step needed for basic use).
- **High-level** — You focus on solving problems rather than managing low-level computer details.
- **Dynamically typed** — You don’t need to declare variable types explicitly.
- **Object-oriented** — Supports classes and objects, while still allowing simpler procedural styles.
- **Cross-platform** — Runs on Windows, macOS, Linux, and many other systems.
- **Extensive standard library** — Comes with many built-in modules for common tasks.

---

## 3. Why Learn Python?

Python is one of the most popular programming languages in the world for several strong reasons:

1. **Beginner-friendly** — The syntax is clean and close to natural English, making it easier to learn as a first language.
2. **Simple and readable** — Code is easier to write, read, and maintain compared to many other languages.
3. **Powerful and versatile** — Suitable for both small scripts and large-scale applications.
4. **Large global community** — Extensive libraries, frameworks, tutorials, documentation, and active support available worldwide.
5. **High industry demand** — Widely used in tech companies, research, startups, and freelancing opportunities.
6. **Rich ecosystem** — Thousands of third-party packages available through PyPI for almost any task.

**Common areas where Python is used:**
- Web development (Django, Flask, FastAPI)
- Data science and data analysis (Pandas, NumPy, Matplotlib)
- Machine learning and artificial intelligence (TensorFlow, PyTorch, scikit-learn)
- Automation and scripting
- Scientific computing
- Backend services and APIs

Because of its balance of simplicity and power, Python is an excellent first language for beginners and remains highly relevant for professionals.

---

## 4. How Python Code Looks

Here’s a classic first example:

```python
print("Hello, World")
```

**Explanation:**
- `print()` is a built-in Python function used to display output.
- Anything inside quotation marks (`"..."`) is treated as a **string** (text).
- Python executes the instruction and shows whatever is inside the parentheses on the screen.

This single line already demonstrates how readable Python is compared to many other languages.

---

## 5. Python is Case-Sensitive

Python treats uppercase and lowercase letters as completely different.

**Correct:**
```python
print("Correct")
```

**Incorrect:**
```python
Print("Wrong")
```

In the second example, Python looks for a function named `Print` (with a capital P). Since the built-in function is called `print` (all lowercase), it will raise a `NameError`.

Remember:  
`print`, `Print`, and `PRINT` are three different names in Python.

---

## 6. Your First Small Program

Create a file named `hello.py` and write the following code:

```python
print("My name is Akash")
print("I am starting my Python journey")
```

**How to run it:**
1. Save the file as `hello.py`.
2. Open a terminal (or command prompt).
3. Navigate to the folder containing the file.
4. Run the command:

```bash
python hello.py
```

You should see both lines printed in the terminal.

This simple exercise helps you practice creating a file, writing code, and running a Python program.

---

## 7. Practice Tasks

Try these small exercises on your own:

1. Print your full name.
2. Print the name of your university or school.
3. Print three separate sentences (each on a new line).

**Tip:** Use the `print()` function for each task. Experiment with different text and notice how the output appears.

---

## What You Learned Today

- What programming is and how computers follow instructions
- What Python is, who created it, and its main characteristics
- Why Python is a popular and practical language to learn
- How to write and run a basic Python program
- That Python is case-sensitive

**Next topic:** [Installing Python and Setting Up Your Environment](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-02/notes.md)
