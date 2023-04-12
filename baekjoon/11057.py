import sys

input = sys.stdin.readline

n = int(input().strip())

d = [1] * 10

for i in range(1, n):
    for j in range(1, 10):
        d[j] += d[j - 1]

print(sum(d) % 10007)