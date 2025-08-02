"""
#CLASSES 

class name_of_class:
    def __init__(self,name,age):
        self.name =  name
        self.age = age
y = name_of_class("RNS",25)
print(y.name)
print(y)
"""
"""
class hmt:
    def __init__(self,year,age):
        self.year = year
        self.age = age
p1 = hmt(2025,90)
"""
"""
class state:
    def __init__(pranathi, city,population):
        pranathi.c1 =city
        pranathi.p1 =population
x= state("BLR",25000000)
y= state("DXB",1000000)
print(x.c1)
print(y.p1)
"""

#inhetrance

"""
# polymorphism

class Animal:
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    def speak(self):  # Same method name, different implementation
        print("Dog barks")
class Cat(Animal):
    def speak(self):  # Same method name, different implementation
        print("Cat meows")
# a = Animal()
# print(a.speak())
# b = Dog()
# print(b.speak())
c = Cat()
print(c.speak())
# Using polymorphism
for i in [Animal(), Dog(), Cat()]:
    i.speak()
"""

"""
#Encapsulation
class BankAccount:
    def __init__(self):
        self.__balance = 0 #change from zero balance account to minimum
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
    def get_balance(self):
        return self.__balance
account = BankAccount()
account.deposit(100)    #passing values
account.deposit(500000)
print("Balance:",account.get_balance())
"""

#abstraction
from abc import ABC, abstractmethod
# 1. Define an Abstract Base Class (ABC)
class Shape(ABC): # Inherit from ABC to make it abstract
    @abstractmethod # Decorator to mark methods as abstract
    def area(self):
        """Abstract method to calculate the area of the shape."""
        pass
    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape."""
        pass
# 2. Create Concrete Subclasses
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14159 * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
# 3. Use the abstraction
def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
circle = Circle(5)
rectangle = Rectangle(10, 5)
print("Circle:")
print_shape_info(circle)
print("\nRectangle:")
print_shape_info(rectangle)