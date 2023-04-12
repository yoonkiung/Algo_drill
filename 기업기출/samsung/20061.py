import sys

input = sys.stdin.readline

n = int(input())

green = [[False] * 4 for _ in range(6)]
blue = [[False] * 6 for _ in range(4)]

depth_green = [5] * 4
depth_blue = [5] * 4

def find_depth_green(x, y):
    return (depth_green[y])

def find_depth_blue(x, y):
    return (depth_blue[x])

def update_max_depth_green():
    for j in range(4):
        for i in range(6):
            if (green[i][j] == True):
                depth_green[j] = i - 1
                break
            depth_green[j] = 5

def update_max_depth_blue():
    for i in range(4):
        for j in range(6):
            if (blue[i][j] == True):
                depth_blue[i] = j - 1
                break
            depth_blue[i] = 5

def is_all_block_green(i):
    for j in range(4):
        if (green[i][j] == False):
            return (False)
    return (True)

def is_all_block_blue(j):
    for i in range(4):
        if (blue[i][j] == False):
            return (False)
    return (True)

def cal_point_green():
    point = 0
    global green

    while (True):
        flag = False
        for i in range(2, 6):
            if (is_all_block_green(i)):
                point += 1
                flag = True
                if (i < 5):
                    green = [[False] * 4] + \
                            green[:i] + \
                            green[i + 1:]
                elif (i == 5):
                    green = [[False] * 4] + \
                            green[:i]
        
        if (not flag):
            break
    return (point)

def cal_point_blue():
    point = 0
    global blue

    while (True):
        flag = False
        for j in range(2, 6):
            if (is_all_block_blue(j)):
                # print("j", j)
                flag = True
                blue = list(map(list, zip(*blue)))
                point += 1
                if (j < 5):
                    blue = [[False] * 4] + \
                            blue[:j] + \
                            blue[j + 1:]
                elif (j == 5):
                    blue = [[False] * 4] + \
                            blue[:j]
                blue = list(map(list, zip(*blue)))

        if (not flag):
            break
    return (point)

def search_top_green():
    global green
    count = 0
    for i in range(2):
        for j in range(4):
            if (green[i][j] == True):
                count += 1
                break
    
    if (count == 1):
        green = [[False] * 4] + \
                green[:5]
    elif (count == 2):
        green = [[False] * 4] + \
                [[False] * 4] + \
                green[:4]

def search_top_blue():
    global blue
    count = 0
    for j in range(2):
        for i in range(4):
            if (blue[i][j] == True):
                count += 1
                break
    
    if (count == 1):
        blue = list(map(list, zip(*blue)))
        blue = [[False] * 4] + \
                blue[:5]
        blue = list(map(list, zip(*blue)))
    elif (count == 2):
        blue = list(map(list, zip(*blue)))
        blue = [[False] * 4] + \
                [[False] * 4] + \
                blue[:4]
        blue = list(map(list, zip(*blue)))

def move_green(t, x, y):
    max_depth = 6
    
    # max_depth 찾기
    if (t == 1 or t == 3):
        max_depth = find_depth_green(x, y)
    elif (t == 2):
        max_depth = min(max_depth, find_depth_green(x, y))
        max_depth = min(max_depth, find_depth_green(x, y + 1))
    # 블럭 놓기
    if (t == 1 or t == 3):
        green[max_depth][y] = True
        if (t == 3):
            green[max_depth - 1][y] = True
    elif (t == 2):
        green[max_depth][y] = True
        green[max_depth][y + 1] = True
    
    # 점수 계산
    point = cal_point_green()

    # 연한배열 확인
    search_top_green()
    # max_depth 배열 업데이트
    update_max_depth_green()
    return (point)

def move_blue(t, x, y):
    max_depth = 6

    # max_depth 찾기
    if (t == 1 or t == 2):
        max_depth = find_depth_blue(x, y)
    elif (t == 3):
        max_depth = min(max_depth, find_depth_blue(x, y))
        max_depth = min(max_depth, find_depth_blue(x + 1, y))
    # print("max_depth = ", max_depth)
    # 블럭 놓기
    if (t == 1 or t == 2):
        blue[x][max_depth] = True
        if (t == 2):
            blue[x][max_depth - 1] = True
    elif (t == 3):
        blue[x][max_depth] = True
        blue[x + 1][max_depth] = True
    # for ele in blue:
    #     print(ele)
    # print()

    # 점수 계산
    point = cal_point_blue()
    # for ele in blue:
    #     print(ele)
    # print()
    # 연한배열 확인
    search_top_blue()
    # for ele in blue:
    #     print(ele)
    # print()
    # max_depth 배열 업데이트
    update_max_depth_blue()
    
    return (point)

def cal_true():
    global green
    global blue

    blue = list(map(list, zip(*blue)))

    count = 0
    for i in range(6):
        for j in range(4):
            if (green[i][j] == True):
                count += 1
            if (blue[i][j] == True):
                count += 1
    return (count)

point = 0
for _ in range(n):
    t, x, y = list(map(int, input().split()))
    
    point += move_green(t, x, y)
    point += move_blue(t, x, y)
    
print(point)
print(cal_true())