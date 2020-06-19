import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))   # np.log()함수에 0을 입력하면 -inf되므로 아주작은 수인 delta를 더해줌

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# 예시 1: 3번째 클래스일 확률이 가장 높다고 추측
y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(cross_entropy_error(np.array(y1), np.array(t)))   # 0.5108...

# 예시 2: 8번째 클래스일 확률이 가장 높다고 추측
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(cross_entropy_error(np.array(y2), np.array(t)))   # 2.3025...

