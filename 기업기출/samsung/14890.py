import sys

input = sys.stdin.readline

n, l = list(map(int, input().strip().split()))

array = []
for i in range(n):
    array.append(list(map(int, input().strip().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

def is_same_level_low_up(i, j, l):
    level = array[i][j]
    for x in range(j, j + l):
        if (x >= n):
            return (False)
        if (level != array[i][x]):
            return (False)
        if (visited[i][x] == True):
            return (False)
    for x in range(j, j + l):
        visited[i][x] = True
    return (True)

def is_same_level_col_up(i, j, l):
    level = array[i][j]
    for x in range(i, i + l):
        if (x >= n):
            return (False)
        if (level != array[x][j]):
            return (False)
        if (visited[x][j] == True):
            return (False)
    for x in range(i, i + l):
        visited[x][j] = True 
    return (True)


def is_same_level_low_down(i, j, l):
    level = array[i][j]
    for x in range(j, j - l, -1):
        if (x < 0):
            return (False)
        if (level != array[i][x]):
            return (False)
        if (visited[i][x] == True):
            return (False)
    for x in range(j, j - l, -1):
        visited[i][x] = True
    return (True)

def is_same_level_col_down(i, j, l):
    level = array[i][j]
    for x in range(i, i - l, -1):
        if (x < 0):
            return (False)
        if (level != array[x][j]):
            return (False)
        if (visited[x][j]):
            return (False)
    for x in range(i, i - l, -1):
        visited[x][j] = True
    return (True)


count = 0
for i in range(n):
    flag = True
    j = 0
    while (j < n - 1):
        if (array[i][j] == array[i][j + 1]):
            j += 1
            continue
        elif (array[i][j] - array[i][j + 1] == 1):
            if (is_same_level_low_up(i, j + 1, l)):
                j += l
            else:
                flag = False
                break
        elif (array[i][j] - array[i][j + 1] == -1):
            if (is_same_level_low_down(i, j, l)):
                j += 1
            else:
                flag = False
                break
        else:
            flag = False
            break
    if (flag):
        count += 1

visited = [[False for _ in range(n)] for _ in range(n)]

for j in range(n):
    flag = True
    i = 0
    while (i < n - 1):
        if (array[i][j] == array[i + 1][j]):
            i += 1
            continue
        elif (array[i][j] - array[i + 1][j] == 1):
            if (is_same_level_col_up(i + 1, j, l)):
                i += l
            else:
                flag = False
                break
        elif (array[i][j] - array[i + 1][j] == -1):
            if (is_same_level_col_down(i, j, l)):
                i += 1
            else:
                flag = False
                break
        else:
            flag = False
            break
    if (flag):
        count += 1


print(count)