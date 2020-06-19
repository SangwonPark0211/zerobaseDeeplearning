import numpy as np

# f(x0, x1) = x0^2 + x1^2 함수의 구현
def function_2(x):
    return x[0]**2 + x[1]**2

# 편미분을 이용한 기울기 계산
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) # 형상이 x와 같고 모두 0 인 배열

    for idx in range(x.size):
        tmp_val = x[idx]
        
        # f(x+h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad
# function_2 그래프의 (x0,x1) = (3, 4)에서의 기우릭
print(numerical_gradient(function_2, np.array([3.0, 4.0]))) #[6. 8.]

# 경사하강법
# f: 최적화하려는 함수 , x: 초깃값, lr: 학습률, step_num: 경사법에 따른 반복횟수
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr*grad
    return x

print(gradient_descent(function_2, np.array([-3.0, 4.0]), 0.1, 100))    
# [-6.11110793e-10  8.14814391e-10]으로 결과값이 최솟값을 갖는 지점인(0,0)에 가깝게 나온다.

# 학습률이 너무 큰 예 : lr=10.0
print(gradient_descent(function_2, np.array([-3.0, 4.0]), 10.0, 100))
# [-2.58983747e+13 -1.29524862e+12]으로 발산해버림

# 학습률이 너무 작은 예 : lr=1e-10
print(gradient_descent(function_2, np.array([-3.0, 4]), 1e-10, 100))
# [-2.99999994  3.99999992]으로 거의 갱신되지 않고 학습 끝나버림

