
print("Day 20: Dictionaries Examples")

# Creating a dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student)

# Dictionary structure
person = {"name": "John", "age": 25, "city": "New York"}
print(person)

# Accessing dictionary values
student = {"name": "Alice", "age": 20}
print(student["name"])
print(student["age"])

# Adding new key-value pairs
car = {"brand": "Toyota", "year": 2022}
car["color"] = "Red"
print(car)

# Updating values
user = {"username": "admin", "status": "active"}
user["status"] = "inactive"
print(user)

# Checking if a key exists
student = {"name": "Alice", "age": 20}
print("name" in student)
print("grade" in student)

# Iterating keys
person = {"name": "Tom", "age": 30, "city": "Paris"}
for key in person:
    print(key)

# Iterating values
person = {"name": "Tom", "age": 30, "city": "Paris"}
for value in person.values():
    print(value)

# Iterating key-value pairs
person = {"name": "Tom", "age": 30, "city": "Paris"}
for key, value in person.items():
    print(key, value)

# Creating a dictionary example
book = {"title": "Python Basics", "pages": 300}
print(book)

# Accessing values example
user = {"name": "Sarah", "age": 28}
print(user["name"])

# Adding data example
product = {"name": "Laptop", "price": 1000}
product["stock"] = 50
print(product)

# Updating data example
settings = {"theme": "light"}
settings["theme"] = "dark"
print(settings)

# Iterating dictionary example
student = {"name": "Anna", "age": 21, "grade": "A"}
for key, value in student.items():
    print(key, value)

# Duplicate keys example
data = {"a": 1, "a": 2}
print(data)

# Dictionary vs list example
my_list = [10,20,30]
print(my_list[0])

my_dict = {"a": 10, "b": 20}
print(my_dict["a"])

print("End of Day 20 examples")
