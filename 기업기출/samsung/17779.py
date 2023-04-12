import sys

W = 0
R = 1
B = 2

input = sys.stdin.readline

n, k= list(map(int, input().split()))

color_board = []
for i in range(n):
    color_board.append(list(map(int, input().split())))

pos_board = [[[] for _ in range(n)] for _ in range(n)]
pos = []
for i in range(k):
    a, b, d = list(map(int, input().split()))
    pos.append([a - 1, b - 1, d])
    pos_board[a - 1][b - 1].append(i)

def find_dir(d):
    if (d == 1):
        return ([0, 1])
    elif (d == 2):
        return ([0, -1])
    elif (d == 3):
        return ([-1, 0])
    else:
        return ([1, 0])

def change_dir(d):
    if (d == 1):
        return (2)
    elif (d == 2):
        return (1)
    elif (d == 3):
        return (4)
    else:
        return (3)

def move(num):
    x, y, d = pos[num]

    delta = find_dir(d)
    nx = x + delta[0]
    ny = y + delta[1]

    if (nx < 0 or nx >= n or ny < 0 or ny >= n \
        or color_board[nx][ny] == B):
        d = change_dir(d)
        delta = find_dir(d)
        pos[num][2] = d
        nx = x + delta[0]
        ny = y + delta[1]

        if (nx < 0 or nx >= n or ny < 0 or ny >= n \
        or color_board[nx][ny] == B):
            return

    if (color_board[nx][ny] == W):
        remain_pos = 0
        for j in range(len(pos_board[x][y])):
            if (pos_board[x][y][j] == num):
                remain_pos = j
        
        for index in pos_board[x][y][remain_pos:]:
            pos[index] = [nx, ny, pos[index][2]]
        
        pos_board[nx][ny] = pos_board[nx][ny] + pos_board[x][y][remain_pos:]
        pos_board[x][y] = pos_board[x][y][:remain_pos]

        if (len(pos_board[nx][ny]) >= 4):
            print(count)
            exit()
    
    elif (color_board[nx][ny] == R):
        remain_pos = 0
        for j in range(len(pos_board[x][y])):
            if (pos_board[x][y][j] == num):
                remain_pos = j
        
        for index in pos_board[x][y][remain_pos:]:
            pos[index] = [nx, ny, pos[index][2]]

        if (remain_pos == 0):
            pos_board[nx][ny] = pos_board[nx][ny] + pos_board[x][y][len(pos_board[x][y]) - 1::-1]
        else:
            pos_board[nx][ny] = pos_board[nx][ny] + pos_board[x][y][len(pos_board[x][y]) - 1:remain_pos - 1:-1]
        pos_board[x][y] = pos_board[x][y][:remain_pos]

        if (len(pos_board[nx][ny]) >= 4):
            print(count)
            exit()
    

count = 0
while (count < 1000):
    count += 1
    for i in range(k):
        move(i)

print(-1)
