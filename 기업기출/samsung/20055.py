n, k = list(map(int, input().split()))
board = list(map(int, input().split()))
robot = [0] * (2 * n)

def rotate():
    global board
    global robot

    board = [board[2 * n - 1]] + board[:2 * n - 1]
    robot = [robot[2 * n - 1]] + robot[:2 * n - 1]

    robot[n - 1] = 0
    
def move():
    i = n - 2

    zero_count = 0
    if (robot[i] == 1 and robot[i + 1] == 0 and board[i + 1] >= 1):
        board[i + 1] -= 1
        if (board[i + 1] == 0):
            zero_count += 1
        robot[i] = 0
    
    i -= 1

    while (i >= 1):
        if (robot[i] == 1 and robot[i + 1] == 0 and board[i + 1] >= 1):
            board[i + 1] -= 1
            if (board[i + 1] == 0):
                zero_count += 1
            robot[i] = 0
            robot[i + 1] = 1
        i -= 1
    
    if (board[0] >= 1):
        robot[0] = 1
        board[0] -= 1
        if (board[0] == 0):
            zero_count += 1

    return (zero_count)

count = 0
time = 0
while (count < k):
    rotate()
    count += move()
    time += 1

print(time)

    
