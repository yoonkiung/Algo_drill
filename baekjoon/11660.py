import sys
import copy
input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))
array = []
for i in range(n):
    array.append(list(map(int, input().strip().split())))
dp = copy.deepcopy(array)
for i in range(n):
    for j in range(n):
        if (i == 0 and j == 0):
            continue
        if (i == 0):
            dp[i][j] += dp[i][j - 1]
        elif (j == 0):
            dp[i][j] += dp[i - 1][j]
        else:
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for i in range(m):
    x1, y1, x2, y2 = list(map(int, input().strip().split()))
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    if (x1 == 0 and y1 == 0):
        print(dp[x2][y2])
        continue
    elif (y1 == 0):
        result = dp[x2][y2] - \
                    dp[x1 - 1][y2]
    elif (x1 == 0):
        result = dp[x2][y2] - \
                    dp[x2][y1 - 1]
    else:
        result = dp[x2][y2] - \
                    dp[x2][y1 - 1] - \
                    dp[x1 - 1][y2] + \
                    dp[x1 - 1][y1 - 1]    
    print(result)