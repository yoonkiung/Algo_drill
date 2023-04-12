import sys

sys.setrecursionlimit(10 ** 8)

ORIG = 'ORIG'
TEN = 'TEN'
TWENTY = 'TWENTY'
THIRTY = 'THIRTY'

input = sys.stdin.readline

info = list(map(int, input().split()))

origin = [i for i in range(0, 41, 2)]
ten_blue = [10, 13, 16, 19, 25, 30, 35, 40]
twenty_blue = [20, 22, 24, 25, 30, 35, 40]
thirty_blue = [30, 28, 27, 26, 25, 30, 35, 40]

player = [[0, ORIG], [0, ORIG], [0, ORIG], [0, ORIG]]

def new_pos(index, status, jump):
    new_index = jump + index
    if (status == ORIG):
        if (new_index >= len(origin)):
            return ([False, False])
        if (origin[new_index] == 10):
            return ([0, TEN])
        if (origin[new_index] == 20):
            return ([0, TWENTY])
        if (origin[new_index] == 30):
            return ([0, THIRTY])
        return ([new_index, status])
    elif (status == TEN):
        if (new_index >= len(ten_blue)):
            return ([False, False])
        return ([new_index, status])
    elif (status == TWENTY):
        if (new_index >= len(twenty_blue)):
            return ([False, False])
        return ([new_index, status])
    elif (status == THIRTY):
        if (new_index >= len(thirty_blue)):
            return ([False, False])
        return ([new_index, status])
    
def cur_num(index, status):
    if (status == ORIG):
        return (origin[index])
    if (status == TEN):
        return (ten_blue[index])
    if (status == TWENTY):
        return (twenty_blue[index])
    if (status == THIRTY):
        return (thirty_blue[index])

def is_same_num(index, status, c_index, c_status):
    num1 = cur_num(index, status)
    num2 = cur_num(c_index, c_status)

    if (num1 != num2):
        return (False)
    if (num1 == 10 or num1 == 20 or num1 == 25 or num1 == 35 or num1 == 40):
        return (True)
    if (num1 == 30):
        if (status == THIRTY and index == 0 and c_status == THIRTY and c_index == 0):
            return (True)
        if (status == THIRTY and index == 0):
            return (False)
        if (c_status == THIRTY and c_index == 0):
            return (False)
        return (True)

    if (status == c_status):
        return (True)
    return (False)

def is_same_pos(index, status, i):
    for j in range(4):
        if (i == j):
            continue
        c_index, c_status = player[j]
        if (not is_in_map(c_index, c_status)):
            continue
        if (c_index == index and c_status == status):
            return (True)
        if (is_same_num(index, status, c_index, c_status)):
            return (True)
    return (False)

def is_in_map(index, status):
    if (index == 100):
        return (False)
    else:
        return (True)

def get_point(index, status):
    if (status == ORIG):
        return (origin[index])
    if (status == TEN):
        return (ten_blue[index])
    if (status == TWENTY):
        return (twenty_blue[index])
    if (status == THIRTY):
        return (thirty_blue[index])

max_value = -1
def dfs(point, depth):
    
    
    if (depth >= 10):
        global max_value
        max_value = max(max_value, point)
        return
    
    jump = info[depth]
    for i in range(4):
        index, status = player[i]
        if (is_in_map(index, status)):
            new_index, new_status = new_pos(index, status, jump)
            new_point = 0
            if (not new_status):
                new_index = 100
            else:
                if (is_same_pos(new_index, new_status, i) == True):
                    continue
                new_point = get_point(new_index, new_status)
            player[i][0] = new_index
            player[i][1] = new_status
            dfs(point + new_point, depth + 1)
            player[i][0] = index
            player[i][1] = status

dfs(0, 0)
print(max_value)