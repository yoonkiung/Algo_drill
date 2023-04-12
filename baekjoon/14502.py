import sys
from collections import deque
from itertools import combinations
import copy

def count_safe(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            if (array[i][j] == 0):
                count += 1
    return (count)

def bfs(array, queue, n, m):
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
                array[nx][ny] = 2
                queue.append((nx, ny))
    return (count_safe(array))

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

array = []
for i in range(n):
    array.append(list(map(int, input().strip().split())))

walls = []
queue = deque()

for i in range(n):
    for j in range(m):
        if (array[i][j] == 0):
            walls.append((i, j))
        if (array[i][j] == 2):
            queue.append((i, j))

max = -1
combi = list(combinations(walls, 3))

for comb in combi:
    cpy_arr = copy.deepcopy(array)
    for ele in comb:
        cpy_arr[ele[0]][ele[1]] = 1
    temp = bfs(cpy_arr, queue.copy(), n, m)
    if (temp > max):
        max = temp

print(max)