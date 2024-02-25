# ========List=======
# Is a collection which is ordered and changeable. Allows duplicate members.

#Example:
numbers = [1, 2, 3, 4, 5]
# indexing:
# print first element
print(numbers[0]) # output 1, because index 1 is 0
# print last element
print(numbers[-1]) # output 5, because index 5 is -1 . Negative indexing.

# print all elements
print(numbers)

# replace element /assign value
numbers[0] = 10
print(numbers) # output [10, 2, 3, 4, 5]

# Insert element at first index
numbers.insert(0, 20)
print(numbers) # output [20, 10, 2, 3, 4, 5]
# Insert element at middle index
numbers.insert(2, 30)
print(numbers) # output [20, 10, 30, 2, 3, 4, 5]
# Insert element at last index
numbers.append(40)
print(numbers) # output [20, 10, 30, 2, 3, 4, 5, 40]

# Remove element at first index
numbers.pop(0)
print(numbers) # output [10, 30, 2, 3, 4, 5, 40]

# Get list length
print(len(numbers)) # output 7

# loop over list using for loop
for number in numbers:
  print(number, end=' ')

print() # Terminal purpose only
# Loop over list using while loop
i = 0
while i < len(numbers):
  print(numbers[i], end=' ')
  i += 1

print() # For terminal clearence

# Check element of list is even or odd
for number in numbers:
  if number % 2 == 0:
    print(f"{number} is even")
  else:
    print(f"{number} is odd")

# clear list
numbers.clear()

# ========Tuple=======
# Is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are immutable objects
# Example:
colors = ('red', 'green', 'blue')
# indexing:
# print first element
print(colors[0]) # output red
# print last element
print(colors[-1]) # output blue
# print all elements
print(colors)

# replace element /assign value
# colors[0] = 'yellow' # TypeError: 'tuple' object does not support item assignment

# Insert element at first index
# colors.insert(0, 'yellow') # TypeError: 'tuple' object does not support item assignment

# Insert element at middle index
# colors.insert(2, 'yellow') # TypeError: 'tuple' object does not support item assignment

# Insert element at last index
colors = colors + ('yellow',)
print(colors) # output ('red', 'green', 'blue', 'yellow')

# Remove element at first index
# colors.pop(0) # TypeError: 'tuple' object does not support item assignment

# Get list length
print(len(colors)) # output 4

# loop over tuple using for loop
for color in colors:
  print(color, end=' ')

print() # Terminal purpose only

# Loop over tuple using while loop
i = 0
while i < len(colors):
  print(colors[i], end=' ')
  i += 1

print() # For terminal clearence


# ========Set======== 
# Is a collection which is unordered, unchangeable*, and unindexed. 
# No duplicate members.
#Example:
permisions = {'read', 'write', 'execute'}
# indexing:
# print first element
# print(permisions[0]) # TypeError: 'set' object is not subscriptable

# print all elements
print(permisions)

# replace element /assign value
# permisions[0] = 'read' # TypeError: 'set' object does not support item assignment

# Insert element at first index
# permisions.insert(0, 'read') # TypeError: 'set' object does not support item assignment

# Insert element at middle index
# permisions.insert(2, 'read') # TypeError: 'set' object does not support item assignment

# Insert element 
permisions = permisions | {'others'}
print(permisions) # output {'read', 'write', 'execute', 'read'}

# insert element using add
permisions.add('readwrite')
print(permisions) # output {'read', 'write', 'execute', 'read', 'readwrite'}

# Loop over set using for loop
for permision in permisions:
  print(permision, end=' ')

print() # Terminal purpose only

  

# ==============Dictionary=======
# Is a collection which is ordered** and changeable. No duplicate members.

# Example:
commands = {
  'cat': 'Create or read file',
  'ls': 'List files',
  'rm': 'Remove file',
  'mkdir': 'Create directory',
  'cd': 'Change directory',
  'pwd': 'Print working directory',
  'touch': 'Create or update file',
  'mv': 'Move file',
  'cp': 'Copy file',
  'default': 'Invalid command'
}

# indexing:
# print first element
print(commands['cat']) # output Create or read file
# print all elements
print(commands)
# replace element /assign value
commands['touch'] = 'Create  zero byte file'
print(commands) 
# Insert element at first index
# commands.insert(0, 'read') # TypeError: 'set' object does not support item assignment
# Insert element at middle index
# commands.insert(2, 'read') # TypeError: 'set' object does not support item assignment
# Add element
commands['rmdir'] = 'Remove empty directory'
print(commands)

# Remove element
print(commands.pop('cat'))

# Loop over dictionary using for loop
for command in commands:
  print(command, commands[command])

print() # Terminal purpose only


# simple programming using dictionary

while True:
  command = input("> ").lower()
  if command == 'exit':
    break 
  print(commands.get(command, commands['default']))

print()
