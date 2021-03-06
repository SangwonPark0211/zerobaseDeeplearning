import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)    # (60000, 784)
print(t_train.shape)    # (60000, 10)

train_size = x_train.shape[0]
batch_size = 10
# train_size미만의 수 중 batch_size만큼을 랜던하게 선택해 ndarray로 출력
batch_mask = np.random.choice(train_size, batch_size)
print(batch_mask) 
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]