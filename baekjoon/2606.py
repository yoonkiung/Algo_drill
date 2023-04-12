import sys

input = sys.stdin.readline

#input
n = int(input().strip())
v = int(input().strip())

#variable init
array = [[] for _ in range(n + 1)]
for i in range(v):
    com1, com2 = list(map(int, input().strip().split()))
    array[com1].append(com2)
    array[com2].append(com1)

visited = [False] * (n + 1)

count = -1
def dfs(node):
    global count
    count += 1
    visited[node] = True
    for i in array[node]:
        if (visited[i] == False):
            dfs(i)

dfs(1)
print(count)