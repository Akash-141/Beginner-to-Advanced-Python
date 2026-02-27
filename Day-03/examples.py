print("Day 3: Python Syntax and Indentation Examples")

# Example 1: Basic Python statement
print("Hello, Python")

# Example 2: Case sensitivity
name = "Akash"
Name = "Paul"

print(name)
print(Name)

# Example 3: Statements on new lines
print("Line 1")
print("Line 2")

# Allowed but not recommended
print("Line 1"); print("Line 2")

# Example 4: Single-line comment
# This is a comment
print("Hello")

# Example 5: Multi-line comment
"""
This is a multi-line comment
used for longer explanations
"""

# Example 6: Correct indentation
age = 18

if age >= 18:
    print("You are an adult")

# Example 7: Loop indentation
for i in range(3):
    print("Number:", i)

# Example 8: Nested indentation
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")

print("End of Day 3 examples")
