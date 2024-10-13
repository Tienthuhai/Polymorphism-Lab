from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius  # Private field

    def calculate_area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def calculate_perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height  # Private field
        self.__width = width    # Private field

    def calculate_area(self):
        """Calculate the area of the rectangle."""
        return self.__height * self.__width

    def calculate_perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.__height + self.__width)


# Example usage:
circle = Circle(5)
print("Circle Area:", circle.calculate_area())           # Output: Circle Area: 78.53981633974483
print("Circle Perimeter:", circle.calculate_perimeter()) # Output: Circle Perimeter: 31.41592653589793

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.calculate_area())      # Output: Rectangle Area: 24
print("Rectangle Perimeter:", rectangle.calculate_perimeter())  # Output: Rectangle Perimeter: 20
