import sys
from collections import deque

input = sys.stdin.readline

def change_delta(dir, delta):
    if (dir == "L"):
        if (delta[0] == 0 and delta[1] == 1):
            return ([-1, 0])
        if (delta[0] == 1 and delta[1] == 0):
            return ([0, 1])
        if (delta[0] == 0 and delta[1] == -1):
            return ([1, 0])
        if (delta[0] == -1 and delta[1] == 0):
            return ([0, -1])
    if (dir == "D"):
        if (delta[0] == 0 and delta[1] == 1):
            return ([1, 0])
        if (delta[0] == 1 and delta[1] == 0):
            return ([0, -1])
        if (delta[0] == 0 and delta[1] == -1):
            return ([-1, 0])
        if (delta[0] == -1 and delta[1] == 0):
            return ([0, 1])

n = int(input().strip())
k = int(input().strip())

board = [[0 for _ in range(n)] for _ in range(n)]
board[0][0] = 1

for i in range(k):
    a, b = list(map(int, input().strip().split()))
    board[a -1][b - 1] = 2


l = int(input().strip())
chdir = {}
for i in range(l):
    a, b = list(input().strip().split())
    chdir[int(a)] = b

x, y = 0 ,0
delta = [0, 1]
time = 0
queue = deque()
queue.append((x, y))

while (1):

    # new location
    t_x, t_y = queue[0]
    nx, ny = queue[-1]
    nx += delta[0]
    ny += delta[1]

    if (nx < 0 or nx >= n):
        break
    if (ny < 0 or ny >= n):
        break
    if (board[nx][ny] == 1):
        break
    if (board[nx][ny] == 2):
        queue.append((nx, ny))
    if (board[nx][ny] == 0):
        queue.append((nx, ny))
        queue.popleft()
        board[t_x][t_y] = 0
    board[nx][ny] = 1
    time += 1
    if (time in chdir):
        delta = change_delta(chdir[time], delta)

print(time + 1)