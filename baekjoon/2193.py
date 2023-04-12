import sys

input = sys.stdin.readline

n = int(input().strip())

array = [0, 1, 1, 2, 3]

if (n <= 4):
    print(array[n])
else:
    for i in range(5, n + 1):
        array.append(array[i - 1] + array[i - 2])
    print(array[n])