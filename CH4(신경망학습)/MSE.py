import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)


t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# 예시 1: 3번째 클래스일 확률이 가장 높다고 추정함
y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(mean_squared_error(np.array(y1), np.array(t)))   # 0.0975...

# 예시 2: 8번째 클래스일 확률이 가장 높다고 추정함
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(mean_squared_error(np.array(y2), np.array(t)))   # 0.5975....
