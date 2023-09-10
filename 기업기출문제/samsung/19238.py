from collections import deque
INF = 5000000


n, m, fuel = list(map(int, input().split()))

board = []

info = {}

for i in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)

driver = list(map(int, input().split()))
driver[0] -= 1
driver[1] -= 1


for i in range(m):
    cx, cy, dx, dy = list(map(int, input().split()))

    board[cx - 1][cy - 1] = 'C'
    info[(cx - 1, cy - 1)] = (dx - 1, dy - 1)

def find_human(x, y):
    queue = deque()
    queue.append((x, y, 0))

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visited = [[False] * n for _ in range(n)]
    min_depth = INF
    cus_list = []
    while (queue):
        x, y, depth = queue.popleft()
        visited[x][y] = True
        
        if (board[x][y] ==  'C'):
            if (min_depth == INF):
                min_depth = depth
            elif (min_depth < depth):
                cus_list.sort(key = lambda x: x[1])
                cus_list.sort(key = lambda x: x[0])
                return (cus_list[0])
            cus_list.append([x, y, depth])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or ny < 0 or nx >= n or ny >= n \
                or board[nx][ny] == 1 \
                or visited[nx][ny] == True):
                continue
            
            queue.append((nx, ny, depth + 1))
            visited[nx][ny] = True
    if (len(cus_list) == 0):
        return (INF, INF, INF)
    else:
        return (cus_list[0])

def find_shortest(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, 0))

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visited = [[False] * n for _ in range(n)]

    while (queue):
        x, y, depth = queue.popleft()
        visited[x][y] = True
        if (x == x2 and y == y2):
            return (depth)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or ny < 0 or nx >= n or ny >= n \
                or board[nx][ny] == 1 \
                or visited[nx][ny] == True):
                continue
            
            queue.append((nx, ny, depth + 1))
            visited[nx][ny] = True
    return (INF)



for i in range(m):
    driver_x, driver_y = driver[0], driver[1]

    c_x, c_y, length = find_human(driver_x, driver_y)
    if (fuel < length):
        print(-1)
        break
    if (c_x == INF and c_y == INF and length == INF):
        print(-1)
        break

    fuel -= length
    driver = [c_x, c_y]
    d_x, d_y = info[(c_x, c_y)]
    length = find_shortest(c_x, c_y, d_x, d_y)
    if (fuel < length):
        print(-1)
        break
    if (c_x == INF and c_y == INF and d_x == INF and d_y == INF):
        print(-1)
        break
    fuel -= length
    fuel += length * 2
    driver = [d_x, d_y]
    board[c_x][c_y] = 0
    
    if (i == m - 1):
        print(fuel)
