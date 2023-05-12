import numpy as np
from timeit import Timer
#Add/Subtract/Multiply/Divide by Scalar

# Creating a large array of size 10**6
array = np.random.randint(1000, size=10**6)
 
# method that adds elements using for loop
def add_forloop():
  new_array = [element + 1 for element in array]
 
# method that adds elements using vectorization
def add_vectorized():
  new_array = array + 1
 
# Finding execution time using timeit
execution_time_forloop = Timer(add_forloop).timeit(1)
execution_time_vectorized = Timer(add_vectorized).timeit(1)
 
print("Computation time is %0.9f using for-loop"%execution_time_forloop)
print("Computation time is %0.9f using vectorization"%execution_time_vectorized)


#Sum and Max of array

# Creating a large array of size 10**5
array = np.random.randint(1000, size=10**5)

def sum_using_forloop():
  sum_array=0
  for element in array:
    sum_array += element

def sum_using_builtin_method():
  sum_array = sum(array)

def sum_using_numpy():
  sum_array = np.sum(array)

time_forloop = Timer(sum_using_forloop).timeit(1)
time_builtin = Timer(sum_using_builtin_method).timeit(1)
time_numpy = Timer(sum_using_numpy).timeit(1)

print("Summing elements takes %0.9f units using for loop"%time_forloop)
print("Summing elements takes %0.9f units using builtin method"%time_builtin)
print("Summing elements takes %0.9f units using numpy"%time_numpy)

print()

def max_using_forloop():
  maximum=array[0]
  for element in array:
    if element > maximum:
      maximum = element

def max_using_builtin_method():
  maximum = max(array)

def max_using_numpy():
  maximum = np.max(array)

time_forloop = Timer(max_using_forloop).timeit(1)
time_builtin = Timer(max_using_builtin_method).timeit(1)
time_numpy = Timer(max_using_numpy).timeit(1)

print("Finding maximum element takes %0.9f units using for loop"%time_forloop)
print("Finding maximum element takes %0.9f units using built-in method"%time_builtin)
print("Finding maximum element takes %0.9f units using numpy"%time_numpy)

#3. Dot product

# Create 2 vectors of same length
length = 100000
vector1 = np.random.randint(1000, size=length)
vector2 = np.random.randint(1000, size=length)

# Finds dot product of vectors using for loop
def dotproduct_forloop():
  dot = 0.0
  for i in range(length):
    dot += vector1[i] * vector2[i]

# Finds dot product of vectors using numpy vectorization
def dotproduct_vectorize():
  dot = np.dot(vector1, vector2)


# Finding execution time using timeit
time_forloop = Timer(dotproduct_forloop).timeit(1)
time_vectorize = Timer(dotproduct_vectorize).timeit(1)

print("Finding dot product takes %0.9f units using for loop"%time_forloop)
print("Finding dot product takes %0.9f units using vectorization"%time_vectorize)


#4. Outer Product

# Create 2 vectors of same length
length1 = 1000
length2 = 500
vector1 = np.random.randint(1000, size=length1)
vector2 = np.random.randint(1000, size=length2)

# Finds outer product of vectors using for loop
def outerproduct_forloop():
  outer_product = np.zeros((length1, length2), dtype='int')
  for i in range(length1):
    for j in range(length2):
      outer_product[i, j] = vector1[i] * vector2[j]

# Finds outer product of vectors using numpy vectorization
def outerproduct_vectorize():
  outer_product = np.outer(vector1, vector2)

# Finding execution time using timeit
time_forloop = Timer(outerproduct_forloop).timeit(1)
time_vectorize = Timer(outerproduct_vectorize).timeit(1)

print("Finding outer product takes %0.9f units using for loop"%time_forloop)
print("Finding outer product takes %0.9f units using vectorization"%time_vectorize)

#5 Matrix Multiplication

# Create 2 vectors of same length
n = 100
k = 50
m = 70
matrix1 = np.random.randint(1000, size=(n, k))
matrix2 = np.random.randint(1000, size=(k, m))

# Multiply 2 matrices using for loop
def matrixmultiply_forloop():
  product = np.zeros((n, m), dtype='int')
  for i in range(n):
    for j in range(m):
      for z in range(k):
        product[i, j] += matrix1[i, z] * matrix2[z, j]

# Multiply 2 matrices using numpy vectorization
def matrixmultiply_vectorize():
  product = np.matmul(matrix1, matrix2)

# Finding execution time using timeit
time_forloop = Timer(matrixmultiply_forloop).timeit(1)
time_vectorize = Timer(matrixmultiply_vectorize).timeit(1)

print("Multiplying matrices takes %0.9f units using for loop"%time_forloop)
print("Multiplying matrices takes %0.9f units using vectorization"%time_vectorize)

#6. Element Wise Product in Matrix
# Create 2 vectors of same length
n = 500
m = 700
matrix1 = np.random.randint(1000, size=(n, m))
matrix2 = np.random.randint(1000, size=(n, m))

# Multiply 2 matrices using for loop
def multiplication_forloop():
  product = np.zeros((n, m), dtype='int')
  for i in range(n):
    for j in range(m):
      product[i, j] = matrix1[i, j] * matrix2[i, j]

# Multiply 2 matrices using numpy vectorization
def multiplication_vectorize():
  product = matrix1 * matrix2

# Finding execution time using timeit
time_forloop = Timer(multiplication_forloop).timeit(1)
time_vectorize = Timer(multiplication_vectorize).timeit(1)

print("Element Wise Multiplication takes %0.9f units using for loop"%time_forloop)
print("Element Wise Multiplication takes %0.9f units using vectorization"%time_vectorize)

