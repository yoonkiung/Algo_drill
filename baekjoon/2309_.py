from itertools import combinations
import sys

if __name__ == '__main__':
	arr = [None] * 9
	sum = 0
	for i in range(9):
		arr[i] = int(sys.stdin.readline())
		sum += arr[i]
	sum -= 100
	
	comb = list(combinations(arr, 2))
	for a, b in comb:
		if a + b == sum:
			arr.remove(a)
			arr.remove(b)
	
	arr.sort()
	print(*arr, sep='\n')
	