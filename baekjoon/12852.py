import sys
input = sys.stdin.readline

n = int(input().strip())

d = [0, 0, 1, 1]

for i in range(4, n + 1):
    temp = 1000000000
    if (i % 3 == 0):
        temp = min(temp, d[i // 3] + 1)
    if (i % 2 == 0):
        temp = min(temp, d[i // 2] + 1)
    temp = min(temp, d[i - 1] + 1)
    d.append(temp)

print(d[n])
cnt = d[n]
i = n
print(i, end=" ")

while (cnt > 0):
    min_value = 100000000
    if (i % 3 == 0):
        min_value = min(min_value, i // 3)
        cnt = d[i // 3]
    if (i % 2 == 0):
        min_value = min(min_value, i // 3)
        cnt = d[i // 2]
    if (i - 1 < min_value):
        min_value = i - 1
        cnt = d[i - 1]
    print(i, end = " ")