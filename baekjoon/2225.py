import sys
input = sys.stdin.readline

n, k = list(map(int, input().strip().split()))

array = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
array[1] = [1 for _ in range(n + 1)]

for i in range(1, k + 1):
    for j in range(n + 1):
        array[i][j] = array[i - 1][j] + array[i][j - 1]

print(array[k][n] % 1000000000)

