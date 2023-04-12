import sys

input = sys.stdin.readline
n = int(input().strip())


d = [0 for _ in range(n + 1)]
if (n % 2 == 1):
    print(0)
else:
    d[2] = 3
    for i in range(4, n + 1, 2):
        for j in range(0, i, 2):
            d[i] += d[j] + d[i - j]
        d[i] += 1
    print(d[-1])