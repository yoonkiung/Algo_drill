import sys
input = sys.stdin.readline

n = int(input().strip())

d = []
d.append([1, 0, 0])
for i in range(1, n + 1):
    temp = [0, 0, 0]
    temp[0] = (d[i - 1][0] + d[i - 1][1] + d[i - 1][2]) % 9901
    temp[1] = (d[i - 1][0] + d[i - 1][2]) % 9901
    temp[2] = (d[i - 1][0] + d[i - 1][1]) % 9901
    d.append(temp)

print(sum(d[n]) % 9901)