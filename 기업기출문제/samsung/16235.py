import sys

input = sys.stdin.readline

n, m, k = list(map(int, input().strip().split()))

a = []
for i in range(n):
    a.append(list(map(int, input().strip().split())))

board = [[[] for _ in range(n)] for _ in range(n)]
food = [[5 for _ in range(n)] for _ in range(n)]

memory = []
for i in range(m):
    x, y, z = list(map(int, input().strip().split()))
    board[x - 1][y - 1].append(z)
    memory.append((x - 1, y - 1))
for mem in memory:
    board[mem[0]][mem[1]].sort()
    
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def spring_summer():
    extension = []
    for i in range(n):
        for j in range(n):
            if (board[i][j]):
                dead = 0
                tmp_len = len(board[i][j])
                for k in range(tmp_len):
                    if (not (board[i][j][k] <= food[i][j])):
                        index = k
                        while (k < tmp_len):
                            dead += board[i][j][index] // 2
                            del board[i][j][index]
                            k += 1
                        break
                    else:
                        food[i][j] -= board[i][j][k]
                        board[i][j][k] += 1
                        if (board[i][j][k] % 5 == 0):
                            extension.append((i, j, k))
                food[i][j] += dead
            food[i][j] += a[i][j]

    for exten in extension:
        i, j, k = exten[0], exten[1], exten[2]
        for index in range(8):
                nx = i + dx[index]
                ny = j + dy[index]
                if (nx < 0 or nx >= n or ny < 0 or ny >= n):
                    continue
                board[nx][ny].insert(0, 1)

for _ in range(k):
    spring_summer()

count = 0
for i in range(n):
    for j in range(n):
        count += len(board[i][j])
print(count)
