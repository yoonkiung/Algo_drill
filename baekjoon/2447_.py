import sys
from typing import Any

sys.setrecursionlimit(10 ** 6)

g_arr = []
n = int(input())

g_arr = [[' ' for i in range (n)] for i in range (n)]

def stars(n: int) -> None:
	
	if n == 3:
		g_arr[0] = g_arr[2] = ['*', '*', '*']
		g_arr[1] =['*', ' ', '*']
		return 

	div3 = n // 3
	stars(div3)

	for i in range(0, n, div3):
		for j in range(0, n, div3):
			if i != div3 or j != div3:
				for k in range(div3):
					g_arr[k + i][j:j + div3] = g_arr[k][:div3]


	

stars(n)

for i in range(n):
	for j in range(n):
		print(g_arr[i][j], end='')
	print()
