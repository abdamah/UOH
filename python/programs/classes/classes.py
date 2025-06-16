# What is a class?
# A class is a blueprint for creating objects (instances). It defines a set of attributes (variables) and methods (functions)
# that the objects created from the class will have.

# What is an instance or object?
# An instance (or object) is an individual object created from a class. It has the attributes and methods defined in the class.

# OOPs Features:
# 1. Encapsulation:
#    Encapsulation refers to bundling the data (attributes) and the methods (functions) that operate on the data into a single unit (class).
#    It also refers to restricting direct access to some of an object's attributes, which is typically done by making them private.

# 2. Inheritance:
#    Inheritance allows a new class (child class) to inherit attributes and methods from an existing class (parent class),
#    which allows code reuse and hierarchical classification.

# 3. Polymorphism:
#    Polymorphism allows methods to be used in different ways depending on the context. It is often seen as method overriding
#    (in child classes) or method overloading (same method name with different arguments).

# 4. Abstraction:
#    Abstraction involves hiding the complex implementation details of an object and only exposing the necessary functionality to the user.

# Now, let's start with a simple class without a constructor:
# Importing ABC and abstractmethod for abstraction
from abc import ABC, abstractmethod


class Shape:
    """
    A simple class to represent a shape (without constructor).
    """

    def area(self):
        pass  # Placeholder method

    def perimeter(self):
        pass  # Placeholder method

    @classmethod
    def shape_type(cls):
        """
        Class method: This is used to get the type of the shape class.
        """
        return cls.__name__

    @staticmethod
    def info():
        """
        Static method: This is used to display general information about shapes.
        """
        print("Shapes are geometric figures that have area and perimeter.")

# Example 1: Creating subclasses for specific shapes (Circle, Rectangle, Square)
# Encapsulation: The details of how the area and perimeter are calculated are hidden inside the respective classes.
# Inheritance: Circle, Rectangle, and Square inherit from the Shape class.

# Circle class (inherits from Shape)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Encapsulation of radius attribute

    def area(self):
        return 3.14 * (self.radius ** 2)  # Area = πr²

    def perimeter(self):
        return 2 * 3.14 * self.radius  # Perimeter = 2πr

# Rectangle class (inherits from Shape)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  # Encapsulation of length attribute
        self.width = width    # Encapsulation of width attribute

    def area(self):
        return self.length * self.width  # Area = length * width

    def perimeter(self):
        return 2 * (self.length + self.width)  # Perimeter = 2(length + width)

# Square class (inherits from Rectangle, demonstrating polymorphism)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Inherits from Rectangle, but with equal sides

    def area(self):
        return self.length * self.width  # Inherited from Rectangle, but now a square

    def perimeter(self):
        return 4 * self.length  # Perimeter of square = 4 * side

# Now, let's test the functionality by creating objects of the classes:


print("Circle Example:")
circle = Circle(5)  # Create a circle object with radius 5
print(f"Circle Area: {circle.area()}")  # Expected output: Area of circle
# Expected output: Perimeter of circle
print(f"Circle Perimeter: {circle.perimeter()}")

print("\nRectangle Example:")
# Create a rectangle object with length 4 and width 6
rectangle = Rectangle(4, 6)
# Expected output: Area of rectangle
print(f"Rectangle Area: {rectangle.area()}")
# Expected output: Perimeter of rectangle
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

print("\nSquare Example:")
square = Square(4)  # Create a square object with side length 4
print(f"Square Area: {square.area()}")  # Expected output: Area of square
# Expected output: Perimeter of square
print(f"Square Perimeter: {square.perimeter()}")

# Class Methods, Static Methods, and Polymorphism demonstration

# Demonstrating Class Method
print("\nClass Method Example:")
# It prints 'Circle' using the class method
print(f"Shape type: {Circle.shape_type()}")

# Demonstrating Static Method
print("\nStatic Method Example:")
Circle.info()  # Static method doesn't need an instance

# Polymorphism demonstration: We can call the same method name (area) on different objects of different types
print("\nPolymorphism Example:")
shapes = [Circle(3), Rectangle(4, 5), Square(6)]
for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area()}")

# Now, let's add abstract class and abstract methods for abstraction


class Shape(ABC):
    """
    A simple abstract class to represent a shape (with constructor).
    """

    def __init__(self):
        pass  # Constructor for the abstract class

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area. 
        This method must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter.
        This method must be implemented by all subclasses.
        """
        pass

    @classmethod
    def shape_type(cls):
        """
        Class method: This is used to get the type of the shape class.
        """
        return cls.__name__

    @staticmethod
    def info():
        """
        Static method: This is used to display general information about shapes.
        """
        print("Shapes are geometric figures that have area and perimeter.")

# Circle class (inherits from Shape, now implementing the abstract methods)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Encapsulation of radius attribute

    def area(self):
        return 3.14 * (self.radius ** 2)  # Area = πr²

    def perimeter(self):
        return 2 * 3.14 * self.radius  # Perimeter = 2πr

# Rectangle class (inherits from Shape, now implementing the abstract methods)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  # Encapsulation of length attribute
        self.width = width    # Encapsulation of width attribute

    def area(self):
        return self.length * self.width  # Area = length * width

    def perimeter(self):
        return 2 * (self.length + self.width)  # Perimeter = 2(length + width)

# Square class (inherits from Rectangle, now implementing abstract methods)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Inherits from Rectangle, but with equal sides

    def area(self):
        return self.length * self.width  # Inherited from Rectangle, but now a square

    def perimeter(self):
        return 4 * self.length  # Perimeter of square = 4 * side

# Testing the updated abstract classes and methods:


print("\nUpdated Circle Example with Abstract Class:")
circle = Circle(7)  # Create a circle object with radius 7
print(f"Circle Area: {circle.area()}")  # Expected output: Area of circle
# Expected output: Perimeter of circle
print(f"Circle Perimeter: {circle.perimeter()}")

print("\nUpdated Rectangle Example with Abstract Class:")
# Create a rectangle object with length 5 and width 10
rectangle = Rectangle(5, 10)
# Expected output: Area of rectangle
print(f"Rectangle Area: {rectangle.area()}")
# Expected output: Perimeter of rectangle
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

print("\nUpdated Square Example with Abstract Class:")
square = Square(6)  # Create a square object with side length 6
print(f"Square Area: {square.area()}")  # Expected output: Area of square
# Expected output: Perimeter of square
print(f"Square Perimeter: {square.perimeter()}")
