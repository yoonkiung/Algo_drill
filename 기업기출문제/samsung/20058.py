from collections import deque

n, q = list(map(int, input().split()))
num = 2 ** n

array = []
for i in range(num):
    array.append(list(map(int, input().split())))

level = list(map(int, input().split()))

def rotate_part(x, y, length):
    cache = []
    for i in range(length):
        temp = []
        for j in range(length):
            temp.append(array[x + i][y + j])
        cache.append(temp)
    l = 0
    for j in range(y + length - 1, y - 1, -1):
        k = 0
        for i in range(x, x + length):
            array[i][j] = cache[l][k]
            k += 1
        l += 1

def rotate(length):
    for i in range(0, num, 2 ** length):
        for j in range(0, num, 2 ** length):
            rotate_part(i, j, 2 ** length)

def del_ice():
    global array
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    new_arr = [[0 for _ in range(num)] for _ in range(num)]

    for x in range(num):
        for y in range(num):
            count = 0
            if (array[x][y] > 0):
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if (nx < 0 or ny < 0 or nx >= num or ny >= 2 **n):
                        continue
                    if (array[nx][ny] >= 1):
                        count += 1

            if (0 <= count < 3):
                if (array[x][y] == 0):
                    new_arr[x][y] = array[x][y]    
                else:
                    new_arr[x][y] = array[x][y] - 1
            else:
                new_arr[x][y] = array[x][y]
    
    array = new_arr

visited = [[False] * num for _ in range(num)]

def search_big(x, y):
    queue = deque()
    queue.append((x, y))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    count = 1

    while (queue):
        x, y = queue.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or ny < 0 or nx >= num or ny >= num):
                continue
            if (visited[nx][ny] == True or array[nx][ny] == 0):
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
            count += 1
    return (count)

for lev in level:
    rotate(lev)
    del_ice()

count = 0
for ele in array:
    count += sum(ele)
print(count)



count = 0
for i in range(num):
    for j in range(num):
        if (visited[i][j] == True or array[i][j] == 0):
            continue
        count = max(count, search_big(i, j))
print(count)

