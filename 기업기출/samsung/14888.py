import sys
import copy
input = sys.stdin.readline

PLUS = 0
MIN = 1
MULTI = 2
DIV = 3

min_value = 1000000001
max_value = -1000000001

def dfs(i, oper, ex):
    if (i == n):
        global min_value
        global max_value
        min_value = min(ex, min_value)
        max_value = max(ex, max_value)
        return
    for j in range(4):
        if (oper[j] == 0):
            continue
        n_oper = copy.deepcopy(oper)
        n_oper[j] -= 1
        n_ex = ex
        if (j == PLUS):
            n_ex += array[i]
        elif (j == MIN):
            n_ex -= array[i]
        elif (j == MULTI):
            n_ex *= array[i]
        else:
            if (ex < 0):
                temp = ex * -1
                temp = temp // array[i]
                n_ex = temp * -1
            else:
                n_ex = ex // array[i]
        dfs(i + 1, n_oper, n_ex)


n = int(input().strip())

array = list(map(int, input().strip().split()))
operator = list(map(int, input().strip().split()))

dfs(1, operator, array[0])
print(max_value)
print(min_value)