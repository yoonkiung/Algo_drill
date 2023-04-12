import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input().strip())

array = []
for i in range(n):
    array.append(list(map(int, input().strip().split())))

d = [[0 for _ in range(n)] for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if (d[i][j] == 0 or (i == n - 1 and j == n - 1)):
            continue
        
        dx = [array[i][j], 0]
        dy = [0, array[i][j]]
        
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]

            if (nx < n and ny < n):
                d[nx][ny] += d[i][j]

print(d[n - 1][n - 1])