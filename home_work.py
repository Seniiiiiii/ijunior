import math

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return math.pi * self.radius **2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.widht = width
        self.height = height


    def area(self):
        return self.widht * self.height

сircle = Circle(4)
print(сircle.area())

rectangle = Rectangle()
print(rectangle.area())