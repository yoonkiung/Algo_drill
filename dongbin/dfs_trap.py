import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

array = []

for i in range(n):
    temp_arr = list(map(int, input().strip()))
    array.append(temp_arr)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while (queue):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            if (array[nx][ny] == 0):
                continue
            if (array[nx][ny] == 1):
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))
    
    return array[n - 1][m - 1]

print(bfs(0, 0))