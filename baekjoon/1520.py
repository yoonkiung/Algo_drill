import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def dfs(x, y):
    if (x == m - 1 and y == n - 1):
        return (1)
    
    if (d[x][y] != -1):
        return (d[x][y])
    
    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < m and 0 <= ny < n and array[x][y] > array[nx][ny]):
            ways += dfs(nx, ny)
    
    d[x][y] = ways
    return d[x][y]

m, n = list(map(int, input().strip().split()))

array = []
for i in range(m):
    array.append(list(map(int, input().strip().split())))


d = [[-1] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(dfs(0, 0))
