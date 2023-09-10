import sys

input = sys.stdin.readline

r, c, k = list(map(int, input().split()))

board = []
for _ in range(3):
    board.append(list(map(int, input().split())))

def sorting(num):
    max_len = num
    for i in range(len(board)):
        dic = {}
        for j in range(len(board[i])):
            if (board[i][j] == 0):
                continue
            if (board[i][j] in dic):
                dic[board[i][j]] += 1
            else:
                dic[board[i][j]] = 1
        dic = dict(sorted(dic.items()))
        dic = dict(sorted(dic.items(), key = lambda x : x[1]))
        new_array = []
        for di in dic.items():
            new_array.append(di[0])
            new_array.append(di[1])
        board[i] = new_array
        max_len = max(len(board[i]), max_len)
    
    for i in range(len(board)):
        arr_len = len(board[i])
        if (arr_len < max_len):
            board[i] += [0] * (max_len - arr_len)
    return(max_len)

col = 3
row = 3
time = 0
while (True):
    if (time >= 101):
        break
    if (0 <= r - 1 < len(board) and 0 <= c - 1 < len(board[0]) and board[r - 1][c - 1] == k):
        break
    if (row >= col):
        col = sorting(col)
    else:
        board = list(map(list, zip(*board)))
        row = sorting(row)
        board = list(map(list, zip(*board)))
    time += 1
if (time >= 101):
    print(-1)
else:
    print(time)