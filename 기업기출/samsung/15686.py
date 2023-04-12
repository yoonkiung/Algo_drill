import sys
from itertools import combinations
input = sys.stdin.readline


def distance(x1, y1, x2, y2):
    return (abs(x1 - x2) + abs(y1 - y2))

n, m = list(map(int, input().strip().split()))

board = []
for _ in range(n):
    board.append(list(map(int, input().strip().split())))

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if (board[i][j] == 1):
            home.append((i, j))
        elif (board[i][j] == 2):
            chicken.append((i, j))

_chicken = list(combinations(chicken, m))
ans = []
for ch in _chicken:
    val = 0
    for h in home:
        lst = []
        for c in ch:
            lst.append(distance(c[0], c[1], h[0], h[1]))
        val += sorted(lst)[0]
    ans.append(val)

print(sorted(ans)[0])