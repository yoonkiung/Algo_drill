n, m, k = list(map(int, input().split()))

ball_info = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    temp = list(map(int, input().split()))
    x, y = temp[0] - 1, temp[1] - 1
    temp[0] -= 1
    temp[1] -= 1
    ball_info[x][y].append(temp)

def find_delta(d):
    if (d == 0):
        return ([-1, 0])
    elif (d == 1):
        return ([-1, 1])
    elif (d == 2):
        return ([0, 1])
    elif (d == 3):
        return ([1, 1])
    elif (d == 4):
        return ([1, 0])
    elif (d == 5):
        return ([1, -1])
    elif (d == 6):
        return ([0, -1])
    elif (d == 7):
        return ([-1, -1])

def move_ball():
    global ball_info
    c_ball_info = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (len(ball_info[i][j]) == 0):
                continue
            for k in range(len(ball_info[i][j])):
                x, y, m, s, d = ball_info[i][j][k]
                delta = find_delta(d)
                x += (s % n) * delta[0]
                y += (s % n) * delta[1]
                if (x > 0):
                    x = x % n
                elif (x < 0):
                    x = x + n
                if (y > 0):
                    y = y % n
                elif (y < 0):
                    y = y + n
                c_ball_info[x][y].append([x, y, m, s, d])
    count = 0    
    for i in range(n):
        for j in range(n):
            if (len(c_ball_info[i][j]) >= 1):
                if (len(c_ball_info[i][j]) == 1):
                    count += c_ball_info[i][j][0][2]
                    continue
                new_m = 0
                new_s = 0
                flag = 0
                key = 0
                for k in range(len(c_ball_info[i][j])):
                    new_m += c_ball_info[i][j][k][2]
                    new_s += c_ball_info[i][j][k][3]
                    if (k == 0):
                        key = c_ball_info[i][j][k][4] % 2
                    else:
                        if (key != c_ball_info[i][j][k][4] % 2):
                            flag = 1
                
                    
                temp = []
                x = c_ball_info[i][j][k][0]
                y = c_ball_info[i][j][k][1]
                m = new_m // 5
                if (m != 0):
                    s = new_s // len(c_ball_info[i][j])

                    for _ in range(4):
                        count += m
                        temp.append([x, y, m, s, flag])
                        flag += 2
                    
                c_ball_info[i][j] = temp
    ball_info = c_ball_info
    return (count)

count = 0
for i in range(k):
    count = move_ball()

print(count)
