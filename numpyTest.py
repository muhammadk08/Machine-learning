import numpy as np

c = np.array([20, 1, 2, 3, 4])
print(c)

c[0] = 100
print(c)

d = c[1:4]
print(d)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])
print(arr[:4])
print(arr[4:])
print(arr[1:5:])

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr[1::2])

a = np.array([0, 1, 2, 3, 4])

print(a.size)
print(a.ndim)
print(a.shape)

X = np.array([1, 2])
Y = np.array([3, 2])

print(np.dot(X, Y))

x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)
print(y)

print(np.linspace(-2, 2, num=5))
print(np.linspace(-2, 2, num=9))