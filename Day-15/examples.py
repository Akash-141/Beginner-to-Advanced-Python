# Import entire module
import math

print(math.pi)
print(math.sqrt(36))

# Import specific function
from math import pow

print(pow(2, 3))

# Using alias
import math as m

print(m.factorial(5))

# Custom module example (if mymodule.py exists)
# import mymodule
# print(mymodule.greet("John"))
