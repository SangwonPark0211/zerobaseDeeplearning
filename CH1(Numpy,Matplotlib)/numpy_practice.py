import numpy as np

# np.array() 실습
X = np.array([1.0, 2.0, 3.0])
print(X)    # [1. 2. 3.]
print(type(X))  # <class 'numpy.ndarray'>

# Numpy 산술연산 실습
# 행렬의 형상(N차원 행렬에서 각 차원의 크기)이 같아야만 연산가능
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x+y)  # [3. 6. 9.]
print(x*y)  # [2. 8. 18.]
print(x/2.0)    # [0.5 1. 1.5]

# N차원 배열 생성 실습
A = np.array([[1,2],[3,4]])
print(A)
print(A.shape)  #(2,2)
print(A.dtype)  #int32
B = np.array([[3,0],[0,6]])
print(A+B)  #[[4 2], [3 10]]
print(A*B)  # [[3 0], [0 24]]

# 브로드캐스트 실습
# 행렬과 스칼라 연산
print(A*10) #[[10 20], [30 40]]

# 원소 접근
Y = np.array([[51, 55], [14, 19], [0, 4]])
print(Y[0]) # [51 55]
print(Y[0][1])  # 55
for row in Y:
    print(row)

# Numpy만의 특이한 원소 접근법(인덱스를 배열로 지정해 여러 개 접근)
Y = Y.flatten() # 1차원 배열로 평탄화 [51 55 14 19 0 4]
print(Y[[0,2,4]])   # 인덱스가 0,2,4인 원소에 접근
print(Y>15) # [True True False True False False]
print(Y[Y>15])





