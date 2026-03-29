
print("Day 24: Function Arguments and Return Values Examples")

def add(a, b):
    return a + b
print(add(2, 3))

def greet(name, age):
    print(name, age)
greet(age=20, name="Alice")

def greet_default(name="Guest"):
    print("Hello", name)
greet_default()
greet_default("Bob")

def total(*numbers):
    return sum(numbers)
print(total(1, 2, 3, 4))

def show_info(**data):
    print(data)
show_info(name="Alice", age=20)

def square(n):
    return n * n
result = square(4)
print(result)

def get_values():
    return 1, 2, 3
a, b, c = get_values()
print(a, b, c)

def multiply(a, b):
    return a * b
print(multiply(3, 4))

def display(name, age):
    print(name, age)
display(age=25, name="John")

def welcome(name="User"):
    print("Welcome", name)
welcome()

def add_all(*nums):
    return sum(nums)
print(add_all(1, 2, 3))

def calc(a, b):
    return a + b, a * b
s, p = calc(2, 3)
print(s, p)

def calculate_total(price, tax=0.1):
    return price + (price * tax)
print(calculate_total(100))

def log_data(*args, **kwargs):
    print(args)
    print(kwargs)
log_data(1, 2, 3, name="Alice", age=25)

def create_user(name, age):
    print(name, age)
create_user(name="Alice", age=25)

print("End of Day 24 examples")
