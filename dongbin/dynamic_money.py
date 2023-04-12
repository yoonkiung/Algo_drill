import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
array = []
inf = 100000000000
d = [inf] * (10001)


for i in range(n):
    array.append(int(input()))

for element in array:
    d[element] = 1

for i in range(1, m + 1):
    for element in array:
        if (d[i - element] != inf):
            d[i] = min(d[i], d[i - element] + 1)

if (d[m] == inf):
    print(-1)
else:
    print(d[m])