import sys

input = sys.stdin.readline

t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    array = []
    for j in range(2):
        array.append(list(map(int, input().strip().split())))
    if (n == 1):
        print(max(array[0][0], array[1][0]))
        continue
    dp = [[0 for i in range(n)] for i in range(2)]
    dp[0][0] = array[0][0]
    dp[1][0] = array[1][0]
    dp[0][1] = array[1][0] + array[0][1]
    dp[1][1] = array[0][0] + array[1][1]
    
    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + array[0][i]
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + array[1][i]
    print(max(dp[0][n - 1], dp[1][n - 1]))
