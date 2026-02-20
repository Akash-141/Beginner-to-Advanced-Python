# Writing to a file
with open("sample.txt", "w") as file:
    file.write("This is a sample file.")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("sample.txt", "a") as file:
    file.write("\nThis is an appended line.")

# Reading line by line
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
