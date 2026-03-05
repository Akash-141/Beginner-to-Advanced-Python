print("Day 11: elif and Nested Conditions Examples")

# Basic elif example
score = 82

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")

# Example showing problem with multiple if statements
score = 85

if score >= 90:
    print("Grade A")

if score >= 80:
    print("Grade B")

# Correct elif usage
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")

# Nested condition example
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")

# Nested even/odd check
number = 10

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is negative")

# Combining elif and nested conditions
temperature = 30
raining = False

if temperature > 35:
    print("Too hot outside")
elif temperature > 25:
    if raining:
        print("Warm but rainy")
    else:
        print("Perfect weather")
else:
    print("Cool weather")

# Login verification example
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")

# Early return function example
def check_login(user, password):
    if user != "admin":
        return "User not found"
    if password != "1234":
        return "Wrong password"
    return "Login successful"

print(check_login("admin", "1234"))

# Simplifying nested conditions
a = 5
b = 3
c = 2

if a > 0 and b > 0 and c > 0:
    print("All numbers are positive")

print("End of Day 11 examples")
