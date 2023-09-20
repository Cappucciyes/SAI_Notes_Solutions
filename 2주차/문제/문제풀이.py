import numpy as np
# 0 부터 99 10x10 배열
start = np.array([[x for x in range(y, y + 10)] for y in range(0, 100, 10)])
print(start, "\n")

# fancy indexing을 통해 각 행에 있는 홀수가 있는 열만 골라 새로운 배열 만들기
odd = np.array(start[:, [1, 3, 5, 7, 9]])
print(odd, "\n")

# Boolean indexing을 통해 3의 배수의 원소들 골라 새로운 배열 만듬
timesThree = np.array(odd[odd % 3 == 0])

print(timesThree, "\n")

# 위에서 새로 얻은 배열을 제곱
squaredTimesThree = timesThree ** 2
print(squaredTimesThree)


# # (새로운 배열 % 3으로 채워진 같은 shape 배열)
# # 위에서 얻은 배열과 0으로 채워진 같은 shape 배열을 비교하여 불리안으로 채워진 배열 얻음 (0 이면 True, 아니면 False)
# # 불이안 배열과 odd 배열을 곱하면 3의 배수 외 전부 0
# timesThree = ((odd % np.full_like(odd, 3)) == np.zeros_like(odd)) * odd

# # 0 외 다른 숫자들은 새로운 리스트에 저장
# newThree = []
# for row in timesThree:
#     for i in row:
#         if i == 0:
#             continue
#         else:
#             newThree.append(i)

# # 리스트를 배열로 만들고 출력
# newThree = np.array(newThree)
# print(newThree, "\n")

# # 위에서 새로 얻은 배열을 제곱
# squaredNewThree = newThree ** 2
# print(squaredNewThree)
