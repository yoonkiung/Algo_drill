import sys
input = sys.stdin.readline

n = int(input().strip())
array = []
for i in range(n):
    array.append(list(map(int, input().strip().split())))

array.sort(key = lambda x:x[0])

d = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if (array[j][1] < array[i][1]):
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))