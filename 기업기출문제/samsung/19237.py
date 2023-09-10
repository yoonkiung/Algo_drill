import copy

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

n, m, k = list(map(int, input().split()))

board = []
shark_info = [0] * (m + 1)
priority = [0] * (m + 1)
shark_dir = [0]

def find_dir(d):
    if (d == 1):
        return ([-1, 0])
    elif (d == 2):
        return ([1, 0])
    elif (d == 3):
        return ([0, -1])
    else:
        return ([0, 1])

def move_shark(time):
    global board
    
    dic_shark = {}
    c_board = copy.deepcopy(board)
    count = 0
    for i in range(1, len(shark_info)):
        if (shark_info[i] == 0):
            continue

        x, y = shark_info[i]
        d = shark_dir[i]

        flag = False
        for j in range(4):
            nd = priority[i][d - 1][j]
            delta = find_dir(nd)
            nx = x + delta[0]
            ny = y + delta[1]
            
            if (nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue

            if (board[nx][ny] == 0):
                if ((nx, ny) in dic_shark):
                    flag = True
                    shark_info[i] = 0
                    count += 1
                    break
                flag = True
                dic_shark[(nx, ny)] = i
                c_board[nx][ny] = [i, time + k]
                shark_info[i] = [nx, ny]
                shark_dir[i] = nd
                break
        if (not flag):
            for j in range(4):
                nd = priority[i][d - 1][j]
                delta = find_dir(nd)
                nx = x + delta[0]
                ny = y + delta[1]
                
                if (nx < 0 or nx >= n or ny < 0 or ny >= n):
                    continue

                if (board[nx][ny] != 0 and board[nx][ny][0] == i):
                    dic_shark[(nx, ny)] = i
                    c_board[nx][ny] = [i, time + k]
                    shark_info[i] = [nx, ny]
                    shark_dir[i] = nd
                    break
    board = c_board
    return (count)

def del_smell(time):
    count = 0
    for i in range(n):
        for j in range(n):
            if (board[i][j] != 0 and board[i][j][1] == time):
                board[i][j] = 0
                count += 1
    return (count)

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if (temp[j] != 0):
            shark_info[temp[j]] = [i, j]
            temp[j] = [temp[j], k]
    board.append(temp)

shark_dir += list(map(int, input().split()))

for i in range(m):
    temp = []
    for j in range(4):
        temp.append(list(map(int, input().split())))
    priority[i + 1] = temp

time = 1
while (True):
    m -= move_shark(time)
    del_smell(time)
    if (m == 1):
        print(time)
        break
    time += 1
    if (time > 1000):
        print(-1)
        break