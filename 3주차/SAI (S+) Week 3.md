Course Name:: [[SAI (S+) Curriculum]]
Date:: 2023/9/26 19:44
Tags:: #course_notes

---

# N차원 배열 정렬

- `numpy.sort(arr, axis=-1)`: `arr`의 각 행의 원소를 정렬 후 각 행을 정렬한 새로운 배열 반환 (기본적으로 오름차순으로 정렬)
  - `axis`에 전달 된 축을 기준으로 정렬 됨
  - `axis = None`인 경우, 배열을 1차원으로 뭉개고 배열함.
- `ndarray.sort()`: ndarray에 있는 메소드로 파이썬의 `list.sort()`와 비슷함.
- `numpy.argsort(arr, axis=-1)`: `numpy.sort(arr, axis=-1)`와 똑같이 정렬함. 하지만 정렬된 배열을 반환하는 대신 각 원소 자리에 정렬된 원소의 원래 인덱스를 저장한 배열을 반환함.

# 배열의 행태 변경

- 차원의 저주: 현제의 데이터(배열)의 차원을 늘릴때 생기는 문제로, 차원이 늘어나면서 각 데이터의 거리가 늘어나면서 딥러닝이나 빅데이터를 다룰때 효율이 떨어지는 현상.
- `ndarry.reshape(shape)`
- `numpy.expand_dims(arr, axis)`: `arr`이란 배열에 `axis`에 전달된 축을 기준으로 1 차원 추가된 배열을 반환.
- `numpy.squeeze(arr, axis)`: `arr`이란 배열에 `axis`에 전달된 축을 기준으로 1 차원 제거 된 배열을 반환. 만일 `axis` 값을 전달 안했다면 (`squeeze(arr)`) 기본값으로 1차원 배열로 축소 시킴.

# 전치행열

- `ndarry.T`: `ndarray` 어트리뷰트로 배열의 전치행열이 어떻게 보일지 보여줌. 원래 배열은 안 바뀜.

# 배열 병합

### 배열에 원소 추가 및 삭제

- `numpy.insert(arr, where, value, axis=None)`: 넘파이 함수로, `arr` 배열에 `axis`축 기준 `where`위치에 `value`를 집어 넣음. `axis=None`일 때 일단 배열을 1차원으로 만들고 시작함. 새로운 배열 반환
  - 1차원 예시 `numpy.insert(arr, 12, 2)` ==> 파이썬 `list.insert()` 처럼 1차원 배열에 12 인덱스 위치에 2를 집어넣음. 이때 1차원이기에 `axis` 값이 None이여도 상관 x
  - 2차원 예시 `numpy.insert(arr, 12, 2, 1)`: `arr`배열에 1번 축 기준으로 12 인덱스에 있는 열에 2로 채운 새로운 열을 추가. 이때, `value` 자리에 알맞는 길이의 열백터였으면 열벡터 그대로 들어감.
- `numpy.delete(arr, where, axis=None)`: 넘파이 함수로, `arr` 배열에 `axis`축 기준 `where`위치에 있는 축을 지움. `axis=None`일 때 일단 배열을 1차원으로 만들고 시작함. 새로운 배열 반환.

`numpy.delete` 예시

```
import numpy as np

arr = np.arange(1,10).reshape([3,3])
print("delete 전\n", arr)

newArr = np.delete(arr, 1,1)
print("delete 이후\n",newArr)

# 출력
# delete 전
# [[1 2 3]
# [4 5 6]
# [7 8 9]]
# delete 이후
# [[1 3]
# [4 6]
# [7 9]]
```

# 배열간 병합

- `numpy.append(arr1, arr2, axis=None)`: `axis`축 방향으로 `arr1`에 `arr2`를 추가 시킴.
- `numpy.vstack([arr1, arr2,...])`: 여러개의 같은 shape의 배열을 첫번째 축 기준으로 이어 붙임.

```
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a,b)))

# 출력
# [[1 2 3]
#  [4 5 6]]
```

- `numpy.hstack([arr1, arr2,...])`: 여러개의 같은 shape의 배열을 두번째 축 기준으로 이어 붙임.

```
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.hstack((a,b)))

# 출력
# [1 2 3 4 5 6]
```

- `numpy.concatenate([arr1, arr2, arr3,...], axis=0)`: 여러 배열(`arr1, arr2, arr3 ...`)을 `axis`축 방향으로 하나의 배열로 이어줌. `axis`기본값은 0.

# 배열 분할

- `numpy.vsplit(arr, n)`: `numpy.vstack` 의 정 반대로, arr을 첫번째 축을 기준으로 n개의 배열로 나눔. 못 나누명 에러가 뜸.
- `numpy.hsplit(arr, n): numpy.hstack` 의 정 반대로, arr을 두번째 축을 기준으로 n개의 배열로 나눔. 못 나누면 에러가 뜸.

---

My Questions::
Related Concepts::
See also::
