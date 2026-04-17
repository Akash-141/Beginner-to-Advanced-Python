print("Day 27: Basic Error Handling Examples")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    num = int("abc")
except ValueError:
    print("Invalid conversion")

try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("Division by zero")

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", x)

try:
    x = 10 / 2
finally:
    print("Execution completed")

try:
    x = int("abc")
except Exception as e:
    print("Error:", e)

try:
    print(5 / 0)
except ZeroDivisionError:
    print("Error occurred")

try:
    num = int("hello")
except ValueError:
    print("Conversion failed")

try:
    result = 10 / 2
except:
    print("Error")
else:
    print(result)

try:
    x = 5
finally:
    print("Done")

try:
    x = int("xyz")
except Exception as e:
    print(e)

try:
    x = int("10")
except ValueError:
    print("Invalid number")

try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Logged error:", e)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(divide(10, 2))
print(divide(10, 0))

print("End of Day 27 examples")
