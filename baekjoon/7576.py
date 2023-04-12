import sys
from collections import deque

input = sys.stdin.readline

m, n = list(map(int, input().strip().split()))

array = []
for i in range(n):
    array.append(list(map(int, input().strip().split())))

def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if (array[i][j] == 1):
                queue.append((i, j))
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while (queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            if (array[nx][ny] == 0):
                queue.append((nx, ny))
                array[nx][ny] = array[x][y] + 1
    
bfs()
# for i in range(n):
#     print(array[i])
max = -1
for i in range(n):
    for j in range(m):
        if (array[i][j] == 0):
            print(-1)
            exit()
        if (array[i][j] > max):
            max = array[i][j]

print(max - 1)