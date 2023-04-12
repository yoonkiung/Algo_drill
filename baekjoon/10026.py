import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input().strip())

general_array = []
array = []

for i in range(n):
    temp_str = input().strip()
    temp_arr = list(temp_str)
    general_array.append(temp_arr)
    array.append(temp_arr.copy())

for i in range(n):
    for j in range(n):
        if (array[i][j] == 'R'):
            array[i][j] = 'G'

def dfs_general(x, y, char):
    if (x < 0 or y < 0 or x >= n or y >= n):
        return
    if (general_array[x][y] != char):
        return
    general_array[x][y] = 'x'
    dfs_general(x + 1, y, char)
    dfs_general(x, y + 1, char)
    dfs_general(x - 1, y, char)
    dfs_general(x, y - 1, char)

def dfs(x, y, char):
    if (x < 0 or y < 0 or x >= n or y >= n):
        return
    if (array[x][y] != char):
        return
    array[x][y] = 'x'
    dfs(x + 1, y, char)
    dfs(x, y + 1, char)
    dfs(x - 1, y, char)
    dfs(x, y - 1, char)
    

normal_count = 0
count = 0
for i in range(n):
    for j in range(n):
        if (general_array[i][j] != 'x'):
            normal_count += 1
            dfs_general(i, j, general_array[i][j])
        if (array[i][j] != 'x'):
            count += 1
            dfs(i, j, array[i][j])

print(normal_count, end=" ")
print(count)