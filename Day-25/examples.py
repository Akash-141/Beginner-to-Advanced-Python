print("Day 25: Scope and Lifetime of Variables Examples")

def my_function():
    x = 10
    print(x)
my_function()

x = 20
def show():
    print(x)
show()
print(x)

def outer():
    x = "outer"
    def inner():
        print(x)
    inner()
outer()

x = 5
def change():
    global x
    x = 10
change()
print(x)

def outer_nonlocal():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    print(x)
outer_nonlocal()

def test():
    x = 100
    print(x)
test()

def func_local():
    a = 1
    print(a)
func_local()

b = 2
def func_global():
    print(b)
func_global()

c = 3
def update():
    global c
    c = 4
update()
print(c)

def outer_example():
    d = 5
    def inner():
        nonlocal d
        d = 6
    inner()
    print(d)
outer_example()

def temp():
    x = 50
    print(x)
temp()

def calculate():
    result = 10 + 20
    return result
print(calculate())

count = 0
def increment():
    global count
    count += 1
increment()
print(count)

def controlled():
    value = 10
    def inner():
        return value + 5
    return inner()
print(controlled())

print("End of Day 25 examples")
