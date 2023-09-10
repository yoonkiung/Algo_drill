import sys
import copy
input = sys.stdin.readline

min_value = 2001

def cal_power(board):
    ret = 0
    for i in range(len(board)):
        for j in range(i, len(board)):
            ret += array[board[i]][board[j]] + array[board[j]][board[i]]
    return (ret)

def dfs(i, start, link):
    if (i == n):
        global min_value
        gap = abs(cal_power(start) - cal_power(link))
        if (gap == 0):
            print(0)
            exit()
        min_value = min(min_value, gap)
        return
    
    else:
        n_start = copy.deepcopy(start)
        n_link = copy.deepcopy(link)
        if (len(n_start) == n // 2):
            n_link.append(i)   
            dfs(i + 1, n_start, n_link)
        elif (len(n_link) == n // 2):
            n_start.append(i)
            dfs(i + 1, n_start, n_link)
        else:
            n_link.append(i)   
            dfs(i + 1, n_start, n_link)
            del n_link[-1]
            n_start.append(i)
            dfs(i + 1, n_start, n_link)
        

n = int(input().strip())

array = []
for i in range(n):
    array.append(list(map(int, input().strip().split())))

start = []
link = []
dfs(0, start, link)
print(min_value)
