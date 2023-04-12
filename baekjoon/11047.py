import sys

n, k = map(int, sys.stdin.readline().split())

array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort(reverse=True)

coins = 0
for element in array:
    if (k // element >= 1):
        coins += k // element
        k %= element
    if (k == 0):
        break

print(coins)