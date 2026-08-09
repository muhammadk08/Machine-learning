# # Integer
# x = 42
# print(type(x))        # <class 'int'>

# # Float
# y = 3.14
# print(type(y))        # <class 'float'>

# # String
# name = "Alice"
# print(type(name))     # <class 'str'>

# # More examples directly on expressions
# print(type(10))       # <class 'int'>
# print(type(2.5))      # <class 'float'>
# print(type("hello"))  # <class 'str'>
# print(type(True))     # <class 'bool'>


# x = 2
# print(float(x))  # 2.0

# y = 3.6
# print(int(y))    # 3

# z = "10"
# print(int(z))    # 10

age = 18
print(age >= 18)  # True
print(age < 18)   # False

# Find the length (number of characters) in the string
len("The BodyGuard")   # 12

s = "The BodyGuard"

# Get characters from index 0 up to (but not including) 4
print(s[0:4])   # "The "

# Get characters from index 8 up to 12
print(s[8:12])  # "uard"

a = "Thriller is the sixth studio album"
print("before upper:", a)

b = a.upper()
print("after upper:", b)

a = "The BodyGuard is the best album"
b = a.replace("BodyGuard", "Janet")
print(b)  # "The Janet is the best album"

text = "The BodyGuard"
print(text.find("he"))   # 1
print(text.find("Body")) # 4