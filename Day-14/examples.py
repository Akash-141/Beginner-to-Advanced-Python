# Creating a class
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print("Car:", self.brand, "-", self.year)

# Creating objects
car1 = Car("Toyota", 2020)
car2 = Car("Honda", 2022)

# Accessing attributes
print(car1.brand)
print(car2.year)

# Calling method
car1.display_info()
car2.display_info()
