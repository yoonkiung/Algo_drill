import sys

input = sys.stdin.readline

t = int(input().strip())

def find_max(array, x, y, n, m):
    max = -1
    for i in range(-1, 2):
        nx = x + i
        ny = y - 1
        if (nx < 0 or ny < 0 or nx >= n or ny >= m):
            continue
        if (array[nx][ny] > max):
            max = array[nx][ny]
    array[x][y] += max
    return (array)

for i in range(t):
    n, m = list(map(int, input().strip().split()))
    all = list(map(int, input().strip().split()))
    array = []
    for i in range(0, n * m, m):
        array.append(all[i:i + m])
    for j in range(1, m):
        for i in range(n):
            array = find_max(array, i, j, n, m)
    max = -1
    for i in range(n):
        if (array[i][m - 1] > max):
            max = array[i][m - 1]
    print(max)