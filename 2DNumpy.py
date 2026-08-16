import numpy as np

X = np.array([[1, 0],
              [0, 1]])
Y = np.array([[2, 1],
              [1, 2]])

print("X =\n", X)
print("Y =\n", Y)

Z_add = X + Y
print("X + Y =\n", Z_add)

Z_scalar = 2 * Y
print("2 * Y =\n", Z_scalar)

Z_hadamard = X * Y
print("X * Y (element-wise) =\n", Z_hadamard)


Z_dot = np.dot(X, Y)
print("np.dot(X, Y) =\n", Z_dot)

