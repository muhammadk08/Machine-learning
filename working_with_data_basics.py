example1 = "example1.txt"  # change to your actual filename if needed

# # Read the entire file
# with open(example1, "r") as file1:
#     FileContent = file1.read()
#     print(FileContent)

# # Check if file is closed
# print(file1.closed)

# # See the content again (from the variable)
# print(FileContent)

# with open(example1, "r") as file1:
#     print(file1.read(4))

# with open(example1, "r") as file1:
#     print(file1.read(4))   # first 4 chars
#     print(file1.read(4))   
with open(example1, "r") as file1:
    print(file1.readline(20))
    print(file1.read(20))
