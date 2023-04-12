import sys
input = sys.stdin.readline

n, k = list(map(int, input().strip().split()))

array = [0]
for i in range(n):
    array.append(int(input().strip()))
array = list(set(array))
array.sort()
n = len(array)

d = [100001] * (k + 1)
d[0] = 0

for num in array:
    for j in range(num, k + 1):
        d[j] = min(d[j], d[j - num] + 1)
if (d[k] == 100001):
    print(-1)
else:
    print(d[k])