"""
Exception:
- abnormal termination of program is called exception.
- Exception handling is used to handle the exception.
- Exception blocks:
. try block:
    code we are expecting to raise exeception.
. except block:
    code to handle the raised exception
. else block:
    code to handle the normal termination of program.
. finally block:
    code to be executed in any case. "Always executes"

"""


## Handle ZeroDivisonError

try:
  x = int(input("x:"))
  y = int(input("y:"))
  # if y = 0 ZeroDivisionError will be raised
  # So here we are expected to raise exception that is why 
  # we write inside try block
  result = x / y 
  print(result)

except ZeroDivisionError as e: # Here we are handling raised exception
  print(e) # This will print error message. You can print your own msg.

# Handle TypoError exception

try:
  x = input("x:") 
  y = input("y:")

  result = x / y
  print(result)
except ZeroDivisionError as e: 
  print(e) 
except TypeError as e:
  print(e)


#Handle Value Error:

try:
  x = input("x:") 
  y = input("y:")

  result = x / y
  print(result)
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
except ValueError as e:
  print(e)
#else block 

try:
  x = int(input("x:"))
  y = int(input("y:"))
  result = x / y
  print(result)

except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)

else:
  print("No exception raised")
# finally block


try:
  x = int(input("x:"))
  y = int(input("y:"))
  result = x / y
  print(result)

except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)

else:
  print("No exception raised")

finally:
  print("This will always execute")


# # Open file using nested try-except-finally

try:
  f = open("data.txt", "r")
  try:
      print(f.read())
  finally:
      f.close()
except FileNotFoundError as e:
  print(e)


# Alternative and clean way to open file
# with key will handle to close the file.
try:
  with open("data", "r") as file:
      file.write('Hello World')
except FileNotFoundError as e:
  print(e)