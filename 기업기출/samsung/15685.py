import sys

input = sys.stdin.readline

n = int(input().strip())

table = [[0 for _ in range(101)] for _ in range(101)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):
    y, x, d, g = list(map(int, input().strip().split()))
    table[x][y] = 1

    curve_list = [d]
    for j in range(g):
        for k in range(len(curve_list) - 1, -1, -1):
            curve_list.append((curve_list[k] + 1) % 4)

    for j in range(len(curve_list)):
        x += dx[curve_list[j]]
        y += dy[curve_list[j]]
        
        if (0 <= x <= 100 and 0 <= y <= 100):
            table[x][y] = 1


count = 0    
for i in range(100):
    for j in range(100):
        if (table[i][j] == 1 and table[i + 1][j] == 1 and table[i][j + 1] == 1 and table[i + 1][j + 1] == 1):
            count += 1

# for ele in table:
#     print(ele)
# print()
print(count)
