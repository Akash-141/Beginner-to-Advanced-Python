
print("Day 21: Dictionary Methods Examples")

student = {"name": "Alice", "age": 20}
print(student.get("name"))
print(student.get("grade"))

print(student.keys())
print(student.values())
print(student.items())

student = {"name": "Alice"}
student.update({"age": 20})
print(student)

student = {"name": "Alice", "age": 20}
removed = student.pop("age")
print(removed)
print(student)

student = {"name": "Alice", "age": 20}
print(student.popitem())

student = {"name": "Alice", "age": 20}
student.clear()
print(student)

original = {"a": 1, "b": 2}
copy_dict = original.copy()
print(copy_dict)

user = {"username": "admin"}
print(user.get("username"))

data = {"a": 1, "b": 2}
print(data.keys())
print(data.values())

for key, value in data.items():
    print(key, value)

config = {"theme": "light"}
config.update({"theme": "dark"})
print(config)

numbers = {"one": 1, "two": 2}
numbers.pop("one")
print(numbers)

user = {"name": "Alice"}
age = user.get("age", 0)
print(age)

data = {"a": 1, "b": 2}
for key, value in data.items():
    print(f"{key}: {value}")

print("End of Day 21 examples")
