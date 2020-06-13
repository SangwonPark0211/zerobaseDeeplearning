import numpy as np
import matplotlib.pyplot as plt

# ReLU 함수 구현
def relu(x):
    return np.maximum(0, x)
x1 = np.array([-1.0, 1.0, 2.0])
print(relu(x1))   # [0. 1. 2.]

# ReLU 함수 그래프 그리기
x2 = np.arange(-5.0, 10.0, 0.1)
y = relu(x2)
plt.plot(x2, y)
plt.ylim(-0.1, 10.0)
plt.show()
