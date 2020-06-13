import sys, os
import pickle
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from sigmoid import sigmoid
from softmax import softmax2
import numpy as np

# 처음 한 번은 몇 분 정도 걸립니다.
# normalize 옵션은 0~255의 픽셀값을 0.0~1.0 사이의 값으로 정규화
# flatten 옵션은 1차원 배열로 만드는 것
# one_hot_label 옵션은 정답을 뜻하는 원소만 1인 배열로 만드는 것(False인 경우 '7'과 같이 숫자로 저장)
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=True, one_hot_label=False)

    # 각 데이터의 형상 출력
    print(x_train.shape)    # (60000, 784)
    print(t_train.shape)    # (60000,)
    print(x_test.shape)     # (10000, 784)
    print(t_test.shape)     # (10000,)

    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax2(a3) 

    return y

# x, t = get_data()
# network = init_network()

# accuracy_cnt = 0
# for i in range(len(x)):
#     y = predict(network, x[i])
#     p = np.argmax(y) # 확률(y값)이 가장 높은 원소의 인덱스를 얻는다.
#     if p == t[i]:
#         accuracy_cnt += 1

# print("Accuracy:", str(float(accuracy_cnt/len(x))))

# 배치처리 도입
x, t = get_data()
network = init_network()

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:", str(float(accuracy_cnt/len(x))))


