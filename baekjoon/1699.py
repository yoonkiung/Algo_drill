import sys

input = sys.stdin.readline

n = int(input().strip())

d = [0, 1, 2, 3] + [100001 for _ in range(4, n + 1)]

for i in range(4, n + 1):
    for j in range(1, i):
        if (j * j == i):
            d[i] = 1
            break
        if (i - j * j < 0):
            break
        d[i] = min(d[i], d[i - j * j] + 1)
        
print(d[n])
