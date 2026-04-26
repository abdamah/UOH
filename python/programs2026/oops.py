# ==========================================
# CHAPTER 6: OBJECT-ORIENTED PROGRAMMING (OOP)
# ==========================================


# ==========================================
# 1) INTRODUCTION TO OOP
# ==========================================

"""
Definition:
OOP (Object-Oriented Programming) is a programming paradigm
based on objects and classes.

It helps organize code, reuse logic, and model real-world entities.
"""


# ==========================================
# 2) CLASS & OBJECT
# ==========================================

"""
Class:
Blueprint for creating objects.

Object:
Instance of a class.
"""


from abc import ABC, abstractmethod
class Student:
    name = "Ali"
    age = 20


# create object
s1 = Student()

print(s1.name)
print(s1.age)


# ==========================================
# 3) __init__ CONSTRUCTOR
# ==========================================

"""
__init__ is a special method called automatically
when object is created.
Used to initialize values.
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Ahmed", 22)
print(s1.name, s1.age)


# ==========================================
# 4) INSTANCE METHODS
# ==========================================

"""
Instance methods use 'self' to access object data.
"""


class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am", self.name)


s1 = Student("Asha")
s1.greet()


# ==========================================
# 5) CLASS VARIABLES vs INSTANCE VARIABLES
# ==========================================

"""
Class Variable:
Shared by all objects.

Instance Variable:
Unique for each object.
"""


class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable


s1 = Student("Ali")
s2 = Student("Ahmed")

print(s1.school, s2.school)


# ==========================================
# 6) ENCAPSULATION
# ==========================================

"""
Encapsulation:
Restrict direct access to variables.
Use private variables with '_'
"""


class BankAccount:
    def __init__(self, balance):
        self._balance = balance   # protected

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance


acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())


# ==========================================
# 7) INHERITANCE
# ==========================================

"""
Inheritance:
Child class inherits from parent class.
"""


class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()
d.speak()
d.bark()


# ==========================================
# 8) POLYMORPHISM
# ==========================================

"""
Polymorphism:
Same method name, different behavior.
"""


class Cat:
    def sound(self):
        print("Meow")


class Dog:
    def sound(self):
        print("Bark")


for animal in (Cat(), Dog()):
    animal.sound()


# ==========================================
# 9) ABSTRACTION
# ==========================================

"""
Abstraction:
Hide implementation details.
Use abstract classes.
"""


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


r = Rectangle(5, 4)
print("Area:", r.area())


# ==========================================
# 10) MAGIC METHODS (__str__)
# ==========================================

"""
Magic methods customize object behavior.
"""


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"


s = Student("Ali")
print(s)


# ==========================================
# 11) SIMPLE PROJECT: BANK SYSTEM
# ==========================================

"""
Project:
Simple Bank Account using OOP
"""


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Balance:", self.balance)


# usage
acc = BankAccount("Ali", 1000)

acc.deposit(500)
acc.withdraw(300)
acc.check_balance()


# ==========================================
# 12) SUMMARY
# ==========================================

"""
OOP Concepts:
- Class & Object
- Constructor (__init__)
- Instance methods
- Class vs Instance variables
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

Other:
- Magic methods (__str__)

Project:
✔ Bank Account System
"""
