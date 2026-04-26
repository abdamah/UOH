# ==========================================
# CHAPTER 4: DATA STRUCTURES & FUNCTIONS
# ==========================================


# ==========================================
# 0) MUTABLE vs IMMUTABLE
# ==========================================

"""
Mutable:
Objects that CAN be changed after creation.

Examples:
- list
- set
- dictionary
"""

my_list = [1, 2, 3]
my_list[0] = 100   # ✅ allowed
print(my_list)


"""
Immutable:
Objects that CANNOT be changed after creation.

Examples:
- int
- float
- string
- tuple
"""

x = 10
x = 20   # creates new object (not modifying old one)

my_tuple = (1, 2, 3)
# my_tuple[0] = 100 ❌ Error

print(my_tuple)


# ==========================================
# 1) DATA STRUCTURES
# ==========================================

"""
Definition:
Data structures are used to store and organize data efficiently.
"""

# ------------------------------------------
# 1.1 LIST (Mutable)
# ------------------------------------------

numbers = [10, 20, 30, 40]

print(numbers[0])
numbers.append(50)
numbers.remove(20)

print(numbers)


# ------------------------------------------
# 1.2 TUPLE (Immutable)
# ------------------------------------------

coordinates = (10, 20)

print(coordinates[0])


# ------------------------------------------
# 1.3 SET (Mutable, Unique)
# ------------------------------------------

unique_numbers = {1, 2, 3, 3, 4}

print(unique_numbers)

unique_numbers.add(5)
unique_numbers.remove(2)

print(unique_numbers)


# ------------------------------------------
# 1.4 DICTIONARY (Mutable)
# ------------------------------------------

student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}

print(student["name"])

student["age"] = 21
student["city"] = "Hargeisa"

print(student)


# ==========================================
# 2) STACK PROJECT (USING LIST)
# ==========================================

"""
Stack follows LIFO (Last In First Out)
"""

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

stack.pop()
print("Stack after pop:", stack)

print("Top element:", stack[-1])


# ==========================================
# 3) FUNCTIONS
# ==========================================

"""
Definition:
Reusable block of code.
"""


def greet():
    print("Hello!")


greet()


def add(a, b):
    return a + b


print(add(2, 3))


# ==========================================
# 4) TYPES OF FUNCTIONS
# ==========================================

"""
- Built-in → print(), len()
- User-defined → def
- Lambda → small anonymous functions
"""


def square(x): return x * x


print(square(5))


# ==========================================
# 5) TYPES OF PARAMETERS
# ==========================================

# ------------------------------------------
# 5.1 POSITIONAL PARAMETERS
# ------------------------------------------

def add(a, b):
    print(a + b)


add(2, 3)


# ------------------------------------------
# 5.2 KEYWORD PARAMETERS
# ------------------------------------------

def introduce(name, age):
    print(name, age)


introduce(name="Ali", age=20)


# ------------------------------------------
# 5.3 DEFAULT PARAMETERS
# ------------------------------------------

def greet(name="Guest"):
    print("Hello", name)


greet()
greet("Ahmed")


# ------------------------------------------
# 5.4 ARBITRARY PARAMETERS (*args)
# ------------------------------------------

def total(*nums):
    print(sum(nums))


total(1, 2, 3, 4)


# ------------------------------------------
# 5.5 KEYWORD ARBITRARY (**kwargs)
# ------------------------------------------

def info(**data):
    print(data)


info(name="Ali", age=25)


# ------------------------------------------
# 5.6 POSITIONAL-ONLY PARAMETERS (/)
# ------------------------------------------

"""
Parameters BEFORE '/' must be passed positionally ONLY.
"""


def divide(a, b, /):
    print(a / b)


divide(10, 2)     # ✅ correct
# divide(a=10, b=2) ❌ Error


# ------------------------------------------
# 5.7 KEYWORD-ONLY PARAMETERS (*)
# ------------------------------------------

"""
Parameters AFTER '*' must be passed using keywords ONLY.
"""


def student_info(*, name, age):
    print(name, age)


student_info(name="Ali", age=20)   # ✅ correct
# student_info("Ali", 20) ❌ Error


# ------------------------------------------
# 5.8 COMBINED EXAMPLE
# ------------------------------------------

def example(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


example(1, 2, 3, 4, e=5, f=6)


# ==========================================
# 6) SUMMARY
# ==========================================

"""
Mutable:
- list, set, dictionary

Immutable:
- int, float, string, tuple

Data Structures:
- List → ordered, mutable
- Tuple → ordered, immutable
- Set → unique elements
- Dictionary → key-value

Functions:
- Reusable logic

Parameter Types:
- Positional
- Keyword
- Default
- *args
- **kwargs
- Positional-only (/)
- Keyword-only (*)

# ==========================================================
# SIMPLE PROJECT: STACK USING FUNCTIONS (MENU-DRIVEN)
# ==========================================================

'''
Stack Operations:
- push()  → add element
- pop()   → remove top element
- peek()  → view top element
- size()  → number of elements
- find()  → search element
'''

stack = []


# ------------------------------------------
# FUNCTIONS
# ------------------------------------------

def push(value):
    stack.append(value)
    print("Pushed:", value)


def pop():
    if stack:
        print("Popped:", stack.pop())
    else:
        print("Stack is empty")


def peek():
    if stack:
        print("Top element:", stack[-1])
    else:
        print("Stack is empty")


def size():
    print("Stack size:", len(stack))


def find(value):
    if value in stack:
        print(value, "found at position", stack.index(value))
    else:
        print(value, "not found in stack")


def display():
    print("Current Stack:", stack)


# ------------------------------------------
# MENU USING WHILE LOOP
# ------------------------------------------

while True:
    print("\n===== STACK MENU =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Find")
    print("6. Display")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = int(input("Enter value: "))
        push(value)

    elif choice == "2":
        pop()

    elif choice == "3":
        peek()

    elif choice == "4":
        size()

    elif choice == "5":
        value = int(input("Enter value to find: "))
        find(value)

    elif choice == "6":
        display()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
"""
