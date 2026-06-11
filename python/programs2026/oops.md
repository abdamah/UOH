# Chapter 6: Object-Oriented Programming (OOP)

---

## 1) Introduction to OOP

**Definition:**  
OOP (Object-Oriented Programming) is a programming paradigm based on objects and classes.

It helps organize code, reuse logic, and model real-world entities.

---

## 2) Class & Object

| Term | Meaning |
|------|---------|
| **Class** | Blueprint for creating objects |
| **Object** | Instance of a class |

```python
class Student:
    name = "Ali"
    age = 20

# create object
s1 = Student()

print(s1.name)
print(s1.age)
```

---

## 3) Constructor (`__init__`)

`__init__` is a special method called automatically when an object is created.  
It is used to initialize object values.

### Types of Constructors

| Type | Description | Parameters |
|------|-------------|------------|
| **Default Constructor** | No parameters (only `self`) | `def __init__(self):` |
| **Parameterized Constructor** | Takes values to initialize object data | `def __init__(self, name, age):` |

### 1) Default Constructor

Does not take any parameters except `self`. Sets default values inside the constructor.

```python
class Student:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

s1 = Student()
print(s1.name, s1.age)
```

### 2) Parameterized Constructor

Takes parameters to initialize object data when the object is created.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ahmed", 22)
print(s1.name, s1.age)
```

---

## 4) Types of Methods

Python classes support three types of methods:

| Method Type | Decorator | First Parameter | Works On |
|-------------|-----------|-----------------|----------|
| **Instance Method** | (none) | `self` | Object instance data |
| **Class Method** | `@classmethod` | `cls` | Class-level data |
| **Static Method** | `@staticmethod` | (none) | Independent utility logic |

### Instance Method

Uses `self` to access and modify object (instance) data. Called on an object.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am", self.name)

s1 = Student("Asha")
s1.greet()
```

### Class Method

Uses `cls` to access class-level data. Can create objects or modify class variables. Called on the class or an object.

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def from_age(cls, name, age):
        return cls(name)   # alternative constructor

Student.change_school("XYZ School")
print(Student.school)
```

### Static Method

Does not use `self` or `cls`. Behaves like a regular function inside the class namespace. Used for utility logic related to the class.

```python
class Student:
    @staticmethod
    def is_adult(age):
        return age >= 18

print(Student.is_adult(20))   # True
print(Student.is_adult(15))   # False
```

### All Three Together

```python
class Student:
    school = "ABC School"
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

    # Instance method ÿ works with object data
    def greet(self):
        print(f"Hello, I am {self.name} from {self.school}")

    # Class method ÿ works with class data
    @classmethod
    def get_count(cls):
        return cls.count

    # Static method ÿ no access to self or cls
    @staticmethod
    def is_adult(age):
        return age >= 18

s1 = Student("Ali", 20)
s1.greet()
print("Total students:", Student.get_count())
print("Is adult?", Student.is_adult(s1.age))
```

---

## 5) Class Variables vs Instance Variables

| Type | Description |
|------|-------------|
| **Class Variable** | Shared by all objects |
| **Instance Variable** | Unique for each object |

```python
class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable

s1 = Student("Ali")
s2 = Student("Ahmed")

print(s1.school, s2.school)
```

---

## 6) Encapsulation

**Encapsulation:** Restrict direct access to variables. Use private/protected variables with `_`.

```python
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
```

---

## 7) Inheritance

**Inheritance:** A child class inherits attributes and methods from a parent class.

### Types of Inheritance

| Type | Description | Structure |
|------|-------------|-----------|
| **Single** | One child inherits from one parent | `A ? B` |
| **Multi-level** | Chain of inheritance across levels | `A ? B ? C` |
| **Hierarchical** | Multiple children inherit from one parent | `A ? B`, `A ? C` |
| **Multiple** | One child inherits from multiple parents | `A, B ? C` |

### 1) Single Inheritance

Class **B** inherits from class **A**.

```python
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

obj = B()
obj.show()     # inherited from A
obj.display()  # defined in B
```

### 2) Multi-level Inheritance

Class **C** inherits from **B**, and **B** inherits from **A**.

```python
class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C(B):
    def method_c(self):
        print("Class C")

obj = C()
obj.method_a()  # from A
obj.method_b()  # from B
obj.method_c()  # from C
```

### 3) Hierarchical Inheritance

Classes **B** and **C** both inherit from class **A**.

```python
class A:
    def common(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C(A):
    def method_c(self):
        print("Class C")

b = B()
c = C()

b.common()   # from A
b.method_b()

c.common()   # from A
c.method_c()
```

### 4) Multiple Inheritance

Class **C** inherits from both **A** and **B**.

```python
class A:
    def method_a(self):
        print("Class A")

class B:
    def method_b(self):
        print("Class B")

class C(A, B):
    def method_c(self):
        print("Class C")

obj = C()
obj.method_a()  # from A
obj.method_b()  # from B
obj.method_c()  # from C
```

---

## 8) Polymorphism

**Polymorphism:** Same method name, different behavior.

```python
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in (Cat(), Dog()):
    animal.sound()
```

---

## 9) Abstraction

**Abstraction:** Hide implementation details. Use abstract classes.

```python
from abc import ABC, abstractmethod

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
```

---

## 10) Magic Methods (`__str__`)

Magic methods customize object behavior.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

s = Student("Ali")
print(s)
```

---

## 11) Simple Project: Bank System

**Project:** Simple Bank Account using OOP

```python
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
```

---

## 12) Summary

### OOP Concepts

- Class & Object
- Constructor (`__init__`) — default and parameterized
- Types of methods (instance, class, static)
- Class vs Instance variables
- Encapsulation
- Inheritance (single, multi-level, hierarchical, multiple)
- Polymorphism
- Abstraction

### Other

- Magic methods (`__str__`)

### Project

- Bank Account System
