import sys

input = sys.stdin.readline

#input
n = int(input().strip())

array = []
for i in range(n):
    array.append(list(map(int, input().strip())))

count = 0

def dfs(x, y):
    global count
    if (x < 0 or y < 0 or x >= n or y >= n):
        return
    if (array[x][y] == 0):
        return
    array[x][y] = 0
    count += 1
    dfs(x + 1, y)
    dfs(x, y + 1)
    dfs(x - 1, y)
    dfs(x, y - 1)

arr_element = []
count_group = 0
for i in range(n):
    for j in range(n):
        if (array[i][j] == 1):
            count_group += 1
            dfs(i, j)
            arr_element.append(count)
            count = 0

print(count_group)
arr_element.sort()
for element in arr_element:
    print(element)
