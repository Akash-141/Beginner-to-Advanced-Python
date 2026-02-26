# Day 22 Examples: Inheritance & Polymorphism

# ---------- Basic Inheritance ----------
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()


# ---------- Method Overriding ----------
class Cat(Animal):
    def speak(self):
        print("Cat meows")

cat = Cat()
cat.speak()


# ---------- Using super() ----------
class Bird(Animal):
    def speak(self):
        super().speak()
        print("Bird chirps")

bird = Bird()
bird.speak()


# ---------- Polymorphism Example ----------
class Cow:
    def speak(self):
        print("Cow moos")

animals = [Dog(), Cat(), Bird(), Cow()]

print("\nPolymorphism demo:")
for a in animals:
    a.speak()
