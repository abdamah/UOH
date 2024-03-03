"""
  Object Oriented Programming in Python:
  is a method of structuring a program by bundling related 
  properties and behaviors into individual objects

  When we talk about OOPs we are talking about classes and objects.
  Pilars of OOPs:
  1. Encapsulation
  2. Inheritance
  3. Abstraction
  4. Polymorphism

  class: is a blueprint for creating objects.
  object: is an instance or copy of a class.
  if class contains two main things:
  1. data / variables /properties / attributes
  2. functions / methods / behaviors / actions
"""

# class definition
class Person:
  pass

"""
This is valid syntax of empty class with pass keyword to satisfy compiler.
"""

# object creation
person = Person()
"""
  Here we created instance of class Person, now we can access 
  properties and methods of class Person.
"""

# add properties to class
class Person:
  """These are class level  properties"""
  name = "John"
  age = 23
  country = "USA"

# object creation
person = Person()
print(person.name)
print(person.age)
print(person.country)

# construcotr
class Person:
  """Constructor is a special 
  method in a class used to create and 
  initialize an object of a class
  self: is special keyword that references same obejct or this class
  """
  def __init__(self, name, age, country):
    self.name = name
    self.age = age
    self.country = country

# object creation
person = Person("John", 23, "USA") # we ca pass arguments
print(person.name)
print(person.age)
print(person.country)

# add methods to class
class Person:
  def __init__(self, name, age, country) -> None:
    self.name = name
    self.age = age
    self.country = country

  def greet(self):
    print("Hello, my name is", self.name)

  def is_adult(self):
    if self.age >= 18:
      print("I am an adult")
    else:
      print("I am not an adult")

  def country_name(self):
    print("I am from", self.country)



# object creation
person = Person("John", 13, "USA")
# access methods
person.greet()
person.is_adult()
person.country_name()


#Inheritance
"""
  Inheritance: is a mechanism in
  which one class acquires the properties 
  and methods of another class.
  Inheritance contains two classes:
  1. Base class / parent class / super class
  2. Derived class / child class / sub class
"""

# Base class
class Shape:
  def area(self):
    print("Shape area")

# Derived class
class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height


# Derived class
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius * self.radius

# Another derived class
class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return 0.5 * self.base * self.height


# object creation
rectangle = Rectangle(10, 20)
circle = Circle(5)
triangle = Triangle(10, 20)
print("Rectangle area:",rectangle.area())
print("Circle area:",circle.area())
print("Triangle area:",triangle.area())



# Abstraction
"""
  Abstraction: is the process of hiding the
  internal details of an object from the
  external.
  or
  Absraction is the process of showing essentail features
  of an object to public.

  Python does not directly support abstraction but 
  we can make using abc module.

"""

from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

# We cannot instantiate abstract classes.
#TypeError: Can't instantiate abstract class Shape with abstract method area
# To check uncomment below line of code.
# shape = Shape() 

# class Rectangle should implement area method otherwise becames abstract class
class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

# class Circle should implement area method otherwise becames abstract class
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius * self.radius


# create list of shapes

shapes = [Rectangle(2, 3), Circle(2)]

for shape in shapes:
  print(shape.area())



# Access modifier in python
"""
  Access modifier in python:
  1. public 
  2. protected (_ single underscore)
  3. private (__ double underscore)

"""
class Person:
  def __init__(self, name, age, country):
    self.name = name
    self._age = age
    self.__country = country


# object creation
person = Person("John", 23, "USA")
# access public property
print(person.name)
# access protected property
print(person._age)
# access private property
print(person.__country) # AttributeError: 'Person' object has no attribute '__country'


# 4. Polymorphism
"""
  Polymorphism: is the ability of a
  method to behave differently in different

  Two methods that has same name but different behaviour is called
  polymorhism.
  poly: many
  morph: forms
  polymohism: many forms

  Types of polymohism:
  1. Method overloading
    two or more methods with same name but different parameters
  2. Method overriding
    two or more methods with same name but in different classes 
    this happens only when inheritance is used.
"""
# Method overloading

def calculate_tip(amount, tip_percentage = 10):
    total_payment = amount + (amount * (tip_percentage / 100))
    return total_payment

# Pass one positional required argument
print(calculate_tip(100)) # 120
# Pass one positional required arguments and one optional
print(calculate_tip(10, 20)) # 120

# Now we can say this method is overloaded method
# because it has same name but different parameters


# Method overriding

class Shape:
  def area(self):
    """Base class method print only 'Shape area'"""
    print("Shape area")

class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    """Derived class method print 'Rectangle area'"""
    super().area() ## we can use super() to call the base class method
    return self.width * self.height


# create object Shape class
shape = Shape()
shape.area()

# create object Rectangle class
rectangle = Rectangle(10, 20)
print(rectangle.area())

