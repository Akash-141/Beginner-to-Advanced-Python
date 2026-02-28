print("Day 6: Strings and String Operations Examples")

name = "Akash"
city = 'Dhaka'
paragraph = """This is a
multi-line string"""

print(name)
print(city)
print(paragraph)

text = "Python"
print(text[0])
print(text[3])
print(text[-1])

text = "Programming"
print(text[0:6])
print(text[3:])
print(text[:5])

first = "Hello"
second = "World"
result = first + " " + second
print(result)

print("Ha" * 3)

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

name = "Akash"
age = 21
print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))

print("python" == "Python")

print("End of Day 6 examples")
