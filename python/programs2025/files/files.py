# Writing to a file (with "with" keyword)
# The 'with' statement automatically handles closing the file when done
with open("example_with.txt", "w") as file:
    file.write("Hello, world!\n")  # Writing a line to the file
    # Writing another line
    file.write("Welcome to Python file handling with 'with'.\n")

# Explanation:
# The 'with' statement opens the file in write mode ('w') and ensures that the file is closed
# when the block is exited. This makes file handling safer by avoiding forgotten file closures.

# Reading from a file (with "with" keyword)
# The file is opened in read mode and its contents are printed
with open("example_with.txt", "r") as file:
    content = file.read()  # Read all content of the file
    print("File Content (with 'with'):\n", content)  # Display the content

# Explanation:
# Using 'with' here ensures that the file is automatically closed after reading.
# The file is opened in read mode ('r') and the content is stored in the variable 'content'
# and then printed.

# Appending to a file (with "with" keyword)
# Opens the file in append mode and adds new data to the end
with open("example_with.txt", "a") as file:
    file.write("\nLet's append this line with 'with'.")  # Append a new line

# Explanation:
# The 'a' mode opens the file in append mode, meaning new data is added at the end of the file
# without modifying the existing content.

# Reading line by line (with "with" keyword)
# Opens the file in read mode and reads line by line
with open("example_with.txt", "r") as file:
    print("\nReading line by line (with 'with'):")
    for line in file:  # Loop through each line
        print(line.strip())  # Print each line, removing extra whitespace

# Explanation:
# This approach reads the file line by line. It is useful when dealing with large files as it
# prevents reading everything into memory at once. The 'strip()' method removes leading and trailing spaces.

# Writing to a file (without "with" keyword)
# Open the file in write mode and manually close it after use
file = open("example_without.txt", "w")  # Open file for writing
file.write("Hello, world!\n")  # Writing a line
# Writing another line
file.write("Welcome to Python file handling without 'with'.\n")
file.close()  # Explicitly close the file

# Explanation:
# Here, the file is opened using the 'open()' function without 'with'.
# After the file is written to, we must remember to manually close the file using 'file.close()'.

# Reading from a file (without "with" keyword)
# Open the file and manually close it after reading its contents
file = open("example_without.txt", "r")  # Open file for reading
content = file.read()  # Read all content from the file
print("\nFile Content (without 'with'):\n", content)  # Display the content
file.close()  # Explicitly close the file

# Explanation:
# Similar to writing, we open the file for reading using 'open()' without 'with'.
# After reading the content, we manually close the file to free up system resources.

# Appending to a file (without "with" keyword)
# Open the file in append mode and add content manually
file = open("example_without.txt", "a")  # Open file for appending
file.write("\nLet's append this line without 'with'.")  # Append new content
file.close()  # Explicitly close the file

# Explanation:
# The file is opened in append mode ('a') and new data is added to the end without overwriting
# the existing content. Afterward, the file is closed manually.

# Reading line by line (without "with" keyword)
# Open the file in read mode and manually close it after reading line by line
file = open("example_without.txt", "r")  # Open file for reading
print("\nReading line by line (without 'with'):")
for line in file:  # Loop through each line
    print(line.strip())  # Print each line, removing extra whitespace
file.close()  # Explicitly close the file

# Explanation:
# Similar to the 'with' approach, here we read the file line by line. This method is memory efficient
# for larger files, but we must remember to manually close the file when done.
