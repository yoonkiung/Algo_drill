import sys

input = sys.stdin.readline

t = int(input().strip())

array = [0 for i in range(101)]
array[1] = 1
array[2] = 1
array[3] = 1
for i in range(98):
    array[i + 3] = array[i] + array[i + 1]

for i in range(t):
    print(array[int(input().strip())])