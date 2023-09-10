import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

board = []
shark = []
for i in range(n):
    flag = False
    temp = list(map(int, input().strip().split()))
    board.append(temp)
    if (not flag):
        for j in range(n):
            if (temp[j] == 9):
                shark = [i, j]
                flag = True
                break

def cal_path(x1, y1, x2, y2):
    return (abs(x1 - x2) + abs(y1 - y2))

def bfs(x, y, shark_body):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((x, y, 0))
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    fishs = []
    min_value = 401
    while (queue):
        mx, my, depth = queue.popleft()
        visited[mx][my] = True
        if (1 <= board[mx][my] <= 6 and board[mx][my] < shark_body):
            if (min_value == 401):
                fishs.append((mx, my, depth))
                min_value = min(min_value, depth)
            else:
                if (depth > min_value):
                    fishs.sort(key = lambda x : (x[0], x[1]))
                    board[x][y] = 0
                    board[fishs[0][0]][fishs[0][1]] = 9
                    return (fishs[0][2], [fishs[0][0], fishs[0][1]])
                elif (depth == min_value):
                    fishs.append((mx, my, depth))
                
        for i in range(4):
            nx = mx + dx[i]
            ny = my + dy[i]

            if (nx < 0 or nx >= n or ny < 0 or ny >= n \
                or visited[nx][ny] == True \
                or board[nx][ny] > shark_body):
                continue
            queue.append((nx, ny, depth + 1))
            visited[nx][ny] = True
    if (len(fishs) > 0):
        fishs.sort(key = lambda z : (z[0], z[1]))
        board[x][y] = 0
        board[fishs[0][0]][fishs[0][1]] = 9
        return (fishs[0][2], [fishs[0][0], fishs[0][1]])
    return (False, False)

eat_count = 0
second = 0
shark_body = 2
while (True):
    count, next_pos = bfs(shark[0], shark[1], shark_body)
    if (not next_pos):
        print(second)
        break
    shark = next_pos
    eat_count += 1
    second += count
    
    if (eat_count == shark_body):
        shark_body += 1
        eat_count = 0