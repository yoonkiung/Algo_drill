import sys

n = int(sys.stdin.readline())

array_a = list(map(int, sys.stdin.readline().split()))
array_b = list(map(int, sys.stdin.readline().split()))

array_a.sort()
array_b.sort(reverse=True)

result = 0

for i in range(n):
    result += array_a[i] * array_b[i]

print(result)
