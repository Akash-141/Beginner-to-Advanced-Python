print("Day 26: Lambda Functions Examples")

add = lambda a, b: a + b
print(add(2, 3))

multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))

def apply(func, value):
    return func(value)
print(apply(lambda x: x * 2, 5))

numbers = [1, 2, 3, 4]
print(list(map(lambda x: x**2, numbers)))

numbers = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, numbers)))

pairs = [(1, 2), (3, 1), (5, 0)]
print(sorted(pairs, key=lambda x: x[1]))

square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(10, 20))

nums = [1, 2, 3]
print(list(map(lambda x: x + 1, nums)))

nums = [1, 2, 3, 4]
print(list(filter(lambda x: x > 2, nums)))

data = [(1, 3), (2, 1), (4, 2)]
print(sorted(data, key=lambda x: x[1]))

numbers = [1, 2, 3]
print(list(map(lambda x: x * 2, numbers)))

print("End of Day 26 examples")
