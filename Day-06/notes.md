# Day 6: Strings and String Operations

## 1. Definition of Strings

A **string** in Python is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

Strings are used to store textual data such as names, messages, sentences, and symbols.

In Python, strings are:
- Ordered
- Immutable (cannot be changed after creation)
- Indexed
- Iterable

Official reference:
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

---

## 2. Detailed Explanation of the Topic

Strings are one of the most commonly used data types in Python. Since text processing is essential in real-world applications (web development, automation, data science, APIs, etc.), mastering string operations is critical.

Because strings are immutable:
- You cannot modify individual characters directly
- Any modification creates a new string

Python provides:
- Indexing
- Slicing
- Concatenation
- Repetition
- Built-in string methods
- String formatting techniques

---

## 3. Creating Strings

```python
name = "Akash"
city = 'Dhaka'
paragraph = """This is a
multi-line string"""

print(name)
print(city)
print(paragraph)
```

---

## 4. String Indexing

Each character has a position (index).

```python
text = "Python"
print(text[0])
print(text[3])
print(text[-1])
```

---

## 5. String Slicing

```python
text = "Programming"
print(text[0:6])
print(text[3:])
print(text[:5])
```

---

## 6. String Concatenation

```python
first = "Hello"
second = "World"
result = first + " " + second
print(result)
```

---

## 7. String Repetition

```python
print("Ha" * 3)
```

---

## 8. Useful String Methods

```python
text = "Python"
print(text.upper())
print(text.lower())

text = "   hello   "
print(text.strip())

text = "I like Java"
print(text.replace("Java", "Python"))

sentence = "Python is powerful"
words = sentence.split()
print(words)

text = "Hello World"
print(text.find("World"))
```

---

## 9. String Formatting

```python
name = "Akash"
age = 21
print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))
```

---

## 10. Do's and Don'ts

### Do's
- Use f-strings for formatting
- Use meaningful variable names
- Use built-in methods
- Handle whitespace properly
- Remember immutability

### Don'ts
- Do NOT modify characters directly
- Do NOT overuse + for large strings
- Do NOT ignore case sensitivity
- Do NOT assume user input is clean

---

## 11. Industry Standards

According to PEP 8:
- Prefer f-strings (Python 3.6+)
- Keep formatting readable
- Use descriptive names
- Avoid complex inline expressions

PEP 8 reference:
https://peps.python.org/pep-0008/

---

## 12. Mistakes to Avoid

```python
text = "Python"
# text[0] = "J"

print("python" == "Python")

age = "21"
# print("Age: " + age + 5)
```

---

## Summary

Today you learned:
- String creation
- Indexing and slicing
- Concatenation and repetition
- Important string methods
- Formatting techniques
- Best practices and common mistakes

Next topic: [Input and output](https://github.com/Akash-141/Beginner-to-Advanced-Python/blob/main/Day-07/notes.md)
