import sys

input = sys.stdin.readline

def is_wall(x, y):
    if (x < 0 or x >= n or y < 0 or y >= m):
        return (True)
    if (board[x][y] == 1):
        return (True)
    return (False)

def is_empty_space(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx < 0 or nx >= n or ny < 0 or ny >= m):
            continue
        if (board[nx][ny] == 0):
            return (True)
    return (False)

def reverse_dir(dir):
    if (dir == 0):
        return (2)
    elif (dir == 1):
        return (3)
    elif (dir == 2):
        return (0)
    else:
        return (1)

def find_dir(dir):
    if (dir == 0):
        return ([-1, 0])
    elif (dir == 1):
        return ([0, 1])
    elif (dir == 2):
        return ([1, 0])
    else:
        return ([0, -1])

def rotate_dir(dir):
    if (dir == 0):
        return (3)
    elif (dir == 1):
        return (0)
    elif (dir == 2):
        return (1)
    else:
        return (2)

def is_clean(x, y):
    if (board[x][y] == 0):
        return (True)
    return (False)


n, m = list(map(int, input().strip().split()))

x, y, d = list(map(int, input().strip().split()))

board = []
for i in range(n):
    board.append(list(map(int, input().strip().split())))

count = 0

while (True):
    if (board[x][y] == 0):
        board[x][y] = 2
        count += 1
    if (not is_empty_space(x, y)):
        rev_dir = find_dir(reverse_dir(d))
        nx = x + rev_dir[0]
        ny = y + rev_dir[1]
        if (is_wall(nx, ny)):
            break
        else:
            x, y = nx, ny
    else:
        for i in range(3):
            d = rotate_dir(d)
            next_dir = find_dir(d)
            nx = x + next_dir[0]
            ny = y + next_dir[1]
            if (is_wall(nx, ny) == False and is_clean(nx, ny)):
                x, y = nx, ny
                break

print(count)
            
        