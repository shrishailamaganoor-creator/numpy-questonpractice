#20 basic level questions i practiced whilee learning numpy
import numpy as np
print("="*62)
print( """#practice questions""" )
print("="*62)
print("■"*50)


# 1. How do you create a NumPy array from a Python list?
l1 = [1, 2, 3, 4, 6]
ar = np.array(l1)
print(ar)
print("■"*50)

# 2. ERROR
# Difference between np.array() and np.asarray()
a = np.array([1, 2, 3])
print(np.array(a))      # Creates a copy (by default)
print(np.asarray(a))    # Doesn't copy if input is already a NumPy array
print("was mistaken")
print("■"*50)

# 3. How do you create an array of zeros/ones of shape (3,4)?
o = np.zeros((3,4))
print(o)
print("■"*50)

# 4. What does np.arange(0, 10, 2) return?
print(np.arange(0,10,2))
print("■"*50)

# 5. How do you generate 5 evenly spaced numbers between 0 and 1?
print(np.linspace(0,1,5))
print("■"*50)

# 6. How do you check an array's shape, size, and dtype?
print(ar.shape)
print(ar.size)
print(ar.dtype)
print("■"*50)

# 7. How do you reshape a 1D array of 12 elements into (3,4)?
arr12 = np.arange(1,13)
print(arr12.reshape((3,4)))
print("■"*50)

# 8. How do you access the last element of a 1D array?
print(ar[-1])
print("■"*50)

# 9. ERROR
# How do you slice the first 3 rows of a 2D array?
a = np.array([[1,2],
              [3,4],
              [5,6],
              [7,8]])

print(a[:3])
#array[rows, columns]
print(" was mistaken")
print("■"*50)

# 10. What does arr[::-1] do?
print(ar[::-1])
print("■"*50)

# 11. How do you find the sum, mean, and max of an array?
print(np.sum(ar))
print(np.mean(ar))
print(np.max(ar))
print("■"*50)

# 12. How do you create an identity matrix with np.eye()?
print(np.eye(4))
print("■"*50)

# 13. How do you generate random integers between 1 and 100?
print(np.random.randint(1,100))
print("■"*50)

# 14. What's the difference between a NumPy array and a Python list?
# NumPy arrays are faster, support vectorized operations,
# and require all elements to be of the same data type.
print(l1 == [1,2,3,4,6])
print("■"*50)

# 15. How do you check if two arrays are equal element-wise?
l2 = np.arange(1,6)
print(ar == l2)
print("■"*50)

# 16. How do you concatenate two 1D arrays?
print(np.concatenate((ar, l2)))
print("■"*50)

# 17. How do you find the data type of an array and convert it?
print(l2.dtype)
print(l2.astype(float))
print("■"*50)

# 18. How do you create a 2D array?
a = np.array([[1,2],[3,4]])
print(a)
print("■"*50)

# 19. How do you find the number of dimensions (ndim) of an array?
print(a.ndim)
print("■"*50)

# 20. How do you flatten a multi-dimensional array?
b = np.array([[[1,2],[3,4]]])
print(b.flatten())
print("■"*50)


