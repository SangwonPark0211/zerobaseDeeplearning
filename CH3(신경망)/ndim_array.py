import numpy as np

A = np.array([1,2,3,4])
print(np.ndim(A))   # 1
print(A.shape)  # (4,)
print(A.shape[0])   # 4

B = np.array([[1,2], [3,4], [5,6]])
print(np.ndim(B))   # 2
print(B.shape)  # (3,2)

# 행렬의 곱
C1 = np.array([[1, 2, 3], [4, 5, 6]])
print(C1.shape)  # (2,3)
D1 = np.array([[1, 2], [3, 4], [5, 6]])
print(D1.shape)  # (3,2)
print(np.dot(C1, D1)) # [[22 28] [49 64]]

C2 = np.array([[1,2], [3,4], [5,6]])
print(C2.shape) # (3,2)
D2 = np.array([7,8])
print(D2.shape) # (2,)
print(np.dot(C2, D2))   # [23 53 83]

# 신경망의 행렬곱
X = np.array([1,2])
W = np.array([[1,3,5], [2,4,6]])
Y = np.dot(X,W)
print(Y)    # [5 11 17]
