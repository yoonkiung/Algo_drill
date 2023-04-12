import sys
sys.setrecursionlimit(10 ** 6)

g_count = 0

def check(index, board):
    i = 0
    while (i < index):
        if (board[index] == board[i]):
            return False
        elif (index - i == abs(board[index] - board[i])):
            return False
        i += 1
    return True

def queen(i, n, board):
    global g_count

    if i == n:
        g_count += 1
    else:
        for j in range(n):
            board[i] = j
            if (check(i, board)):
                queen(i + 1, n, board)

if __name__ == '__main__':
    n = int(input())
    board = [None] * n
    queen(0, n, board)
    print(g_count)

# 사간초과 아직 해결 못함...