# Day 14: Introduction to Object-Oriented Programming (OOP)

## 1. What is OOP?

Object-Oriented Programming (OOP) is a programming style based on objects.

Objects combine data (attributes) and behavior (methods).

Official documentation:
https://docs.python.org/3/tutorial/classes.html

---

## 2. Creating a Class

A class is a blueprint for creating objects.

```python
class Person:
    pass
```

---

## 3. The __init__ Method

The __init__ method runs when an object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## 4. Creating an Object

```python
person1 = Person("Alice", 25)

print(person1.name)
print(person1.age)
```

---

## 5. Adding Methods

Methods are functions inside a class.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)
```

---

## 6. The self Keyword

self refers to the current object.

It allows access to attributes and methods inside the class.

---

## 7. Why Use OOP?

- Organize code better
- Reuse code
- Model real-world concepts
- Improve readability

---

## Practice Tasks

1. Create a class called Car with attributes brand and year.
2. Create an object of Car.
3. Add a method that prints car details.
4. Create multiple objects from the same class.
5. Add a new attribute to your class.

---

## What You Learned Today

- What OOP is
- Creating classes
- __init__ method
- Creating objects
- Methods in classes
- self keyword
