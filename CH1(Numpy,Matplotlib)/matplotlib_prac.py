import numpy as np
# matplotlib은 그래프 그리기, 데이터 시각화에 유용한 라이브러리
import matplotlib.pyplot as plt

# y=sin(x) 함수 그리기
x = np.arange(0, 6, 0.1)    # [0, 0.1, 0.2, ... , 5.8, 5.9]
y = np.sin(x)
plt.plot(x, y)
plt.show()

# 그래프 각 축의 이름, 레이블, 그래프 제목 표시
z = np.arange(0, 6, 0.1)
y1 = np.sin(z)
y2 = np.cos(z)

plt.plot(z, y1, label="sin")
plt.plot(z, y2, label="cos")
plt.xlabel("z")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()

# 이미지 표시하기
from matplotlib.image import imread

img = imread('dog.png') # 적절한 경로 설정해서 넣어주기
plt.imshow(img)
plt.show()



