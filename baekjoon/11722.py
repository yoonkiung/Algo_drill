import sys

input = sys.stdin.readline
n = int(input().strip())
array = list(map(int, input().strip().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if (array[j] > array[i]):
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))