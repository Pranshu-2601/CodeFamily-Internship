import numpy as np

arr = np.array([20, 30, 10, 80, 70, 40, 50, 90, 60,])

# NumPy array
print("NumPy Array: ", arr)
print("Data type of the Array: ", type(arr))
print("Shape of Array: ", arr.shape)

# Indexing
print("\nIndexing: ", arr[-1], arr[3], arr[5]+arr[3])

# Slicing
print("\nSlicing: ", arr[4:], arr[:5], arr[::-5])

# Reshaping Array

newarr = arr.reshape(3, 3)
print("\n1-D to 2-D Array:",newarr)

arr2 = np.array([[10, 20, 30], [40, 50, 60]])
print("\n2-D Array",arr2)
print("Shape of 2-D array", arr2.shape)

newarr2 = arr.reshape(-1)
print("\n2-D to 1-D Array:", newarr2)

# Iterating
arr3 = np.array([[10, 20, 30], [40, 50, 60]])

for x in arr3:
  print("\nIteration:", x)







