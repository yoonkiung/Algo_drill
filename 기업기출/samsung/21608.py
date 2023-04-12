n = int(input())

dic_favorite = {}
student = [0]
board = [[0] * n for _ in range(n)]
num_student = n ** 2

for i in range(n ** 2):
    key, a, b, c, d = list(map(int, input().split()))
    student.append(key)
    dic_favorite[key] = [a, b, c, d]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(1, num_student + 1):
    number = student[i]

    prior = dic_favorite[number]

    collect = []
    for x in range(n):
        for y in range(n):
            if (board[x][y] != 0):
                continue
            temp = [x, y, 0, 0]
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]

                if (nx < 0 or ny < 0 or nx >= n or ny >= n):
                    continue
                if (board[nx][ny] == 0):
                    temp[3] += 1
                for pri in prior:
                    if (pri == board[nx][ny]):
                        temp[2] += 1
                
            collect.append(temp)
    
    collect.sort(key = lambda x: x[1])
    collect.sort(key = lambda x: x[0])
    collect.sort(key = lambda x: x[3], reverse = True)
    collect.sort(key = lambda x: x[2], reverse = True)
    
    x, y = collect[0][0], collect[0][1]
    board[x][y] = number

count = 0
for i in range(n):
    for j in range(n):
        number = board[i][j]
        
        prior = dic_favorite[number]
        temp = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if (nx < 0 or ny < 0 or nx >= n or ny >= n):
                    continue
            
            if (board[nx][ny] in prior):
                temp += 1
        
        if (temp == 1):
            count += 1
        elif (temp == 2):
            count += 10
        elif (temp == 3):
            count += 100
        elif (temp == 4):
            count += 1000

print(count)
