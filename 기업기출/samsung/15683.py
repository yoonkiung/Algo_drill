import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def cal_zero(array):
    ret = 0
    for i in range(n):
        for j in range(m):
            if (array[i][j] == 0):
                ret += 1
    return (ret)

def light_one_up(array, x, y):
    i = x
    j = y
    while (i >= 0 and array[i][j] != 6):
        if (array[i][j] == 0):
            array[i][j] = '#'
        i -= 1

def light_one_down(array, x, y):
    i = x
    j = y
    while (i < n and array[i][j] != 6):
        if (array[i][j] == 0):
            array[i][j] = '#'
        i += 1

def light_one_right(array, x, y):
    i = x
    j = y
    while (j < m and array[i][j] != 6):
        if (array[i][j] == 0):
            array[i][j] = '#'
        j += 1

def light_one_left(array, x, y):
    i = x
    j = y
    while (j >= 0 and array[i][j] != 6):
        if (array[i][j] == 0):
            array[i][j] = '#'
        j -= 1

def light_two_up(array, x, y):
    light_one_up(array, x, y)
    light_one_down(array, x, y)

def light_two_right(array, x, y):
    light_one_right(array, x, y)
    light_one_left(array, x, y)

def light_three_up(array, x, y):
    light_one_up(array, x, y)
    light_one_right(array, x, y)

def light_three_left(array, x, y):
    light_one_up(array, x, y)
    light_one_left(array, x, y)

def light_three_down(array, x, y):
    light_one_down(array, x, y)
    light_one_left(array, x, y)

def light_three_right(array, x, y):
    light_one_down(array, x, y)
    light_one_right(array, x, y)

def light_four_up(array, x, y):
    light_two_right(array, x, y)
    i = x
    j = y
    while (i >= 0 and array[i][j] != 6):
        if (array[i][j] == 0):
            array[i][j] = '#'   
        i -= 1

def light_four_down(array, x, y):
    light_two_right(array, x, y)
    i = x
    j = y
    while (i < n and array[i][j] != 6):
        if (array[i][j] == 0):
            array[i][j] = '#'   
        i += 1


def light_four_right(array, x, y):
    light_two_up(array, x, y)
    i = x
    j = y
    while (j < m and array[i][j] != 6):
        if (array[i][j] == 0):        
            array[i][j] = '#'
        j += 1

def light_four_left(array, x, y):
    light_two_up(array, x, y)
    i = x
    j = y
    while (j >= 0 and array[i][j] != 6):
        if (array[i][j] == 0):
            array[i][j] = '#'
        j -= 1

def light_five(array, x, y):
    light_two_right(array, x, y)
    light_two_up(array, x, y)
min_value = 65

def dfs(table, depth):
    if (depth == len(cctv)):
        global min_value
        min_value = min(min_value, cal_zero(table))
        return
    
    x, y, num = cctv[depth]
    if (num == 1):
        for i in range(4):
            if (i == 0):
                n_table = copy.deepcopy(table)
                light_one_down(n_table, x, y)
                dfs(n_table, depth + 1)
            elif (i == 1):
                n_table = copy.deepcopy(table)
                light_one_up(n_table, x, y)
                dfs(n_table, depth + 1)
            elif (i == 2):
                n_table = copy.deepcopy(table)
                light_one_right(n_table, x, y)
                dfs(n_table, depth + 1)
            elif (i == 3):
                n_table = copy.deepcopy(table)
                light_one_left(n_table, x, y)
                dfs(n_table, depth + 1)
    elif (num == 2):
        for i in range(2):
            if (i == 0):
                n_table = copy.deepcopy(table)
                light_two_right(n_table, x, y)
                dfs(n_table, depth + 1)
            elif (i == 1):
                n_table = copy.deepcopy(table)
                light_two_up(n_table, x, y)
                dfs(n_table, depth + 1)
    elif (num == 3):
        for i in range(4):
            if (i == 0):
                n_table = copy.deepcopy(table)
                light_three_left(n_table, x, y)
                dfs(n_table, depth + 1)
            elif (i == 1):
                n_table = copy.deepcopy(table)
                light_three_right(n_table, x, y)
                dfs(n_table, depth + 1)
            elif (i == 2):
                n_table = copy.deepcopy(table)
                light_three_up(n_table, x, y)
                dfs(n_table, depth + 1)               
            elif (i == 3):
                n_table = copy.deepcopy(table)
                light_three_down(n_table, x, y)
                dfs(n_table, depth + 1)
    elif (num == 4):
        for i in range(4):
            if (i == 0):
                n_table = copy.deepcopy(table)
                light_four_left(n_table, x, y)
                dfs(n_table, depth + 1)
            elif (i == 1):
                n_table = copy.deepcopy(table)
                light_four_right(n_table, x, y)
                dfs(n_table, depth + 1)
            elif (i == 2):
                n_table = copy.deepcopy(table)
                light_four_up(n_table, x, y)
                dfs(n_table, depth + 1)               
            elif (i == 3):
                n_table = copy.deepcopy(table)
                light_four_down(n_table, x, y)
                dfs(n_table, depth + 1)
    else:
        n_table = copy.deepcopy(table)
        light_five(n_table, x, y)
        dfs(n_table, depth + 1)

n, m = list(map(int, input().strip().split()))
board = []
cctv = []
for i in range(n):
    temp = list(map(int, input().strip().split()))
    board.append(temp)
    for j in range(m):
        if (1 <= temp[j] <= 5):
            cctv.append([i, j, temp[j]])
if (len(board) == 0):
    print(cal_zero(board))
else:
    dfs(board, 0)
print(min_value)