# Example of file handling with different access modes in Python

# Writing to a file (write mode - 'w')
with open("example.txt", "w") as file:
    file.write("This is written in 'write' mode.\n")
    print("Data written to the file in 'write' mode.")

# Reading from a file (read mode - 'r')
with open("example.txt", "r") as file:
    content = file.read()
    print("\nReading in 'read' mode:")
    print(content)

# Appending to a file (append mode - 'a')
with open("example.txt", "a") as file:
    file.write("This line is added in 'append' mode.\n")
    print("Data appended to the file in 'append' mode.")

# Reading the updated file (read mode - 'r' again)
with open("example.txt", "r") as file:
    content = file.read()
    print("\nUpdated content after appending:")
    print(content)

# Reading and writing to a file (read+write mode - 'r+')
with open("example.txt", "r+") as file:
    file.write("New data written in 'r+' mode.\n")  # Overwrites starting part
    file.seek(0)  # Move the cursor to the beginning of the file
    content = file.read()
    print("\nContent after 'r+' mode:")
    print(content)

# Writing and reading a file (write+read mode - 'w+')
with open("example_w+.txt", "w+") as file:
    file.write("This is written in 'w+' mode.\n")  # Completely overwrites file
    file.seek(0)  # Move the cursor to the beginning
    content = file.read()
    print("\nContent in 'w+' mode:")
    print(content)

# Appending and reading a file (append+read mode - 'a+')
with open("example.txt", "a+") as file:
    file.write("Data added in 'a+' mode.\n")  # Appends new data
    file.seek(0)  # Move the cursor to the beginning
    content = file.read()
    print("\nContent after 'a+' mode:")
    print(content)
