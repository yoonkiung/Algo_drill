import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))

board = []
vir_pos = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if (temp[j] == 2):
            vir_pos.append((i, j))
    board.append(temp)

com_list = list(combinations(vir_pos, m))

def is_all(table):
    for i in range(n):
        for j in range(n):
            if (table[i][j] == 0):
                return (False)
    return (True)

def bfs(table, com):
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    for c in com:
        queue.append(list(c) + [0])
        visited[c[0]][c[1]] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cur_depth = 0

    while (queue):
        x, y, depth = queue.popleft()
        visited[x][y] = True
        if (table[x][y] != 2):
            cur_depth = depth
        table[x][y] = -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or nx >= n or ny < 0 or ny >= n \
                or visited[nx][ny] == True \
                or table[nx][ny] == 1):
                continue
            queue.append([nx, ny, depth + 1])
            visited[nx][ny] = True
    if (is_all(table)):
        return (cur_depth)
    return (101)

ans = 1000000
for c in com_list:
    ans = min(ans, bfs(copy.deepcopy(board), c))
if (ans == 101):
    print(-1)
else:
    print(ans)