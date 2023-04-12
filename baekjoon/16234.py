import sys
from collections import deque
import copy

input = sys.stdin.readline

n, l, r = list(map(int, input().strip().split()))

array = []
init_visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    array.append(list(map(int, input().strip().split())))

def change_arr(share, value):
    for element in share:
        array[element[0]][element[1]] = value

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    share = []
    sum = 0
    count = 0
    while (queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or ny < 0 or nx >= n or ny >= n):
                continue
            if (visited[nx][ny] == True):
                continue
            gap = abs(array[nx][ny] - array[x][y])
            if (gap >= l and gap <= r):
                share.append((nx, ny))
                visited[nx][ny] = True
                sum += array[nx][ny]
                count += 1
                queue.append((nx, ny))
    if (count != 0):
        change_arr(share, sum // count)
        return True
    return False

def each_day():
    day = 0
    while (1):
        visited = copy.deepcopy(init_visited)
        flag = False
        for i in range(n):
            for j in range(n):
                if (visited[i][j] == False):
                    temp_flag = bfs(i, j, visited)
                    if (temp_flag):
                        flag = True
        if (not flag):
            return (day)
        day += 1

print(each_day())