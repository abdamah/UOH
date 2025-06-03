# 1. Defining a Simple Class
import math
from abc import ABC, abstractmethod


class Person:
    """A simple class to represent a person."""

    def greet(self):
        print("Hello, how are you?")


# Creating an object of the class
person1 = Person()
person1.greet()  # Output: Hello, how are you?


# 2. Class with Constructor
class PersonWithConstructor:
    """A class with a constructor to initialize attributes."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating an object with constructor
person2 = PersonWithConstructor("Alice", 30)
person2.greet()  # Output: Hello, my name is Alice and I am 30 years old.


# 3. Class Attributes and Methods
class Circle:
    """A class to represent a circle."""
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    def area(self):
        return Circle.pi * (self.radius ** 2)


# Accessing class attributes and methods
circle = Circle(5)
# Output: Area of the circle: 78.53975
print(f"Area of the circle: {circle.area()}")


# 4. Encapsulation
class BankAccount:
    """A class to represent a bank account."""

    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


# Using encapsulation
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(f"Balance: {account.get_balance()}")  # Output: Balance: 1200


# 5. Inheritance
class Animal:
    """Base class for animals."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):
    """Derived class representing a dog."""

    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    """Derived class representing a cat."""

    def speak(self):
        print(f"{self.name} says Meow!")


# Creating objects of derived classes
dog = Dog("Rex")
cat = Cat("Mittens")

# Calling overridden methods
dog.speak()  # Output: Rex says Woof!
cat.speak()  # Output: Mittens says Meow!


# 5.1 Child Class with Its Own Constructor
class DogWithBreed(Animal):
    """Derived class with an additional constructor."""

    def __init__(self, name, breed):
        # Call the parent class constructor
        super().__init__(name)
        self.breed = breed  # Additional attribute specific to the child class

    def speak(self):
        print(f"{self.name} says Woof! It is a {self.breed}.")


# Using the class with its own constructor
dog_with_breed = DogWithBreed("Max", "Labrador")
print(f"Dog's Name: {dog_with_breed.name}")  # Access parent class attribute
print(f"Dog's Breed: {dog_with_breed.breed}")  # Access child class attribute
dog_with_breed.speak()  # Calls the overridden speak method

# Output:
# Dog's Name: Max
# Dog's Breed: Labrador
# Max says Woof! It is a Labrador.


# 6. Polymorphism
def animal_sound(animal):
    """A function to demonstrate polymorphism."""
    animal.speak()


# Passing different animal objects
animal_sound(dog)  # Output: Rex says Woof!
animal_sound(cat)  # Output: Mittens says Meow!
animal_sound(dog_with_breed)  # Output: Max says Woof! It is a Labrador.


# 7. Multiple Inheritance Example
class Bird:
    """Class representing a bird."""

    def fly(self):
        print("Bird can fly.")


class Fish:
    """Class representing a fish."""

    def swim(self):
        print("Fish can swim.")


class Penguin(Bird, Fish):
    """Derived class inheriting from both Bird and Fish."""

    def speak(self):
        print("Penguins cannot fly but can swim.")


penguin = Penguin()
penguin.fly()   # Output: Bird can fly.
penguin.swim()  # Output: Fish can swim.
penguin.speak()  # Output: Penguins cannot fly but can swim.


# 7.1 Method Resolution Order (MRO) in Multiple Inheritance
class Base1:
    def action(self):
        print("Action from Base1")


class Base2:
    def action(self):
        print("Action from Base2")


class Derived(Base1, Base2):
    pass


# Creating an object of Derived
derived = Derived()
derived.action()  # Output: Action from Base1

# Checking the MRO
print(Derived.mro())
# Output: [<class '__main__.Derived'>, <class '__main__.Base1'>, <class '__main__.Base2'>, <class 'object'>]


# 8. Abstract Classes

# Define an abstract class

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Method to calculate the area of the shape."""
        pass

# Define a Circle subclass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Define a Rectangle subclass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Define a Triangle subclass


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Creating instances of the shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

# Printing the areas
# Output: Circle Area: 78.53981633974483
print(f"Circle Area: {circle.area()}")
print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 24
print(f"Triangle Area: {triangle.area()}")  # Output: Triangle Area: 10.5
