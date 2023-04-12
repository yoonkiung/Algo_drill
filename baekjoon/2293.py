import sys

input = sys.stdin.readline

n, k = list(map(int, input().strip().split()))

coins = []

for i in range(n):
    coins.append(int(input().strip()))
coins.sort()

d = [0] * (k + 1)
d[0] = 1

for coin in coins:
    for i in range(coin, k + 1):
        d[i] += d[i - coin]

print(d[k])
