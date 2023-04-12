from math import floor

n = int(input())
num = n

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
board = [[0 for _ in range(n)] for _ in range(n)]

def move_percent(x, y, percent):
    if (not (x < 0 or y < 0 or x >= num or y >= num)):
        array[x][y] += percent
        return (0)
    return (percent)

def move_sand(x, y, delta):
    send = array[x][y]
    count = 0
    if (delta[0] == 0 and delta[1] == -1):
        
        nx = x - 1
        ny = y
        count += move_percent(nx, ny, floor(send * 0.07))
        nx = x + 1
        ny = y
        count += move_percent(nx, ny, floor(send * 0.07))

        nx = x - 1
        ny = y - 1
        count += move_percent(nx, ny, floor(send * 0.1))
        nx = x + 1
        ny = y - 1
        count += move_percent(nx, ny, floor(send * 0.1))

        nx = x - 1
        ny = y + 1
        count += move_percent(nx, ny, floor(send * 0.01))
        nx = x + 1
        ny = y + 1
        count += move_percent(nx, ny, floor(send * 0.01))

        nx = x - 2
        ny = y
        count += move_percent(nx, ny, floor(send * 0.02))
        nx = x + 2
        ny = y
        count += move_percent(nx, ny, floor(send * 0.02))
        
        nx = x
        ny = y - 2
        count += move_percent(nx, ny, floor(send * 0.05))
        
        nx = x
        ny = y - 1
        send -= floor(send * 0.07) * 2 + \
                floor(send * 0.1) * 2 + \
                floor(send * 0.01) * 2 + \
                floor(send * 0.02) * 2 + \
                floor(send * 0.05)
        count += move_percent(nx, ny, send)

    elif (delta[0] == 0 and delta[1] == 1):
        nx = x - 1
        ny = y
        count += move_percent(nx, ny, floor(send * 0.07))
        
        nx = x + 1
        ny = y
        count += move_percent(nx, ny, floor(send * 0.07))

        nx = x - 1
        ny = y - 1
        count += move_percent(nx, ny, floor(send * 0.01))
        nx = x + 1
        ny = y - 1
        count += move_percent(nx, ny, floor(send * 0.01))

        nx = x - 1
        ny = y + 1
        count += move_percent(nx, ny, floor(send * 0.1))
        nx = x + 1
        ny = y + 1
        count += move_percent(nx, ny, floor(send * 0.1))

        nx = x - 2
        ny = y
        count += move_percent(nx, ny, floor(send * 0.02))
        nx = x + 2
        ny = y
        count += move_percent(nx, ny, floor(send * 0.02))
        
        nx = x
        ny = y + 2
        count += move_percent(nx, ny, floor(send * 0.05))
        
        nx = x
        ny = y + 1
        send -= floor(send * 0.07) * 2 + \
                floor(send * 0.1) * 2 + \
                floor(send * 0.01) * 2 + \
                floor(send * 0.02) * 2 + \
                floor(send * 0.05)
        count += move_percent(nx, ny, send)

    elif (delta[0] == 1 and delta[1] == 0):
        nx = x
        ny = y - 1
        count += move_percent(nx, ny, floor(send * 0.07))
        
        nx = x
        ny = y + 1
        count += move_percent(nx, ny, floor(send * 0.07))

        nx = x - 1
        ny = y - 1
        count += move_percent(nx, ny, floor(send * 0.01))
        nx = x - 1
        ny = y + 1
        count += move_percent(nx, ny, floor(send * 0.01))

        nx = x + 1
        ny = y - 1
        count += move_percent(nx, ny, floor(send * 0.1))
        nx = x + 1
        ny = y + 1
        count += move_percent(nx, ny, floor(send * 0.1))

        nx = x
        ny = y - 2
        count += move_percent(nx, ny, floor(send * 0.02))
        nx = x
        ny = y + 2
        count += move_percent(nx, ny, floor(send * 0.02))
        
        nx = x + 2
        ny = y
        count += move_percent(nx, ny, floor(send * 0.05))
        
        nx = x + 1
        ny = y
        send -= floor(send * 0.07) * 2 + \
                floor(send * 0.1) * 2 + \
                floor(send * 0.01) * 2 + \
                floor(send * 0.02) * 2 + \
                floor(send * 0.05)
        count += move_percent(nx, ny, send)

    elif (delta[0] == -1 and delta[1] == 0):
        nx = x
        ny = y - 1
        count += move_percent(nx, ny, floor(send * 0.07))
        
        nx = x
        ny = y + 1
        count += move_percent(nx, ny, floor(send * 0.07))

        nx = x + 1
        ny = y - 1
        count += move_percent(nx, ny, floor(send * 0.01))
        nx = x + 1
        ny = y + 1
        count += move_percent(nx, ny, floor(send * 0.01))

        nx = x - 1
        ny = y - 1
        count += move_percent(nx, ny, floor(send * 0.1))
        nx = x - 1
        ny = y + 1
        count += move_percent(nx, ny, floor(send * 0.1))

        nx = x
        ny = y - 2
        count += move_percent(nx, ny, floor(send * 0.02))
        nx = x
        ny = y + 2
        count += move_percent(nx, ny, floor(send * 0.02))
        
        nx = x - 2
        ny = y
        count += move_percent(nx, ny, floor(send * 0.05))
        
        nx = x - 1
        ny = y
        send -= floor(send * 0.07) * 2 + \
                floor(send * 0.1) * 2 + \
                floor(send * 0.01) * 2 + \
                floor(send * 0.02) * 2 + \
                floor(send * 0.05)
        count += move_percent(nx, ny, send)

    
    array[x][y] = 0
    
    return (count)

x = n // 2
y = n // 2
n = 1
f = -1
count = 0

while (n < num + 1):
    for i in range(n):
        y += f
        if (y == -1):
            break
        board[x][y] = 1
        count += move_sand(x, y, [0, f])
    f *= -1
    if (y == -1):
        break
    for i in range(n):
        x += f
        if (x == -1):
            break
        board[x][y] = 1
        count += move_sand(x, y, [f, 0])
    if (x == -1):
        break
    n += 1

print(count)