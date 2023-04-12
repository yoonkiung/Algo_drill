import sys

input = sys.stdin.readline

n, m = list(map(int, input().split(" ")))

array = []

for i in range(n):
    temp_arr = list(map(int, input().strip()))
    array.append(temp_arr)


def dfs(x, y):
    if (x < 0 or x > n - 1 or y < 0 or y > m - 1):
        return False
    if (array[x][y] == 0):
        array[x][y] = 1
        dfs(x - 1, y)
        dfs(x , y - 1)
        dfs(x + 1, y)
        dfs(x , y + 1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if (dfs(i, j)):
            count += 1

print(count)