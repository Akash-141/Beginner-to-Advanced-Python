# Writing to a file
with open("sample.txt", "w") as f:
    f.write("This is line 1.\n")
    f.write("This is line 2.\n")

# Reading the file
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# Appending to the file
with open("sample.txt", "a") as f:
    f.write("This is line 3.\n")

# Reading line by line
with open("sample.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
