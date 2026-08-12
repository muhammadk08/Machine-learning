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