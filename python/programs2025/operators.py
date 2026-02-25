# Static values
a = 10
b = 5

print(f"Values: a = {a}, b = {b}")

print("\nArithmetic Operators:")
print(f"{a} + {b} = {a + b}")  # Addition
print(f"{a} - {b} = {a - b}")  # Subtraction
print(f"{a} * {b} = {a * b}")  # Multiplication
print(f"{a} / {b} = {a / b}")  # Division
print(f"{a} % {b} = {a % b}")  # Modulus
print(f"{a} ** {b} = {a ** b}")  # Exponentiation
print(f"{a} // {b} = {a // b}")  # Floor Division

print("\nComparison Operators:")
print(f"{a} == {b}: {a == b}")  # Equal to
print(f"{a} != {b}: {a != b}")  # Not equal to
print(f"{a} > {b}: {a > b}")    # Greater than
print(f"{a} < {b}: {a < b}")    # Less than
print(f"{a} >= {b}: {a >= b}")  # Greater than or equal to
print(f"{a} <= {b}: {a <= b}")  # Less than or equal to

print("\nLogical Operators:")
print(f"{a} > 0 and {b} > 0: {a > 0 and b > 0}")  # Logical AND
print(f"{a} > 0 or {b} > 0: {a > 0 or b > 0}")    # Logical OR
print(f"not({a} > 0): {not(a > 0)}")              # Logical NOT

print("\nBitwise Operators:")
print(f"{a} & {b}: {a & b}")  # Bitwise AND
print(f"{a} | {b}: {a | b}")  # Bitwise OR
print(f"{a} ^ {b}: {a ^ b}")  # Bitwise XOR
print(f"~{a}: {~a}")          # Bitwise NOT
print(f"{a} << 1: {a << 1}")  # Left shift
print(f"{b} >> 1: {b >> 1}")  # Right shift

print("\nAssignment Operators:")
x = a
x += b
print(f"x += {b}: {x}")
x = a
x -= b
print(f"x -= {b}: {x}")
x = a
x *= b
print(f"x *= {b}: {x}")
x = a
x /= b
print(f"x /= {b}: {x}")
x = a
x %= b
print(f"x %= {b}: {x}")
x = a
x **= b
print(f"x **= {b}: {x}")
x = a
x //= b
print(f"x //= {b}: {x}")
