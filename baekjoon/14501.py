import sys

input = sys.stdin.readline

# dp
# n = int(input().strip())

# T = []
# P = []

# for i in range(n):
#     temp = list(map(int, input().strip().split()))
#     T.append(temp[0])
#     P.append(temp[1])

# d = [0] * (n + 1)

# for i in range(n):
#     for j in range(i + T[i], n + 1):
#         if (d[j] < d[i] + P[i]):
#             d[j] = d[i] + P[i]

# print(max(d))

#dfs

def dfs(day, profit):
    global max_rev
    if (day == n):
        max_rev = max(max_rev, profit)
        return
    t = table[day][0]
    p = table[day][1]
    dfs(day + 1, profit)
    if (day + t <= n):
        dfs(day + t, profit + p)

n = int(input().strip())
table = []
for i in range(n):
    table.append(list(map(int, input().strip().split())))

max_rev = 0
dfs(0, 0)

print(max_rev)