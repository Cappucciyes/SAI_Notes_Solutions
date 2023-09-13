def primeList(start, end):
    global numChart
    global primeChart
    
    numChart = list(range(end+1))
    primeChart = [True] * (end + 1)

    primeChart[0], primeChart[1] = False, False

    for i in range(start, end + 1):
        if not primeChart[i]:
            continue

        for j in range(i * 2, end + 1, i):
            if j >= (end + 1):
                break
            primeChart[j] = False


n, m = (int(x) for x in input().split(' '))
primeList(n, m)
count = 0

for index in range(int(n), int(m) + 1):
    if primeChart[index]:
        print(index)
        count += 1

print(count)
