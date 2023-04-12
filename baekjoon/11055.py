import sys

input = sys.stdin.readline

n = int(input().strip())
array = list(map(int, input().strip().split()))

d = [1] * n
d[0] = array[0]

for i in range(1, n):
    for j in range(0, i):
        if (array[j] < array[i]):
            d[i] = max(d[i], d[j] + array[i])
        else:
            d[i] = max(d[i], array[i])

print(max(d))