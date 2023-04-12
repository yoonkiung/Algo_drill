import sys

input = sys.stdin.readline

n = int(input().strip())

d = [0, 1, 3, 5]

if (n < 3):
    print(d[n])
else:
    for i in range(4, n + 1):
        d.append(d[i - 1] + d[i - 2] * 2)
    print(d[n] % 10007)