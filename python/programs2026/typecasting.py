# ==========================================
# Chapter2: PYTHON TYPE CASTING
# ==========================================

"""
Definition:
Type casting (or type conversion) is the process of converting 
a variable from one data type to another.
Python supports built-in functions to perform type casting.
"""

# ==========================================
# 1) INT() - Convert to Integer
# ==========================================

"""
Definition:
int() converts a compatible value into an integer.
- Floats are truncated (decimal part removed)
- Strings must represent a valid number
"""

x = 10.9
y = "20"

print("Original x (float):", x, type(x))
x_int = int(x)
print("x converted to int:", x_int, type(x_int))

y_int = int(y)
print("y converted to int:", y_int, type(y_int))


# ==========================================
# 2) FLOAT() - Convert to Float
# ==========================================

"""
Definition:
float() converts a value to decimal (floating point) number.
"""

x = 10
y = "20.5"

x_float = float(x)
y_float = float(y)

print("x converted to float:", x_float, type(x_float))
print("y converted to float:", y_float, type(y_float))


# ==========================================
# 3) STR() - Convert to String
# ==========================================

"""
Definition:
str() converts a value to string representation.
"""

x = 100
y = 25.99

x_str = str(x)
y_str = str(y)

print("x as string:", x_str, type(x_str))
print("y as string:", y_str, type(y_str))


# ==========================================
# 4) BOOL() - Convert to Boolean
# ==========================================

"""
Definition:
bool() converts a value to True or False.
- Zero, empty strings, empty containers → False
- Non-zero numbers, non-empty strings/containers → True
"""

x = 0
y = 5
z = ""
w = "Python"

print("bool(x):", bool(x))
print("bool(y):", bool(y))
print("bool(z):", bool(z))
print("bool(w):", bool(w))


# ==========================================
# 5) COMPLEX() - Convert to Complex Number
# ==========================================

"""
Definition:
complex() converts numbers or strings to a complex number.
- Complex numbers have a real and imaginary part
"""

x = 10
y = 5.5

x_complex = complex(x)
y_complex = complex(y)

print("x as complex:", x_complex, type(x_complex))
print("y as complex:", y_complex, type(y_complex))


# ==========================================
# 6) NOTES
# ==========================================

# ==========================================
# PYTHON TYPE CASTING: IMPLICIT AND EXPLICIT
# ==========================================

"""
Definition:
Type casting (type conversion) is changing a variable from one data type to another.

1) Implicit Type Casting:
   - Python automatically converts one data type to another
   - Happens without programmer intervention
   - Also called "type coercion"

2) Explicit Type Casting:
   - Programmer manually converts a variable from one type to another
   - Done using built-in functions like int(), float(), str(), bool(), complex()
"""

# ==========================================
# 1) IMPLICIT CASTING
# ==========================================

"""
Definition:
Python automatically converts a smaller type to a larger type to avoid data loss.
"""

a = 10      # int
b = 5.5     # float

# Python automatically converts a → float before addition
c = a + b
print("Result of a + b:", c, type(c))  # type is float

# Another example:
x = 100          # int
y = 2.5          # float
z = x * y        # int * float → float
print("x * y:", z, type(z))


# ==========================================
# 2) EXPLICIT CASTING
# ==========================================

"""
Definition:
Programmer manually converts the data type using built-in functions.
"""

x = 10.7
y = "20"

# Convert float to int
x_int = int(x)    # removes decimal part
print("x converted to int:", x_int, type(x_int))

# Convert string to float
y_float = float(y)
print("y converted to float:", y_float, type(y_float))

# Convert int to string
a = 100
a_str = str(a)
print("a converted to string:", a_str, type(a_str))

# Convert int to boolean
b = 0
b_bool = bool(b)
print("b converted to bool:", b_bool, type(b_bool))

# Convert numbers to complex
c = 5
c_complex = complex(c)
print("c converted to complex:", c_complex, type(c_complex))


# ==========================================
# 3) SUMMARY
# ==========================================

"""
- Implicit Casting (Automatic):
  Python converts smaller data type → larger data type automatically
  Example: int + float → float

- Explicit Casting (Manual):
  Programmer uses functions like int(), float(), str(), bool(), complex()
  to convert types manually
"""
