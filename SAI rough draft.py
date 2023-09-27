import numpy as np

# 0부터 99까지의 정수를 포함하는 10x10 크기의 배열 생성
data = np.arange(100).reshape(10, 10)
print(data)

# 홀수로 이루어진 행렬
test_array = data[data % 2 == 1].reshape(-1, 10)
print(test_array)

# Boolean indexing을 통해 3의 배수의 원소들 골라 새로운 배열 만듬
timesThree = test_array[test_array % 3 == 0]
print(timesThree)

# 위에서 새로 얻은 배열을 제곱
squaredTimesThree = timesThree ** 2
print(squaredTimesThree)
