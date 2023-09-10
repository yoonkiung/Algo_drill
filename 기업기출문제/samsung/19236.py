import copy

board = [[0 for _ in range(4)] for _ in range(4)]
info_fish = [0] * 17

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        num, d = temp[j], temp[j + 1]
        x = i
        y = j // 2
        board[x][y] = num
        info_fish[num] = [x, y, d]

def swap_table(plane, x1, y1, x2, y2):
    temp = plane[x1][y1]
    plane[x1][y1] = plane[x2][y2]
    plane[x2][y2] = temp

def swap_fish(table, fish, x, y, nx, ny):
    x1 = table[x][y]
    x2 = table[nx][ny]
    if (fish[x1] != 0 and fish[x2] != 0):
        d_x1 = fish[x1][2]
        d_x2 = fish[x2][2]
        temp = fish[x1]
        fish[x1] = fish[x2]
        fish[x2] = temp
        fish[x1][2] = d_x1
        fish[x2][2] = d_x2
    elif (fish[x1] == 0):
        fish[x2][0] = x
        fish[x2][1] = y
    elif (fish[x2] == 0):
        fish[x1][0] = nx
        fish[x1][1] = ny

def find_dir(d):
    if (d == 1):
        return ([-1, 0])
    if (d == 2):
        return ([-1, -1])
    if (d == 3):
        return ([0, -1])
    if (d == 4):
        return ([1, -1])
    if (d == 5):
        return ([1, 0])
    if (d == 6):
        return ([1, 1])
    if (d == 7):
        return ([0, 1])
    if (d == 8):
        return ([-1, 1])

def change_dir(d):
    if (d <= 7):
        return (d + 1)
    if (d == 8):
        return (1)

def move_fish(table, fish, shark_x, shark_y):
    for i in range(1, 17):
        if (fish[i] == 0):
            continue
        x, y, d = fish[i]
        dx, dy = find_dir(d)
        nx = x + dx
        ny = y + dy
        for _ in range(7):
            if (nx < 0 or nx >= 4 or ny < 0 or ny >= 4 \
                or (nx == shark_x and ny == shark_y)):
                d = change_dir(d)
                fish[i][2] = d
                dx, dy = find_dir(d)
                nx = x + dx
                ny = y + dy
                continue
            break
        swap_fish(table, fish, x, y, nx, ny)
        swap_table(table, x, y, nx, ny)
        

max_value = 0
def dfs(point, x, y, table, fish):
    global max_value
    c_table = copy.deepcopy(table)
    c_fish = copy.deepcopy(fish)
    num = c_table[x][y]
    max_value = max(max_value, point + num)
    c_table[x][y] = 0
    delta = find_dir(c_fish[num][2])
    c_fish[num] = 0
    move_fish(c_table, c_fish, x, y)
    for _ in range(4):
        nx = x + delta[0]
        ny = y + delta[1]
        if (nx < 0 or nx >= 4 or ny < 0 or ny >= 4):
            break
        if (c_table[nx][ny] == 0):
            x = nx
            y = ny

            continue
        dfs(point + num, nx, ny, c_table, c_fish)
        x = nx
        y = ny

dfs(0, 0, 0, board, info_fish)
print(max_value)