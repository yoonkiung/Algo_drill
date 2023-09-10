import sys

input = sys.stdin.readline

r, c, t = list(map(int, input().strip().split()))

board = []
machine = []
flag = False
for i in range(r):
    temp = list(map(int, input().strip().split()))
    board.append(temp)
    if (not flag):
        for j in range(c):
            if (temp[j] == -1):
                machine.append([i, j])
                machine.append([i + 1, j])
                flag = True
                break

def fluent():
    add_list = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(r):
        for j in range(c):
            if (board[i][j] > 0):
                count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if (nx < 0 or nx >= r or ny < 0 or ny >= c \
                        or board[nx][ny] == -1):
                        continue
                    count += 1
                    add_list.append([nx, ny, board[i][j] // 5])
                board[i][j] = board[i][j] - (board[i][j] // 5) * count
    for ele in add_list:
        x, y, amount = ele[0], ele[1], ele[2]
        board[x][y] += amount

def swap(x1, y1, x2, y2):
    temp = board[x1][y1]
    board[x1][y1] = board[x2][y2]
    board[x2][y2] = temp

def blow():
    visited = [[True for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if (i == machine[0][0] or j == machine[0][1] \
                or i == machine[1][0] or j == machine[1][1] \
                or i == 0 or i == r - 1 \
                or j == 0 or j == c - 1):
                visited[i][j] = False
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    t_x, t_y = machine[0][0], machine[0][1]
    
    cnt_x, cnt_y = t_x, t_y
    next_x, next_y = 0, 0
    while (True):
        for i in range(4):
            nx = cnt_x + dx[i]
            ny = cnt_y + dy[i]
            
            if (nx < 0 or nx >= r or ny < 0 or ny >= c \
                or visited[nx][ny] == True):
                continue
            next_x, next_y = nx, ny
            break
        visited[next_x][next_y] = True
        swap(cnt_x, cnt_y, next_x, next_y)
        if (next_x == t_x and next_y == t_y):
            board[cnt_x][cnt_y] = 0
            break
        else:
            cnt_x, cnt_y = next_x, next_y

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    t_x, t_y = machine[1][0], machine[1][1]

    cnt_x, cnt_y = t_x, t_y
    next_x, next_y = 0, 0
    while (True):
        for i in range(4):
            nx = cnt_x + dx[i]
            ny = cnt_y + dy[i]
            
            if (nx < 0 or nx >= r or ny < 0 or ny >= c \
                or visited[nx][ny] == True):
                continue
            next_x, next_y = nx, ny
            break
        visited[next_x][next_y] = True
        swap(cnt_x, cnt_y, next_x, next_y)
        if (next_x == t_x and next_y == t_y):
            board[cnt_x][cnt_y] = 0
            break
        else:
            cnt_x, cnt_y = next_x, next_y

    
for _ in range(t):
    fluent()
    blow()

answer = 0
for ele in board:
    answer += sum(ele)
print(answer + 2)