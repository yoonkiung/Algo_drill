import sys

input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split()))

for i in range(1, n):
    a[i] = max(a[i], a[i - 1] + a[i])

print(max(a))