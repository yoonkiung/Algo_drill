import sys
input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

array = []
for i in range(n):
    array.append(list(map(int, input().strip().split())))

d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        d[i][j] = array[i - 1][j - 1] + max(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])

print(d[n][m])