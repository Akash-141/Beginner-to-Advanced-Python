# Day 22: Object-Oriented Programming — Inheritance & Polymorphism

## 1. Quick Recap of OOP
Object-Oriented Programming (OOP) helps structure code using:

- Classes
- Objects
- Encapsulation
- Inheritance
- Polymorphism

Today we focus on **Inheritance** and **Polymorphism**.

---

## 2. What is Inheritance?

Inheritance allows a class (child) to reuse properties and methods of another class (parent).

### Why use inheritance?

- Code reuse
- Cleaner structure
- Easier maintenance
- Real-world modeling

---

## 3. Basic Inheritance Example

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()
```

The `Dog` class inherits the `speak()` method from `Animal`.

---

## 4. Overriding Methods

A child class can modify parent behavior.

```python
class Dog(Animal):
    def speak(self):
        print("Dog barks")
```

This is called **method overriding**.

---

## 5. Using super()

`super()` lets you call the parent class methods.

```python
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks loudly")
```

---

## 6. What is Polymorphism?

Polymorphism means **same method name, different behavior**.

Example: different animals speaking differently.

---

## 7. Polymorphism Example

```python
class Cat:
    def speak(self):
        print("Cat meows")

class Dog:
    def speak(self):
        print("Dog barks")

animals = [Cat(), Dog()]

for animal in animals:
    animal.speak()
```

Same method name → different outputs.

---

## 8. Types of Polymorphism

- Method overriding
- Operator overloading
- Duck typing

---

## 9. Best Practices

- Use inheritance only when there is a real “is-a” relationship
- Avoid deep inheritance chains
- Prefer composition when appropriate
- Keep classes focused

---

## 🎯 Summary

Today you learned:

- What inheritance is
- How child classes reuse parent code
- Method overriding
- Using super()
- What polymorphism is

You are now thinking in true OOP style. 🚀
