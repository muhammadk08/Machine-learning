filename = "demo_file.txt"

with open(filename, "w") as f:
    f.write("Line A\n")


with open(filename, "w") as f:
    f.write("Line A\n")
    f.write("Line B\n")

lines = ["Line A\n", "Line B\n", "Line C\n"]

with open(filename, "w") as f:
    for line in lines:
        f.write(line)

with open(filename, "w") as f:
    f.write("Overwrite\n")

with open(filename, "a") as f:
    f.write("Line C\n")
    f.write("Line D\n")
    f.write("Line E\n")

with open(filename, "a+") as f:
    f.write("Line F\n")
    # At this point, the cursor is at the end of the file
    data = f.read()
    print("Read after writing with a+:", repr(data))