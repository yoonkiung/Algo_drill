import sys
from collections import deque

input = sys.stdin.readline

#input
n, m, v = list(map(int, input().strip().split()))

#create list
array = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = list(map(int, input().strip().split()))
    array[a].append(b)
    array[b].append(a)


for i in range(n + 1):
    array[i].sort()

#dfs
visited_dfs = [False] * (n + 1)

def dfs(node):
    visited_dfs[node] = True
    print(node, end=" ")
    for i in array[node]:
        if (visited_dfs[i] == False):
            dfs(i)

#bfs
visited_bfs = [False] * (n + 1)

def bfs(node):
    que = deque()
    que.append(node)
    visited_bfs[node] = True
    print(node, end=" ")
    while (que):
        for i in array[que.popleft()]:
            if (visited_bfs[i] == False):
                visited_bfs[i] = True
                print(i, end=" ")
                que.append(i)

dfs(v)
print()
bfs(v)