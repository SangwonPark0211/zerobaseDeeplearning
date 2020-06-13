import numpy as np
import matplotlib.pyplot as plt

# 계단함수 구현
def step_function(x):
    if x>0:
        return 1
    else:
        return 0

# 함수 입력으로 numpy 배열 받을 수 있는 계단함수 구현
def step_function2(x):
    y=x>0
    return y.astype(np.int) # astype : 넘파이 배열의 자료형 변환
x = np.array([-1.0, 1.0, 2.0])
print(step_function2(x))    # [0 1 1]

# 계단함수 그래프 그리기
def draw_step_function(x):
    return np.array(x>0, dtype=np.int)
x = np.arange(-5.0, 5.0, 0.1)
y = draw_step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축 범위 지정
plt.show()



