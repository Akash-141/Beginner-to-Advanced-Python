
print("Day 13: Logical Operators Examples")

# Example 1
count = 1
while count <= 5:
    print("Count:", count)
    count += 1


# Example 2
password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access granted")


# Example 3
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == "exit":
        break
print("Loop stopped")


# Example 4
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)


# Example 5
balance = 100
while balance > 0:
    print("Balance:", balance)
    balance -= 20


# Good practice
i = 0
while i < 5:
    print(i)
    i += 1


# Infinite loop mistake (commented)
# i = 0
# while i < 5:
#     print(i)


# Corrected version
x = 1
while x < 10:
    print(x)
    x += 1


# Better alternative
for i in range(5):
    print(i)
    
print("End of Day 13 examples")
