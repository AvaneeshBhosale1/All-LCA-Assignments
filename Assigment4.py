Matrix1 = [
    [1,2,3],
    [4,5,6]
]

Matrix2 = [
    [7,8,9],
    [10,11,12]
]

Result = [
    [0,0,0],
    [0,0,0]
]


for i in range(len(Matrix1)):
     for j in range(len(Matrix1[0])):
          Result[i][j]=Matrix1[i][j]+Matrix2[i][j]

print("Matrix1:")
for row in Matrix1:
    print(row)

print("Matrix2:")
for row in Matrix2:
    print(row)

print("Sum of Matrix1 and Matrix2:")
for row in Result:
    print(row)




#BY NUMPY

import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[9,8,7],[6,5,4],[3,2,1]])

res=a+b
print(res)
