import numpy as np

# 이름, 학번, 성적 들어간 배열 생성
x = np.array(['이지헌', 20011266, 2.1,
              '이승하', 22012312, 3.5,
              '노주호', 22012414, 4.1,
              '사예진', 21032121, 3.1,
              '이준영', 20032132, 3.8,
              '이주호', 19321327, 1.9,
              '노지헌', 21052136, 2.7,
              '이예진', 18032132, 3.8,
              '노승하', 23164723, 0.8,
              '사준영', 19357213, 4.5]).astype(str).reshape(-1, 3)

# F학점을 받은 학생의 인덱스를 리스트로 구함.
f = list()
for row in range(x.shape[0]):
    if float(x[row][2]) < 2.0:
        f.append(row)

# F학점을 받은 학생의 인덱스를 통해 해당 학생 지움
noF = np.delete(x, f, axis=0)

# argsort()를 활용해 성적순으로 나열했을 때 (오름차순) 새로운 배열의 행이 원래 행의 인덱스가 몇이였는지 알아냄
byGradeIndices = np.argsort(noF, axis=0)

# byGradeIndices을 통해 얻은 재배열 순서로 noF 재배열
tmp = [noF[byGradeIndices[i][2]] for i in range(noF.shape[0])]
byGradeArray = np.array(tmp)[::-1]  # 저장된 배열의 행을 역방향으로 재배열 해 성적이 내림차순으로 보이게 바꿈

print(byGradeArray)

# A 학생, B 학생, C 학생이 각각 2명, 4명, 2명 있으므로 일단 byGradeArray를 4개의 배열로 나누고, 나눠서 얻은 2,3번째 배열을 합해 B 학생을 표현할 수 있다.
a, b1, b2, c = np.vsplit(byGradeArray, 4)
print(a)
print(np.vstack((b1, b2)))
print(c)
