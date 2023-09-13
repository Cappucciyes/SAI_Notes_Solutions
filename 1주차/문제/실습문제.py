numChart = list(range(51))
primeChart = [True] * 51

primeChart[0], primeChart[1] = False, False

for i in range(2, 51):
    if not primeChart[i]:
        continue

    for j in range(i * 2, 51, i):
        if j >= 51:
            break
        primeChart[j] = False

n, m = input().split(' ')
count = 0
for index in range(int(n), int(m) + 1):
    if primeChart[index]:
        print(index)
        count += 1

print(count)
