# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

# Accessing values
print(student["name"])
print(student["grade"])

# Adding a new key-value pair
student["email"] = "john@example.com"

# Updating a value
student["age"] = 21

print(student)

# Removing a key
student.pop("grade")

print(student)

# Looping through dictionary
for key, value in student.items():
    print(key, value)

# Length of dictionary
print(len(student))
