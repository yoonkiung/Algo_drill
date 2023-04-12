import sys
import copy
input = sys.stdin.readline
def is_vaild(table):
    if (m == 0):
        return (True)
    for i in range(n):
        x = i
        y = i
        while (x < h):
            if (table[x][y] == 1):
                if (0 <= y - 1 <= n - 1 and table[x][y - 1] == 1):
                    y -= 1
                elif (0 <= y + 1 <= n - 1 and table[x][y + 1] == 1):
                    y += 1
            x += 1
        if (x != i):
            return (False)
    return (True)
min_value = 4
def dfs(table, depth):
    for ele in table:
        print(ele)
    print()
    if (depth == 4):
        return
    for i in range(h):
        c_table = copy.deepcopy(table)
        for j in range(n):
            if (table[i][j] == 0):
                if (0 <= j - 1 <= n - 1 and table[i][j - 1] == 0):
                    c_table[i][j - 1] = 1
                    c_table[i][j] = 1
                    if (is_vaild(c_table)):
                        global min_value
                        min_value = min(min_value, depth)
                    else:
                        dfs(c_table, depth + 1)
n, m, h = list(map(int, input().strip().split()))
board = [[0 for _ in range(n)] for _ in range(h)]
for i in range(m):
    a, b = list(map(int, input().strip().split()))
    board[a - 1][b] = 1
    board[a - 1][b - 1] = 1
if (is_vaild(board)):
    print(0)
else:
    dfs(board, 1)
    if (min_value >= 4):
        print(-1)
    else:
        print(min_value)