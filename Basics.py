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


# # # # x = 2
# # # # print(float(x))  # 2.0

# # # # y = 3.6
# # # # print(int(y))    # 3

# # # # z = "10"
# # # # print(int(z))    # 10

# # # age = 18
# # # print(age >= 18)  # True
# # # print(age < 18)   # False

# # # # Find the length (number of characters) in the string
# # # len("The BodyGuard")   # 12

# # # s = "The BodyGuard"

# # # # Get characters from index 0 up to (but not including) 4
# # # print(s[0:4])   # "The "

# # # # Get characters from index 8 up to 12
# # # print(s[8:12])  # "uard"

# # # a = "Thriller is the sixth studio album"
# # # print("before upper:", a)

# # # b = a.upper()
# # # print("after upper:", b)

# # # a = "The BodyGuard is the best album"
# # # b = a.replace("BodyGuard", "Janet")
# # # print(b)  # "The Janet is the best album"

# # # text = "The BodyGuard"
# # # print(text.find("he"))   # 1
# # # print(text.find("Body")) # 4

# # L = ["The Bodyguard", 7.0]

# # L.extend(["pop", 10])
# # print(L)   # adds 2 separate elements
# # L = ["The Bodyguard", 7.0]

# # L.append(["pop", 10])
# # print(L)   # adds 1 new nested list

# # A = ["disco", 10, 1.2]
# # A[0] = "hard rock"
# # print(A)
# # A = ["hard rock", 10, 1.2]
# # del(A[0])
# # print(A)
# # print("hard rock".split())      # splits by spaces
# # print("A,B,C,D".split(","))     # splits by comma

# release_year_dict = {
#     "Thriller": "1982",
#     "Back in Black": "1980",
#     "The Dark Side of the Moon": "1973"
# }

# print(release_year_dict.keys())
# print(release_year_dict.values())

# release_year_dict["Graduation"] = "2007"
# print(release_year_dict)
# del(release_year_dict["Thriller"])
# print(release_year_dict)

# A = {"AC/DC", "Thriller", "Back in Black"}
# print(A)
# A.add("NSYNC")
# print(A)

# A.remove("NSYNC")
# print(A)

# print("AC/DC" in A)     # True or False
# print("Beatles" in A)   # False
 
# album_set1 = set(["Thriller", "AC/DC", "Back in Black"])
# album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])

# print(album_set1)
# print(album_set2)
# print(album_set1 & album_set2)
# # or
# print(album_set1.intersection(album_set2))

# print(album_set1.difference(album_set2))
# print(album_set2.difference(album_set1))

# try:
#     number = int("hello")
#     result = 10 / number

# except ZeroDivisionError:
#     print("You cannot divide by zero.")

# except ValueError:
#     print("That was not a valid whole number.")