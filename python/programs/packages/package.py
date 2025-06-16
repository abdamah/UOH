"""
In Python, a package is a way to organize related modules together. 
A package is essentially a directory that contains a special __init__.py file, 
which can be empty or contain initialization code for the package.

Here’s a simple example:

Step 1: Create a Package Structure
my_package/
├── __init__.py
├── module1.py
└── module2.py

my_package/ is the package.
- __init__.py indicates that this directory is a package.
- module1.py and module2.py are modules within the package.

Step 2: Write Code in Modules
module1.py
def greet(name):
    return f"Hello, {name}!"

module2.py
def add(a, b):
    return a + b

init.py
This file can be left empty or contain the following to make the modules easily accessible:
from .module1 import greet
from .module2 import add
"""

# Simulating module1.py
# This module contains a function to greet a user by name.


def greet(name):
    return f"Hello, {name}!"

# Simulating module2.py
# This module contains a function to add two numbers.


def add(a, b):
    return a + b


# Simulating main.py
# This is the script that uses the package and its functionalities.
if __name__ == "__main__":
    # Using the simulated package
    print(greet("Alice"))  # Output: Hello, Alice!
    print(add(3, 5))       # Output: 8
