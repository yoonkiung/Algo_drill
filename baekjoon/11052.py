import sys

input = sys.stdin.readline

n = int(input().strip())
array = list(map(int, input().strip().split()))
array = [0] + array
d = [0] * (n + 1)

d[1] = array[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], array[j] + d[i - j])

print(d[n])
