import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input().strip())


def dfs(y, x):
    if (x < 0 or y < 0 or x >= m or y >= n):
        return
    if (array[y][x] == 0):
        return
    array[y][x] = 0
    dfs(y, x + 1)
    dfs(y + 1, x)
    dfs(y, x - 1)
    dfs(y - 1, x)

for i in range(t):
    m, n, k = list(map(int, input().strip().split()))
    array = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = list(map(int, input().strip().split()))
        array[y][x] = 1
    count = 0
    for x in range(m):
        for y in range(n):
            if (array[y][x] == 1):
                count += 1
                dfs(y, x)
    print(count)


