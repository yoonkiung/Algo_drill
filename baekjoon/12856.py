import sys

input = sys.stdin.readline

n, k = list(map(int, input().strip().split()))

value = [0]
weight = [0]

for i in range(n):
    temp = list(map(int, input().strip().split()))
    weight.append(temp[0])
    value.append(temp[1])

array = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(k + 1):
        if (j < weight[i]):
            array[i][j] = array[i - 1][j]
        else:
            array[i][j] = max(array[i - 1][j], array[i - 1][j - weight[i]] + value[i])

print(array[n][k])