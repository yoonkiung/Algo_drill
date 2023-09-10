import sys

input = sys.stdin.readline

n = int(input().strip())
array = list(map(int, input().strip().split()))

d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if (array[j] > array[i]):
            d[i] = max(d[i], d[j] + 1)
print(n - d[n - 1])