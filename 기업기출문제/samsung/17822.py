import sys
import copy
input = sys.stdin.readline

n, m, t= list(map(int, input().split()))

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

def rotate_right(array):
    array = [array[m - 1]] + array[:m - 1]
    return (array)

def rotate_left(array):
    array = array[1:m] + [array[0]]
    return (array)

def search_own(old, new):
    flag = False
    
    for i in range(m):
        if (old[i] == 0):
            continue
        elif (i == 0):
            if (old[i] == old[m - 1] and old[i] == old[1]):
                new[0] = 0
                new[1] = 0
                new[m - 1] = 0
                flag = True
            elif (old[i] == old[m - 1]):
                new[i] = 0
                new[m - 1] = 0
                flag = True
            elif (old[i] == old[1]):
                new[i] = 0
                new[1] = 0
                flag = True
        elif (i == m - 1):
            if (old[i] == old[0] and old[i] == old[m - 2]):
                new[i] = 0
                new[0] = 0
                new[m - 2] = 0
                flag = True
            elif (old[i] == old[0]):
                new[i] = 0
                new[0] = 0
                flag = True
            elif(old[i] == old[m - 2]):
                new[i] = 0
                new[m - 2] = 0
                flag = True
        else:
            if (old[i] == old[i - 1] and old[i] == old[i + 1]):
                new[i] = 0
                new[i + 1] = 0
                new[i - 1] = 0
                flag = True
            elif (old[i] == old[i - 1]):
                new[i] = 0
                new[i - 1] = 0
                flag = True
            elif (old[i] == old[i + 1]):
                new[i] = 0
                new[i + 1] = 0
                flag = True
    return (flag)
    
def search_other(old, new, first, second):
    flag = False

    for i in range(m):
        if (old[first][i] != 0 and old[first][i] == old[second][i]):
            new[first][i] = 0
            new[second][i] = 0
            flag = True
    return (flag)

def search_others(old, new):
    flag = False

    for i in range(n - 1):
        temp = search_other(old, new, i, i + 1)
        if (temp):
            flag = temp
    return (flag)
            
def cal_average(table):
    div = 0
    add = 0
    for i in range(n):
        for j in range(m):
            if (table[i][j] > 0):
                div += 1
                add += table[i][j]
    if (div == 0 and add == 0):
        return (0)
    return (add / div)

def update_board(table):
    ave = cal_average(table)
    for i in range(n):
        for j in range(m):
            if (table[i][j] != 0 and table[i][j] > ave):
                table[i][j] -= 1
            elif (table[i][j] != 0 and table[i][j] < ave):
                table[i][j] += 1

def search():
    global board
    c_board = copy.deepcopy(board)
    flag = False

    for i in range(n):
        temp = search_own(board[i], c_board[i])
        if (temp):
            flag = temp
    # print("search own")
    # for ele in c_board:
    #     print(ele)
    # print()
    temp = search_others(board, c_board)
    # print("search others")
    # for ele in c_board:
    #     print(ele)
    # print()
    if (temp):
        flag = temp
    
    if (not flag):
        update_board(c_board)
        # print("update_board")
        # for ele in c_board:
        #     print(ele)
        # print()

    board = c_board
    # print("final")
    # for ele in c_board:
    #     print(ele)
    # print()

for i in range(t):
    x, d, k = list(map(int, input().split()))
    # print("original")
    # for ele in board:
    #     print(ele)
    # print()
    if (d == 0):
        z = 1
        while (z * x <= n):
            for j in range(k):
                board[z * x - 1] = rotate_right(board[z * x - 1])
            z += 1
            
    else:
        z = 1
        while (z * x <= n):
            for j in range(k):
                board[z * x - 1] = rotate_left(board[z * x - 1])
            z += 1
    # print("rotate")
    # for ele in board:
    #     print(ele)
    # print()
    search()

count = 0    
for i in range(n):
    count += sum(board[i])
print(count)