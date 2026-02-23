# Day 18 Examples: Decorators and Generators

# ---------- Decorator Example ----------
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function.")
        result = func(*args, **kwargs)
        print("Something is happening after the function.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Akash")


# ---------- Generator Example ----------
def even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2

print("\nEven numbers up to 10:")
for n in even_numbers(10):
    print(n)


# ---------- Generator Expression ----------
squares = (x*x for x in range(6))

print("\nSquares using generator expression:")
for s in squares:
    print(s)
