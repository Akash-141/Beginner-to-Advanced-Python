
print("Day 12: Logical Operators Examples")

# Example of AND operator
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")

# Example of OR operator
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")

# Example of NOT operator
logged_in = False

if not logged_in:
    print("Please log in")

# Combining logical operators
age = 25
country = "BD"

if age >= 18 and country == "BD":
    print("Eligible to vote")

# Logical operator with numbers
value = 0

if not value:
    print("Value is zero or empty")

# Login system example
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# Using parentheses with logical operators
age = 20
student = True

if (age >= 18 and student) or age >= 65:
    print("Discount eligible")

# Self explanatory condition example
is_adult = age >= 18
has_permission = True

if is_adult and has_permission:
    print("Access granted")

# Logical precedence example
a = True
b = False
c = True

print(a or b and c)
print((a or b) and c)

print("End of Day 12 examples")
