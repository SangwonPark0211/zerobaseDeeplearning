import numpy as np
import matplotlib.pyplot as plt

# 시그모이드 함수 구현
def sigmoid(x):
    return 1/(1+np.exp(-x))
x1 = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x1))   # [0.26894142 0.73105858 0.88079708]

# 시그모이드 함수 그래프 그리기
x2 = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x2)
plt.plot(x2, y)
plt.ylim(-0.1, 1.1)
plt.show()