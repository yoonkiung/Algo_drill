import sys

input = sys.stdin.readline

n = int(input().strip())

array = []
for i in range(n):
    array.append(int(input().strip()))

if (n == 1 or n == 2):
    print(sum(array))
    exit()
d = [0 for _ in range(n)]

d[0] = array[0]
d[1] = array[0] + array[1]
d[2] = max(array[0] + array[2], array[1] + array[2])
for i in range(3, n):
    d[i] = max(d[i - 3] + array[i - 1] + array[i], d[i - 2] + array[i])

print(d[n - 1])